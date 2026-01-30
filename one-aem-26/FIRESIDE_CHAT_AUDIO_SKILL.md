# Skill: Fireside Chat Audio Generation

## What This Skill Does

Guides Claude through the end-to-end process of generating a fireside chat audio file from written workshop content. The pipeline has three phases: (1) write a conversational dialogue script from a source document, (2) generate multi-speaker audio via the ElevenLabs Text-to-Dialogue API, and (3) merge the resulting parts into a single MP3 using ffmpeg.

## Context

- **Format**: Fireside chat between two speakers — a male Moderator (MOD) and a female Thought Leader (TL)
- **Tone**: Casual, energetic, conversational — two smart people riffing, not reading slides
- **Source material**: Any structured markdown document (e.g., `workshop-recap.md`, `highlights.md`)
- **Output**: A single merged MP3 file in the `audio/` subdirectory
- **Intermediate artifacts**: A markdown script file and per-part MP3 files

## Prerequisites

- **Environment variable**: `ELEVENLABS_API_KEY` must be set (or present in a `.env` file loaded via `dotenv`)
- **ffmpeg**: Must be installed and available on PATH for the merge step
- **Python packages**: `requests`, `python-dotenv`

---

## Phase 1: Script Writing

### Input

A structured markdown document containing the content to be distilled into dialogue. The source may be a workshop recap, highlights file, or any content-rich document.

### Content Adaptation Strategy

1. Read the source document fully.
2. Select **4–6 themes** that make the strongest conversation. Do NOT try to cover everything — the goal is a compelling 15–20 minute dialogue, not an exhaustive summary.
3. For each theme, identify the most vivid details, quotes, and examples. Strip out anything that works on paper but dies in audio (tables, bullet lists, acronym-heavy sections).
4. Arrange themes in a natural conversational arc: opening hook → escalating substance → human/cultural turn → forward-looking close.

### Script Markdown Structure

```markdown
# Title: A Fireside Chat

> **Format**: ~18-minute fireside chat
> **Speakers**: MOD (Moderator, male) — TL (Thought Leader, female)
> **Source**: [source document description]
> **Note**: Script is split into N parts for ElevenLabs Text-to-Dialogue API generation.

---

## Part 1: [Part Title]

**MOD:** [dialogue text]

**TL:** [dialogue text]

**MOD:** [dialogue text]

---

## Part 2: [Part Title]

...
```

### Dialogue Writing Rules (Critical)

These rules are the single biggest determinant of audio quality. Follow them exactly.

**Voice and register:**
- Use contractions always ("it's", "don't", "that's", "we're" — never the uncontracted form)
- Include conversational fillers naturally — roughly 1 per 3–4 turns ("So —", "I mean,", "Look,", "Right.", "Honestly,", "And here's the thing —")
- Use sentence fragments for reactions ("Exactly.", "Bold.", "Which is wild.", "Strong note to end on.")
- Use dashes for interruptions or pivots ("So — nine sessions, two keynotes...")
- Use ellipses for trailing off ("the distance between those isn't incremental...")
- Vary sentence length aggressively: mix 5-word punches with 30-word explanations

**Speaker behavior:**
- **MOD** reacts before asking the next question. Never just ask a bare question — acknowledge, reframe, or push back first. ("That's a powerful opener. And then you had two external keynotes...")
- **TL** uses concrete examples, names, and numbers. Abstract statements must be grounded immediately. ("Boris shipped over three hundred pull requests. One person.")
- Both speakers can express surprise, humor, or skepticism. This is a conversation, not an interview.

**Audio tags:**
- Permitted tags: `[laughing]`, `[sighing]`, `[whispering]`, `[excited]`
- Use sparingly: **maximum 2–3 per part**
- Place them at the start of a turn or between sentences, never mid-sentence

**Formatting rules:**
- Strip ALL markdown from dialogue text — no bold, italic, links, bullet points, or backticks inside the `**MOD:**` or `**TL:**` lines. The API receives raw text only.
- Use `---` separators between parts
- Each part gets a `## Part N: [Title]` header

### Part Sizing

| Metric | Target | Hard Limit |
|--------|--------|------------|
| Characters per part | 3,000–4,500 | 5,000 |
| Turns per part | 8–16 | 20 |
| Total parts | 4–6 | 8 |

If a part exceeds 5,000 characters, the chunking logic in Phase 2 will split it — but this produces audible seams. Write within limits.

---

## Phase 2: Audio Generation

### API Configuration

| Setting | Value |
|---------|-------|
| Endpoint | `https://api.elevenlabs.io/v1/text-to-dialogue` |
| Method | POST |
| Auth header | `xi-api-key: <ELEVENLABS_API_KEY>` |
| Content-Type | `application/json` |
| Model | `eleven_v3` |
| Output format (query param) | `mp3_44100_128` |
| Stability | `0.0` (most expressive — see Lessons Learned) |

### Default Voice IDs

| Speaker | Voice | Voice ID |
|---------|-------|----------|
| MOD | Chris — Charming, Down-to-Earth (male) | `iP95p4xoKVk53GoZ742B` |
| TL | Sarah — Mature, Reassuring, Confident (female) | `EXAVITQu4vr4xnSDxMaL` |

### Request Payload

```json
{
  "inputs": [
    { "text": "Turn 1 text...", "voice_id": "<MOD_VOICE_ID>" },
    { "text": "Turn 2 text...", "voice_id": "<TL_VOICE_ID>" }
  ],
  "model_id": "eleven_v3",
  "settings": {
    "stability": 0.0
  }
}
```

The `output_format` is passed as a **query parameter**, not in the JSON body:

```
POST https://api.elevenlabs.io/v1/text-to-dialogue?output_format=mp3_44100_128
```

### Script Parsing

Use these regex patterns to extract dialogue from the markdown script:

**Split script into parts:**
```python
part_sections = re.split(r"## Part \d+:.*\n", content)
part_sections = [p.strip() for p in part_sections if p.strip() and "**MOD:**" in p]
```

**Extract speaker turns within a part:**
```python
pattern = r"\*\*(MOD|TL):\*\*\s*(.*?)(?=\*\*(?:MOD|TL):\*\*|---|\Z)"
matches = re.findall(pattern, part_text, re.DOTALL)
```

**Clean extracted text (remove any residual markdown bold):**
```python
clean = re.sub(r"\*\*([^*]+)\*\*", r"\1", text.strip())
clean = clean.replace("---", "").strip()
```

### Chunking Strategy

The API has a practical character limit of ~5,000 characters per call (total across all inputs in a single request).

**Rules:**
1. Never split a speaker turn across chunks. A turn is atomic.
2. Accumulate turns into a chunk until adding the next turn would exceed the limit.
3. When a part requires multiple chunks, use letter suffixes: `part1_a.mp3`, `part1_b.mp3`, etc.

```python
suffix = f"_{chr(97+j)}" if len(chunks) > 1 else ""
label = f"part{i+1}{suffix}"
```

**File naming:** `fireside_chat_part1.mp3`, `fireside_chat_part2.mp3`, or `fireside_chat_part1_a.mp3`, `fireside_chat_part1_b.mp3` if chunked.

### Error Handling

- Check for `ELEVENLABS_API_KEY` before starting. Exit with a clear message if missing.
- Set a request timeout of 300 seconds (audio generation is slow for long inputs).
- On non-200 response, log the status code and first 500 characters of the response body, then continue to the next chunk.
- Track success/failure counts and report a summary at the end.
- If any chunk fails, continue generating the rest — partial output is better than none.

### Generation Script

Write a Python script (`generate_fireside_audio.py`) with this structure:

```python
#!/usr/bin/env python3
"""Generate fireside chat audio via ElevenLabs Text-to-Dialogue API."""

import os, re, sys, requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("ELEVENLABS_API_KEY")
DIALOGUE_URL = "https://api.elevenlabs.io/v1/text-to-dialogue"
MODEL_ID = "eleven_v3"

VOICE_MOD = "iP95p4xoKVk53GoZ742B"  # Chris
VOICE_TL  = "EXAVITQu4vr4xnSDxMaL"  # Sarah

MAX_CHARS_PER_CALL = 5000

# Functions: parse_script, split_turns_into_chunks, build_payload, generate_audio, main
```

See `one-aem-26/generate_fireside_audio.py` for the full reference implementation.

---

## Phase 3: Merge with ffmpeg

After all parts are generated, merge them into a single MP3.

### Step 1: Create a concat list file

Write a text file (`concat_list.txt`) listing all generated MP3 files in order:

```
file 'fireside_chat_part1.mp3'
file 'fireside_chat_part1_b.mp3'
file 'fireside_chat_part2.mp3'
file 'fireside_chat_part3.mp3'
file 'fireside_chat_part4.mp3'
```

**Important:** Include chunked sub-parts in order (part1_a before part1_b before part2).

### Step 2: Run ffmpeg

```bash
ffmpeg -f concat -safe 0 -i concat_list.txt -c copy fireside_chat_full.mp3
```

- `-f concat` — use the concat demuxer
- `-safe 0` — allow relative paths in the list file
- `-c copy` — stream-copy without re-encoding (fast, lossless)

### Step 3: Verify

```bash
ffprobe fireside_chat_full.mp3
```

Check that the duration is reasonable (~15–20 minutes for a 4-part script).

---

## Full Pipeline Summary

```
Source Document (markdown)
        │
        ▼
  ┌─────────────┐
  │  Phase 1:   │  Claude writes a 4–6 part conversational script
  │  Script     │  Output: fireside-chat-full-script.md
  └──────┬──────┘
         │
         ▼
  ┌─────────────┐
  │  Phase 2:   │  Python script calls ElevenLabs API per chunk
  │  Audio Gen  │  Output: audio/fireside_chat_part*.mp3
  └──────┬──────┘
         │
         ▼
  ┌─────────────┐
  │  Phase 3:   │  ffmpeg concat merges all parts
  │  Merge      │  Output: audio/fireside_chat_full.mp3
  └─────────────┘
```

---

## Execution Approach

When the user asks to generate a fireside chat, Claude should:

1. **Read the source document** to understand the content.
2. **Write the script** following Phase 1 rules. Save as `fireside-chat-full-script.md` (or a name the user specifies).
3. **Review the script** — check character counts per part, verify no markdown in dialogue text, confirm conversational tone.
4. **Write the generation script** (`generate_fireside_audio.py`) following Phase 2 specs, or reuse the existing reference implementation if present.
5. **Run the generation script** — execute via `python generate_fireside_audio.py` and monitor output.
6. **Merge the output** — run the ffmpeg concat command from Phase 3.
7. **Verify** — check file sizes and duration with ffprobe.
8. **Report** — tell the user what was generated, total duration, and file locations.

---

## Iteration Support

The pipeline supports iterating on any phase independently:

- **Re-write a single part**: Edit the script, re-generate only that part's audio, re-merge.
- **Change voices**: Update the voice ID constants and re-run. No script changes needed.
- **Adjust expressiveness**: Change the `stability` setting (0.0 = most expressive, 1.0 = most stable). Re-run generation.
- **Re-generate a failed chunk**: Run the generation script targeting only the failed chunk label.
- **Try different content selection**: Rewrite the script with different theme choices from the same source document.

---

## Reference Implementation

The working implementation lives at:

- **Generation script**: `one-aem-26/generate_fireside_audio.py`
- **Full script example**: `one-aem-26/fireside-chat-full-script.md`
- **Generated audio**: `one-aem-26/audio/fireside_chat_full.mp3` (merged) and `one-aem-26/audio/fireside_chat_part*.mp3` (individual parts)

---

## Lessons Learned

These are hard-won insights from the development of this pipeline:

1. **Stability 0.0 produces the best results.** Counter-intuitively, minimum stability gives the most natural, expressive dialogue. Higher values sound robotic and flat. Start at 0.0 and only increase if you get artifacts.

2. **Script quality is ~80% of audio quality.** If the dialogue reads stiffly, no amount of voice tuning will fix it. Invest the most effort in Phase 1. Read the script aloud before generating — if it sounds awkward to a human, it will sound worse from the API.

3. **Never split a speaker turn.** Splitting mid-turn creates audible discontinuities. Always keep a complete turn in one chunk, even if the chunk is slightly under-filled.

4. **Strip ALL markdown from dialogue text.** Bold markers, links, backticks — the API will attempt to read them literally. The parsing regex handles bold, but manually verify no other markdown leaks through.

5. **The Text-to-Dialogue endpoint handles speaker transitions naturally.** Unlike per-line TTS + concatenation, the dialogue endpoint produces natural conversational flow, pacing, and turn-taking. Always prefer it over manual concatenation.

6. **Character limits are per-request, not per-turn.** The 5,000 character limit applies to the total text across all `inputs` in a single API call. Individual turns can be long as long as the chunk total stays under the limit.

7. **Use `mp3_44100_128` output format.** This gives broadcast-quality audio. Lower bitrates are noticeably worse for speech. Higher sample rates provide no perceptible benefit.

8. **ffmpeg concat with `-c copy` is instant and lossless.** No re-encoding needed when all parts share the same codec and sample rate. The merge step takes milliseconds.

9. **Contractions are non-negotiable.** "It is" vs "It's" — the API will read uncontracted forms with unnatural emphasis. Always contract.

10. **Name and attribute quotes in dialogue.** Concrete names ("Boris shipped 300 PRs", "Loni Stark called it Disneylandification") make the audio vivid. Abstract statements ("a leader mentioned...") sound like filler.
