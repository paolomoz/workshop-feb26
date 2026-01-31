#!/usr/bin/env python3
"""
Generate fireside chat audio from the full script using ElevenLabs Text-to-Dialogue API.
Splits the script into parts to stay within API limits, generates one audio file per part.
"""

from __future__ import annotations

import os
import re
import sys
import requests
from dotenv import load_dotenv

load_dotenv()

# --- Configuration ---
API_KEY = os.getenv("ELEVENLABS_API_KEY")
DIALOGUE_URL = "https://api.elevenlabs.io/v1/text-to-dialogue"
MODEL_ID = "eleven_v3"

# Voice assignments
VOICE_MOD = "iP95p4xoKVk53GoZ742B"  # Chris - Charming, Down-to-Earth (male moderator)
VOICE_TL = "EXAVITQu4vr4xnSDxMaL"   # Sarah - Mature, Reassuring, Confident (female thought leader)

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SCRIPT_PATH = os.path.join(SCRIPT_DIR, "fireside-chat-full-script.md")
OUTPUT_DIR = os.path.join(SCRIPT_DIR, "audio")

# Max characters per API call (total text across all inputs)
MAX_CHARS_PER_CALL = 5000


def parse_script(filepath: str) -> list[list[tuple[str, str]]]:
    """
    Parse the markdown script into a list of parts,
    each part being a list of (speaker, text) tuples.
    """
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Split by Part headers
    part_sections = re.split(r"## Part \d+:.*\n", content)
    # Keep only sections that contain dialogue
    part_sections = [p.strip() for p in part_sections if p.strip() and "**MOD:**" in p]

    all_parts = []
    for part_text in part_sections:
        turns = []
        # Match **MOD:** or **TL:** followed by text until the next speaker or section break
        pattern = r"\*\*(MOD|TL):\*\*\s*(.*?)(?=\*\*(?:MOD|TL):\*\*|---|\Z)"
        matches = re.findall(pattern, part_text, re.DOTALL)
        for speaker, text in matches:
            clean = text.strip()
            # Remove markdown bold markers
            clean = re.sub(r"\*\*([^*]+)\*\*", r"\1", clean)
            clean = clean.replace("---", "").strip()
            if clean:
                turns.append((speaker, clean))
        if turns:
            all_parts.append(turns)

    return all_parts


def split_turns_into_chunks(turns: list[tuple[str, str]], max_chars: int) -> list[list[tuple[str, str]]]:
    """Split a list of turns into chunks that each fit within the character limit."""
    chunks = []
    current_chunk = []
    current_chars = 0

    for speaker, text in turns:
        text_len = len(text)
        if current_chars + text_len > max_chars and current_chunk:
            chunks.append(current_chunk)
            current_chunk = []
            current_chars = 0
        current_chunk.append((speaker, text))
        current_chars += text_len

    if current_chunk:
        chunks.append(current_chunk)

    return chunks


def build_payload(turns: list[tuple[str, str]]) -> dict:
    """Build the ElevenLabs API request payload."""
    inputs = []
    for speaker, text in turns:
        voice_id = VOICE_MOD if speaker == "MOD" else VOICE_TL
        inputs.append({"text": text, "voice_id": voice_id})

    return {"inputs": inputs, "model_id": MODEL_ID}


def generate_audio(payload: dict, output_path: str) -> bool:
    """Call the ElevenLabs Text-to-Dialogue API and save the audio file."""
    headers = {
        "xi-api-key": API_KEY,
        "Content-Type": "application/json",
    }

    total_chars = sum(len(inp["text"]) for inp in payload["inputs"])
    num_turns = len(payload["inputs"])
    print(f"  Sending {num_turns} turns, {total_chars} chars to API...")

    try:
        response = requests.post(
            DIALOGUE_URL,
            headers=headers,
            json=payload,
            params={"output_format": "mp3_44100_128"},
            timeout=300,
        )
    except requests.RequestException as exc:
        print(f"  Request failed: {exc}")
        return False

    if response.status_code == 200:
        with open(output_path, "wb") as f:
            f.write(response.content)
        size_mb = len(response.content) / (1024 * 1024)
        print(f"  Saved: {output_path} ({size_mb:.2f} MB)")
        return True
    else:
        print(f"  ERROR {response.status_code}: {response.text[:500]}")
        return False


def main():
    print("=== Fireside Chat Audio Generator (Full Script) ===\n")

    if not API_KEY:
        print("ERROR: ELEVENLABS_API_KEY not found in environment or .env file")
        sys.exit(1)

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # Parse script
    print(f"Parsing script: {SCRIPT_PATH}")
    parts = parse_script(SCRIPT_PATH)
    if not parts:
        print("ERROR: No dialogue parts found in script.")
        sys.exit(1)
    print(f"Found {len(parts)} script parts.\n")

    # Build all chunks across all parts
    all_chunks = []
    for i, part_turns in enumerate(parts):
        total_chars = sum(len(t) for _, t in part_turns)
        print(f"Part {i+1}: {len(part_turns)} turns, {total_chars} chars")
        chunks = split_turns_into_chunks(part_turns, MAX_CHARS_PER_CALL)
        for j, chunk in enumerate(chunks):
            chunk_chars = sum(len(t) for _, t in chunk)
            suffix = f"_{chr(97+j)}" if len(chunks) > 1 else ""
            label = f"part{i+1}{suffix}"
            desc = f"Part {i+1}" + (f" (chunk {j+1}/{len(chunks)})" if len(chunks) > 1 else "")
            print(f"  {desc}: {len(chunk)} turns, {chunk_chars} chars")
            all_chunks.append((label, chunk))

    print(f"\nTotal API calls needed: {len(all_chunks)}\n")
    print("=" * 50)

    # Generate audio for each chunk
    generated = []
    for idx, (label, chunk_turns) in enumerate(all_chunks):
        output_path = os.path.join(OUTPUT_DIR, f"fireside_chat_{label}.mp3")
        print(f"\n[{idx+1}/{len(all_chunks)}] Generating {label}...")
        payload = build_payload(chunk_turns)

        if generate_audio(payload, output_path):
            generated.append(output_path)
        else:
            print(f"  Failed to generate {label}. Continuing...")

    # Summary
    print(f"\n{'=' * 50}")
    print(f"Generation complete. {len(generated)}/{len(all_chunks)} files created.")
    print(f"Output directory: {OUTPUT_DIR}/")
    for f in generated:
        print(f"  - {os.path.basename(f)}")

    if len(generated) < len(all_chunks):
        print(f"\nWARNING: {len(all_chunks) - len(generated)} file(s) failed to generate.")
        sys.exit(1)

    print("\nDone!")


if __name__ == "__main__":
    main()
