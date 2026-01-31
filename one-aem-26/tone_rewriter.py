#!/usr/bin/env python3
"""Rewrite prose from third-person analytical tone to second-person direct tone.

Uses Claude API (Sonnet) with SHA-256 caching so only changed fields
hit the API on subsequent builds.
"""

import copy
import hashlib
import json
import os
import time
import urllib.request
import urllib.error

# Bump this integer whenever you change SYSTEM_PROMPT to invalidate all caches.
TONE_PROMPT_VERSION = 1

SYSTEM_PROMPT = (
    "Rewrite text from third-person analytical tone to second-person direct tone.\n"
    "Rules:\n"
    '- "The team should..." → "You should..." or "We should..."\n'
    '- "Engineers become..." → "You become..."\n'
    '- "The engineer\'s job..." → "Your job..."\n'
    "- Preserve ALL <strong> HTML tags exactly\n"
    "- Preserve ALL <br> HTML tags exactly\n"
    "- Preserve factual content, names, attributions, data points\n"
    "- Keep same sentence count and text length (±15%)\n"
    "- Output JSON only with same keys as input\n"
)

CACHE_FILE = os.path.join(os.path.dirname(__file__), '.tone_cache.json')
MODEL = "claude-sonnet-4-20250514"


# ---------------------------------------------------------------------------
# Env / API key
# ---------------------------------------------------------------------------

def load_env():
    """Load .env from project root (same pattern as generate_images.py)."""
    env_path = os.path.join(os.path.dirname(__file__), '..', '.env')
    env = {}
    if not os.path.exists(env_path):
        return env
    with open(env_path) as f:
        for line in f:
            line = line.strip()
            if '=' in line and not line.startswith('#'):
                key, val = line.split('=', 1)
                env[key.strip()] = val.strip().strip('"')
    return env


# ---------------------------------------------------------------------------
# Prose extraction
# ---------------------------------------------------------------------------

def extract_prose(sections, hero_sub, hero_quote, synth_blocks):
    """Walk all data structures and return {key: original_text} for every
    prose field that should be tone-rewritten."""
    prose = {}

    # Hero
    prose["hero:subtitle"] = hero_sub
    prose["hero:quote"] = hero_quote

    # Sections
    for sec in sections:
        sid = sec["id"]
        if sec.get("summary"):
            prose[f"section:{sid}:summary"] = sec["summary"]
        for i, d in enumerate(sec.get("details", [])):
            prose[f"section:{sid}:details:{i}"] = d
        if sec.get("why"):
            prose[f"section:{sid}:why"] = sec["why"]

        for sub in sec.get("sub_items", []):
            sub_id = sub["id"]
            if sub.get("summary"):
                prose[f"sub:{sub_id}:summary"] = sub["summary"]
            for i, d in enumerate(sub.get("details", [])):
                prose[f"sub:{sub_id}:details:{i}"] = d
            if sub.get("why"):
                prose[f"sub:{sub_id}:why"] = sub["why"]

    # Synthesis blocks
    for i, b in enumerate(synth_blocks):
        prose[f"synth:{i}:heading"] = b["heading"]
        prose[f"synth:{i}:body"] = b["body"]

    return prose


# ---------------------------------------------------------------------------
# Cache management
# ---------------------------------------------------------------------------

def _sha(text):
    return hashlib.sha256(text.encode('utf-8')).hexdigest()


def load_cache():
    if not os.path.exists(CACHE_FILE):
        return {}
    with open(CACHE_FILE) as f:
        return json.load(f)


def save_cache(cache):
    tmp = CACHE_FILE + '.tmp'
    with open(tmp, 'w') as f:
        json.dump(cache, f, indent=2, ensure_ascii=False)
    os.replace(tmp, CACHE_FILE)


def find_stale_keys(prose, cache):
    """Return list of keys whose source text changed (or are missing from cache)."""
    stale = []
    cached_version = cache.get("_tone_prompt_version", 0)
    if cached_version != TONE_PROMPT_VERSION:
        # Prompt changed — everything is stale
        return list(prose.keys())
    for key, text in prose.items():
        entry = cache.get(key)
        if not entry or entry.get("source_hash") != _sha(text):
            stale.append(key)
    return stale


# ---------------------------------------------------------------------------
# Batching
# ---------------------------------------------------------------------------

def _section_prefix(key):
    """Group key by its section/scope for batching."""
    parts = key.split(":")
    if parts[0] == "hero":
        return "hero"
    if parts[0] == "synth":
        # Group by block index to keep batches small
        return f"synth:{parts[1]}"
    # section:ID:field or sub:ID:field — group by parent section ID
    return f"{parts[0]}:{parts[1]}"


def batch_by_section(stale_keys, prose):
    """Group stale keys into batches (one per section/scope)."""
    groups = {}
    for key in stale_keys:
        prefix = _section_prefix(key)
        groups.setdefault(prefix, {})[key] = prose[key]
    return list(groups.values())


# ---------------------------------------------------------------------------
# Claude API
# ---------------------------------------------------------------------------

def _repair_json(text):
    """Attempt to repair common LLM JSON issues (unescaped quotes, etc.)."""
    import re
    # Replace smart/curly quotes inside JSON string values with escaped versions
    # that won't break JSON parsing.  Smart quotes are multi-byte and should
    # already be valid inside JSON strings, so the real issue is usually the
    # model outputting unescaped ASCII double-quotes inside values.
    #
    # Strategy: find each "key": "value" pair and re-escape any inner "
    # We do this by matching the pattern greedily and using json.dumps
    # on individual value strings.

    # First try: see if it already parses
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        pass

    # Second try: the model sometimes wraps values in single quotes
    # or has trailing commas — try ast.literal_eval as fallback
    try:
        import ast
        result = ast.literal_eval(text)
        if isinstance(result, dict):
            return result
    except (ValueError, SyntaxError):
        pass

    # Third try: extract key-value pairs using a regex that handles
    # multi-line values with embedded HTML
    pairs = {}
    # Match "key": "value" where value can contain escaped quotes
    pattern = re.compile(
        r'"([^"]+?)"\s*:\s*"((?:[^"\\]|\\.)*)"',
        re.DOTALL
    )
    for m in pattern.finditer(text):
        pairs[m.group(1)] = m.group(2).replace('\\"', '"').replace('\\n', '\n')

    if pairs:
        return pairs

    return None


def call_claude(user_json, env, retries=1):
    """Send a batch of {key: text} to Claude and get back {key: rewritten_text}.

    Uses Messages API via urllib.request (no SDK dependency).
    """
    api_key = env.get("ANTHROPIC_API_KEY", "")
    if not api_key:
        return None

    payload = {
        "model": MODEL,
        "max_tokens": 8192,
        "system": SYSTEM_PROMPT,
        "messages": [
            {
                "role": "user",
                "content": (
                    "Rewrite the following JSON values. Return ONLY valid JSON "
                    "with the same keys. Escape all double quotes inside values "
                    "with backslash. Do not add any text outside the JSON object.\n\n"
                    + json.dumps(user_json, ensure_ascii=False)
                ),
            }
        ],
    }

    data = json.dumps(payload).encode('utf-8')
    req = urllib.request.Request(
        "https://api.anthropic.com/v1/messages",
        data=data,
        headers={
            "Content-Type": "application/json",
            "x-api-key": api_key,
            "anthropic-version": "2023-06-01",
        },
        method="POST",
    )

    for attempt in range(1 + retries):
        try:
            with urllib.request.urlopen(req, timeout=120) as resp:
                result = json.loads(resp.read().decode('utf-8'))

            # Extract text from the response
            text_block = result.get("content", [{}])[0].get("text", "")

            # Strip markdown code fences if present
            stripped = text_block.strip()
            if stripped.startswith("```"):
                lines = stripped.split("\n")
                lines = lines[1:]  # drop ```json or ```
                if lines and lines[-1].strip() == "```":
                    lines = lines[:-1]
                stripped = "\n".join(lines)

            # Try parsing with repair fallback
            parsed = _repair_json(stripped)
            if parsed is not None:
                return parsed

            raise json.JSONDecodeError("repair failed", stripped, 0)

        except (json.JSONDecodeError, KeyError, IndexError) as e:
            if attempt < retries:
                print(f"    [RETRY] Malformed JSON response, retrying... ({e})")
                time.sleep(2)
                continue
            print(f"    [ERROR] Malformed JSON response after retries: {e}")
            return None
        except urllib.error.HTTPError as e:
            body = e.read().decode('utf-8', errors='replace')
            print(f"    [ERROR] HTTP {e.code}: {body[:300]}")
            return None
        except Exception as e:
            print(f"    [ERROR] API call failed: {e}")
            return None

    return None


# ---------------------------------------------------------------------------
# Apply rewrites to data structures
# ---------------------------------------------------------------------------

def _apply_to_data(sections, hero_sub, hero_quote, synth_blocks, rewrites):
    """Return deep copies of all data structures with rewrites applied."""
    sections = copy.deepcopy(sections)
    synth_blocks = copy.deepcopy(synth_blocks)

    for key, text in rewrites.items():
        parts = key.split(":")

        if parts[0] == "hero":
            if parts[1] == "subtitle":
                hero_sub = text
            elif parts[1] == "quote":
                hero_quote = text

        elif parts[0] == "synth":
            idx = int(parts[1])
            field = parts[2]
            synth_blocks[idx][field] = text

        elif parts[0] == "section":
            sid = parts[1]
            field = parts[2]
            for sec in sections:
                if sec["id"] == sid:
                    if field == "summary":
                        sec["summary"] = text
                    elif field == "details":
                        sec["details"][int(parts[3])] = text
                    elif field == "why":
                        sec["why"] = text
                    break

        elif parts[0] == "sub":
            sub_id = parts[1]
            field = parts[2]
            for sec in sections:
                for sub in sec.get("sub_items", []):
                    if sub["id"] == sub_id:
                        if field == "summary":
                            sub["summary"] = text
                        elif field == "details":
                            sub["details"][int(parts[3])] = text
                        elif field == "why":
                            sub["why"] = text
                        break

    return sections, hero_sub, hero_quote, synth_blocks


def apply_cached(sections, hero_sub, hero_quote, synth_blocks):
    """Apply cached rewrites without calling the API."""
    cache = load_cache()
    if not cache:
        return sections, hero_sub, hero_quote, synth_blocks

    rewrites = {}
    for key, entry in cache.items():
        if key.startswith("_"):
            continue
        if "rewritten" in entry:
            rewrites[key] = entry["rewritten"]

    if not rewrites:
        return sections, hero_sub, hero_quote, synth_blocks

    return _apply_to_data(sections, hero_sub, hero_quote, synth_blocks, rewrites)


# ---------------------------------------------------------------------------
# Main entry point
# ---------------------------------------------------------------------------

def rewrite_all(sections, hero_sub, hero_quote, synth_blocks, clear_cache=False):
    """Rewrite all prose fields via Claude API. Returns updated copies.

    - Checks cache, only sends stale fields to API.
    - On API failure, falls back to original text for those fields.
    """
    env = load_env()
    api_key = env.get("ANTHROPIC_API_KEY", "")
    if not api_key:
        print("[tone] WARNING: ANTHROPIC_API_KEY not found in .env — using original tone")
        return sections, hero_sub, hero_quote, synth_blocks

    # Extract all prose
    prose = extract_prose(sections, hero_sub, hero_quote, synth_blocks)

    # Load or clear cache
    if clear_cache:
        cache = {}
        print("[tone] Cache cleared — rebuilding all fields")
    else:
        cache = load_cache()

    # Find stale keys
    stale = find_stale_keys(prose, cache)

    if not stale:
        print(f"[tone] All {len(prose)} fields are cached — no API calls needed")
        return apply_cached(sections, hero_sub, hero_quote, synth_blocks)

    print(f"[tone] {len(stale)} of {len(prose)} fields need rewriting")

    # Batch and send
    batches = batch_by_section(stale, prose)
    new_rewrites = {}

    for i, batch in enumerate(batches, 1):
        keys_label = ", ".join(list(batch.keys())[:3])
        if len(batch) > 3:
            keys_label += f" (+{len(batch) - 3} more)"
        print(f"  [{i}/{len(batches)}] Rewriting: {keys_label}")

        result = call_claude(batch, env)

        if result:
            for key, rewritten in result.items():
                if key in batch:
                    new_rewrites[key] = rewritten
                    cache[key] = {
                        "source_hash": _sha(batch[key]),
                        "rewritten": rewritten,
                    }
        else:
            print(f"    [SKIP] Falling back to original tone for this batch")

        # Rate limiting
        if i < len(batches):
            time.sleep(1)

    # Update prompt version
    cache["_tone_prompt_version"] = TONE_PROMPT_VERSION

    # Save cache (only on success — no partial writes)
    save_cache(cache)
    print(f"[tone] Cache saved: {CACHE_FILE}")

    # Merge cached + new rewrites and apply
    all_rewrites = {}
    for key, entry in cache.items():
        if key.startswith("_"):
            continue
        if "rewritten" in entry:
            all_rewrites[key] = entry["rewritten"]

    return _apply_to_data(sections, hero_sub, hero_quote, synth_blocks, all_rewrites)
