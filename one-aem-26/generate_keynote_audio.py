#!/usr/bin/env python3
"""
Generate ElevenLabs TTS audio from the keynote script.
Chunks the text at paragraph breaks and concatenates MP3 output.
"""

import re
import requests
import os
import sys

# --- Configuration ---
API_KEY = "0804f46fabe8bd1e44e737e8a5339352961a73fb794652a5dcb200cdf1b2f976"
VOICE_ID = "onwK4e9ZLuTAKqWW03F9"  # Daniel
MODEL_ID = "eleven_multilingual_v2"
VOICE_SETTINGS = {
    "stability": 0.3,
    "similarity_boost": 0.75,
    "style": 0.7,
    "use_speaker_boost": True,
}
MAX_CHUNK_CHARS = 4500

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
INPUT_PATH = os.path.join(SCRIPT_DIR, "keynote_script.md")
OUTPUT_PATH = os.path.join(SCRIPT_DIR, "keynote_audio.mp3")

TTS_URL = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}"

# --- Step 1: Read the script ---
print(f"Reading script from {INPUT_PATH} ...")
with open(INPUT_PATH, "r", encoding="utf-8") as f:
    raw_text = f.read()

# --- Step 2: Strip markdown title/metadata header ---
# Remove lines before (and including) the first '---' separator.
# The header typically looks like:
#   # Title
#   _subtitle_
#   ---
# We strip everything up to and including the first '---' line.
lines = raw_text.split("\n")
body_start = 0
for i, line in enumerate(lines):
    if line.strip() == "---":
        body_start = i + 1
        break

body_text = "\n".join(lines[body_start:]).strip()
print(f"Body text length: {len(body_text)} characters")

# --- Step 3: Chunk the text at paragraph breaks (double newlines) ---
paragraphs = re.split(r"\n\n+", body_text)
chunks = []
current_chunk = ""

for para in paragraphs:
    # If adding this paragraph would exceed the limit, flush current chunk
    if current_chunk and (len(current_chunk) + 2 + len(para)) > MAX_CHUNK_CHARS:
        chunks.append(current_chunk.strip())
        current_chunk = para
    else:
        if current_chunk:
            current_chunk += "\n\n" + para
        else:
            current_chunk = para

if current_chunk.strip():
    chunks.append(current_chunk.strip())

print(f"Split into {len(chunks)} chunk(s):")
for idx, chunk in enumerate(chunks):
    print(f"  Chunk {idx + 1}: {len(chunk)} chars")

# --- Step 4: Generate audio for each chunk ---
headers = {
    "xi-api-key": API_KEY,
    "Content-Type": "application/json",
    "Accept": "audio/mpeg",
}

audio_parts = []

for idx, chunk in enumerate(chunks):
    print(f"\nGenerating audio for chunk {idx + 1}/{len(chunks)} ...")
    payload = {
        "text": chunk,
        "model_id": MODEL_ID,
        "voice_settings": VOICE_SETTINGS,
    }
    resp = requests.post(TTS_URL, headers=headers, json=payload, timeout=120)
    if resp.status_code != 200:
        print(f"ERROR: ElevenLabs API returned status {resp.status_code}")
        print(resp.text[:500])
        sys.exit(1)
    audio_data = resp.content
    print(f"  Received {len(audio_data)} bytes of audio")
    audio_parts.append(audio_data)

# --- Step 5: Concatenate and save ---
print(f"\nConcatenating {len(audio_parts)} audio part(s) ...")
with open(OUTPUT_PATH, "wb") as out:
    for part in audio_parts:
        out.write(part)

file_size = os.path.getsize(OUTPUT_PATH)
print(f"\nSaved to {OUTPUT_PATH}")
print(f"Output file size: {file_size:,} bytes ({file_size / 1024:.1f} KB)")
print("Done!")
