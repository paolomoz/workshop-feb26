#!/usr/bin/env python3
"""
Generate an audio file from the Synthesis section of highlights.md
using the ElevenLabs Text-to-Speech API.
"""

import re
import sys
import os
import requests

# Configuration
HIGHLIGHTS_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "highlights.md")
OUTPUT_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "synthesis_audio.mp3")
VOICE_ID = "onwK4e9ZLuTAKqWW03F9"  # Daniel - Steady Broadcaster, British
MODEL_ID = "eleven_multilingual_v2"
API_KEY = "0804f46fabe8bd1e44e737e8a5339352961a73fb794652a5dcb200cdf1b2f976"
CHUNK_LIMIT = 4500  # safe limit under 5000 chars

API_URL = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}"


def read_highlights(path: str) -> str:
    """Read the highlights.md file."""
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def extract_synthesis(content: str) -> str:
    """Extract the Synthesis: Top Takeaways section."""
    # Find '## Synthesis'
    match = re.search(r'^## Synthesis.*$', content, re.MULTILINE)
    if not match:
        print("ERROR: Could not find '## Synthesis' section in highlights.md")
        sys.exit(1)

    start = match.start()
    rest = content[start:]

    # Find end: next '## ' heading (not ###) or '---' separator after the first line
    lines = rest.split('\n')
    end_line = len(lines)
    for i, line in enumerate(lines):
        if i == 0:
            continue
        stripped = line.strip()
        if stripped.startswith('## ') or stripped == '---':
            end_line = i
            break

    synthesis = '\n'.join(lines[:end_line])
    return synthesis


def strip_markdown(text: str) -> str:
    """Convert markdown to natural spoken text."""

    # Remove the main title line (## Synthesis: Top Takeaways)
    text = re.sub(r'^## .+\n', '', text)

    # Convert ### headings to spoken section breaks
    text = re.sub(r'^### (.+)$', r'\n\1.\n', text, flags=re.MULTILINE)

    # Remove italic markers used for descriptions
    text = re.sub(r'_\(Sources?:[^)]+\)_', '', text)
    text = re.sub(r'_([^_]+)_', r'\1', text)

    # Remove bold markers
    text = re.sub(r'\*\*([^*]+)\*\*', r'\1', text)

    # Convert code blocks to plain text
    text = re.sub(r'```[^\n]*\n(.*?)```', r'\1', text, flags=re.DOTALL)

    # Remove inline code backticks
    text = re.sub(r'`([^`]+)`', r'\1', text)

    # Convert bullet points to natural list items
    text = re.sub(r'^- ', '  ', text, flags=re.MULTILINE)

    # Convert numbered list items (already natural)
    text = re.sub(r'^(\d+)\. ', r'\1: ', text, flags=re.MULTILINE)

    # Convert arrows to "to"
    text = re.sub(r'→', 'to', text)

    # Remove markdown link syntax
    text = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', text)

    # Remove reference markers like (O), (W), etc. at end of sentences
    text = re.sub(r'\s*\([A-Z, ]+\)', '', text)

    # Clean up excessive whitespace
    text = re.sub(r'\n{3,}', '\n\n', text)
    text = text.strip()

    return text


def chunk_text(text: str, limit: int) -> list:
    """Split text into chunks at paragraph boundaries, respecting the character limit."""
    paragraphs = text.split('\n\n')
    chunks = []
    current_chunk = ""

    for para in paragraphs:
        para = para.strip()
        if not para:
            continue
        # If adding this paragraph would exceed the limit, save current and start new
        candidate = (current_chunk + "\n\n" + para).strip() if current_chunk else para
        if len(candidate) > limit and current_chunk:
            chunks.append(current_chunk.strip())
            current_chunk = para
        else:
            current_chunk = candidate

    if current_chunk.strip():
        chunks.append(current_chunk.strip())

    return chunks


def generate_audio(text: str) -> bytes:
    """Send text to ElevenLabs TTS and return audio bytes."""
    headers = {
        "xi-api-key": API_KEY,
        "Content-Type": "application/json",
        "Accept": "audio/mpeg",
    }
    payload = {
        "text": text,
        "model_id": MODEL_ID,
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.75,
            "style": 0.0,
            "use_speaker_boost": True,
        },
    }

    response = requests.post(API_URL, json=payload, headers=headers, timeout=120)

    if response.status_code != 200:
        print(f"ERROR: API returned status {response.status_code}")
        print(f"Response: {response.text[:500]}")
        sys.exit(1)

    return response.content


def main():
    print("Step 1: Reading highlights.md...")
    content = read_highlights(HIGHLIGHTS_PATH)

    print("Step 2: Extracting Synthesis section...")
    synthesis = extract_synthesis(content)
    print(f"  Extracted {len(synthesis)} characters of raw markdown.")

    print("Step 3: Stripping markdown formatting...")
    clean_text = strip_markdown(synthesis)
    print(f"  Clean text: {len(clean_text)} characters.")
    print(f"  Preview: {clean_text[:200]}...")

    print("Step 4: Preparing text chunks...")
    chunks = chunk_text(clean_text, CHUNK_LIMIT)
    print(f"  Split into {len(chunks)} chunk(s).")
    for i, chunk in enumerate(chunks):
        print(f"    Chunk {i + 1}: {len(chunk)} characters")

    print("Step 5: Generating audio via ElevenLabs API...")
    audio_parts = []
    for i, chunk in enumerate(chunks):
        print(f"  Generating chunk {i + 1}/{len(chunks)}...")
        audio_data = generate_audio(chunk)
        audio_parts.append(audio_data)
        print(f"    Received {len(audio_data)} bytes of audio.")

    print("Step 6: Writing output file...")
    with open(OUTPUT_PATH, "wb") as f:
        for part in audio_parts:
            f.write(part)

    total_size = os.path.getsize(OUTPUT_PATH)
    print(f"\nDone! Audio saved to: {OUTPUT_PATH}")
    print(f"File size: {total_size / 1024:.1f} KB")


if __name__ == "__main__":
    main()
