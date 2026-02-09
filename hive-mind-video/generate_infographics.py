#!/usr/bin/env python3
"""Generate all 8 knolling infographics for The Anthropic Hive Mind video."""

import os
import sys
from pathlib import Path

try:
    from google import genai
    from google.genai import types
except ImportError:
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-q", "google-genai"])
    from google import genai
    from google.genai import types

# Load .env
from dotenv import load_dotenv
load_dotenv(Path(__file__).parent / ".env")
load_dotenv(Path(__file__).parent.parent / ".env")


def generate_image(prompt: str, output_path: str, aspect_ratio: str = "16:9") -> str:
    """Generate an image using Gemini 3 Pro Image (Nano Banana Pro)."""
    api_key = os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        raise ValueError("GOOGLE_API_KEY environment variable not set")

    client = genai.Client(api_key=api_key)

    response = client.models.generate_content(
        model="gemini-3-pro-image-preview",
        contents=prompt,
        config=types.GenerateContentConfig(
            response_modalities=["IMAGE"],
            image_config=types.ImageConfig(
                aspect_ratio=aspect_ratio,
                image_size="2K",
            ),
        ),
    )

    # Extract image from response
    for part in response.parts:
        if part.inline_data is not None:
            output_file = Path(output_path)
            output_file.parent.mkdir(parents=True, exist_ok=True)
            image = part.as_image()
            image.save(str(output_file))
            print(f"Image saved to: {output_file}")
            return str(output_file)

    raise RuntimeError("No image was generated")

OUTPUT_DIR = Path(__file__).parent / "infographic"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

KNOLLING_BASE = """Perfectly organized objects arranged at precise 90-degree angles on a flat surface, photographed from directly overhead in a bird's-eye view. Every object casts a subtle drop shadow. Material-authentic textures: brushed metal grain, leather patina, wood grain, glass transparency. Equal spacing between all objects creating an invisible grid. Clean geometric sans-serif label typography in small white text. No perspective, no angle shots, everything in sharp focus. No clutter, no overlap, no casual placement. No text, no labels, no words, no letters, no writing, no captions."""

SECTIONS = [
    {
        "name": "01-intro",
        "prompt": f"""{KNOLLING_BASE} On a matte black felt surface: Top-left, a precise 5x8 grid of 40 small identical white business cards. Top-right, a polished brass NFL badge next to a brushed-steel tech company employee badge, same size. Center, a large polished chrome rocket ship model lying flat, nose pointing right, dominating the composition. Bottom-left, a row of 6 small gold stars ascending in size left to right. Bottom-right, a clean white label tag. Safety orange accent on the rocket engine nozzle. Machinist's bench aesthetic, obsessively organized.""",
    },
    {
        "name": "02-happy-but-sad",
        "prompt": f"""{KNOLLING_BASE} On a warm concrete gray surface: Two parallel columns of objects separated by a center gap. Left column (happy): a sparkler frozen mid-spark, a vintage small cardboard shipping box, a bright copper lightning bolt ornament, a small glass vial of gold glitter, a warm Edison bulb. Right column (sad): a small porcelain elf figurine, an antique brass hourglass with sand nearly gone, a single dried pressed flower, a tiny model village with miniature houses, a dark glass wave paperweight. Cherry red accent on the lightning bolt. Emotional contrast through objects.""",
    },
    {
        "name": "03-the-vibe-mind",
        "prompt": f"""{KNOLLING_BASE} On dark charcoal felt surface: Center, a large hexagonal brass honeycomb piece, polished and reflecting light. Radiating outward at precise compass points: a clipboard with a red X through it, a name tent card with a red X, a small white ceramic chip with a circuit pattern, a brass tuning fork, a small glass centrifuge vial, a network of tiny copper nodes connected by fine wire. Outer edge, one small wooden peg figure positioned at the very edge of the felt separated from the group by a wider gap. Electric blue accent glow on the ceramic chip. Network hub-and-spoke arrangement.""",
    },
    {
        "name": "04-how-to-end-a-golden-age",
        "prompt": f"""{KNOLLING_BASE} On natural birch plywood surface: Left-to-right chronological flow with three distinct clusters separated by wide gaps. Left cluster: a small gold ingot, a miniature cardboard shipping box, an upward-pointing copper arrow. Middle cluster in muted gray tones: a gray stone, a miniature wooden signpost, two small wooden figures pulling at the same object, a cookie with a bite mark. Right cluster in warm gold: a polished golden sphere with radiating brass rays, surrounded by many tiny brass bee figurines arranged on its surface. Bottom center, a brass ruler. Safety orange accent on the golden sphere. Timeline progression from gold to gray to gold.""",
    },
    {
        "name": "05-the-small-version",
        "prompt": f"""{KNOLLING_BASE} On warm natural birch plywood kraft paper surface: Top-left cluster, three tiny laptop models in a row, a miniature ceramic coffee cup, a small donut pastry, a croissant, three pairs of tiny shoes set aside neatly. Center row, a small glass fish bowl, a miniature brass megaphone, a tiny rolled parchment scroll, a red recording indicator dot, small white speech bubble cards. Bottom-left, a small hand mirror face-down. Bottom-right, a miniature hexagonal game tile with small wooden game pieces sorted by color and type. Cherry red accent on a crossed-out label. Progressive growth arrangement from simple to complex, corner to corner.""",
    },
    {
        "name": "06-the-campfire-model",
        "prompt": f"""{KNOLLING_BASE} On dark charcoal felt surface: Center, a small brass campfire model with tiny orange-tipped flames. Surrounding it in a square loop clockwise: a lump of raw gray clay, a small metal sculpting tool, a miniature shaped clay pot, a polished finished ceramic piece — showing evolution. Outside the loop: a printed card with a waterfall diagram with a red X through it, a document with a red X through it, a small brass calendar plate. Corner clusters of tiny wooden people figures seated in a circle. Safety orange accent on the campfire flame tips. Cyclical arrangement around a central focal point.""",
    },
    {
        "name": "07-improv-at-scale",
        "prompt": f"""{KNOLLING_BASE} On matte black surface: Center, a large polished brass theater comedy mask. Top row, three small white ceramic tiles with engraved numbers arranged in a precise line. Left cluster, a small chrome lever mechanism with 6 miniature brass arms radiating from a central pivot, each arm ending at a different small object. Right cluster, small identical brass bee figurines arranged in a tight hexagonal honeycomb formation, with one bee figurine separated and placed apart with a red mark beneath it. Safety orange accent on a brass plate beneath the mask. Hierarchical composition with central dominant object.""",
    },
    {
        "name": "08-more-to-come",
        "prompt": f"""{KNOLLING_BASE} On dark charcoal felt surface transitioning to warm concrete: Left, two small white ceramic question-mark tiles and two folded note cards, a small red rubber stamp. Center-left, a small brown beer bottle, a miniature silver server rack, a tiny castle wall with a moat. Center-right, a row of small gold token coins arranged in a precise line leading right, each slightly larger than the last forming a path. Right, four brass gate arches in ascending size in a row. Far right, a single large heavy brass block. Safety orange accent on the brass block. Left-to-right flow progression, building toward a climactic final object.""",
    },
]


def main():
    for i, section in enumerate(SECTIONS, 1):
        name = section["name"]
        output_path = OUTPUT_DIR / f"{name}.png"

        if output_path.exists():
            print(f"  [{i}/8] Skipping {name} (already exists)")
            continue

        print(f"\n  [{i}/8] Generating: {name}")
        print(f"  {'─' * 50}")

        try:
            generate_image(section["prompt"], str(output_path), "16:9")
            print(f"  ✓ Saved: {output_path}")
        except Exception as e:
            print(f"  ✗ Error on {name}: {e}")
            continue

    print(f"\n  Done! Infographics in: {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
