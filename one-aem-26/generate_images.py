#!/usr/bin/env python3
"""Generate AI infographic images for workshop experience using Imagen 4."""

import base64
import json
import os
import time
import urllib.request
import urllib.error

# Load API key from .env
def load_env():
    env_path = os.path.join(os.path.dirname(__file__), '..', '.env')
    env = {}
    with open(env_path) as f:
        for line in f:
            line = line.strip()
            if '=' in line and not line.startswith('#'):
                key, val = line.split('=', 1)
                env[key.strip()] = val.strip().strip('"')
    return env

env = load_env()
API_KEY = env['GOOGLE_AI_API_KEY']
API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/imagen-4.0-generate-001:predict?key={API_KEY}"
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), 'images')
os.makedirs(OUTPUT_DIR, exist_ok=True)

STYLE_PREFIX = "Detailed educational infographic diagram in warm vintage textbook style with cream paper background and soft decorative border."
STYLE_SUFFIX = "Hand-drawn illustrative style with clean labeled components, soft color fills, flow arrows, callout boxes. Warm earth tones with accent colors. Information-dense visual explanation, not decorative art."

IMAGES = [
    {
        "filename": "hero_header.png",
        "prompt": f"{STYLE_PREFIX} Central team of figures surrounded by orbiting AI agent icons, with arrows showing delegation flow from humans at top labeled 'Design, Plan, Verify' downward to agents at bottom labeled 'Execute, Build, Ship'. Title banner: 'Becoming an AI Native Team'. Four quadrants labeled: Technical, Cultural, Emotional, Organisational. {STYLE_SUFFIX}"
    },
    {
        "filename": "10x_fun.png",
        "prompt": f"{STYLE_PREFIX} Split-view diagram: LEFT side labeled 'Extraction' shows a figure grinding at a desk with downward arrows and 'more hours, more effort' labels. RIGHT side labeled 'Elevation' shows a figure standing on a rising platform delegating to agent icons below, with upward arrows and labels 'delegate grind, keep creative work, enjoy the ride.' Dividing line in center. Balance scale visual metaphor. {STYLE_SUFFIX}"
    },
    {
        "filename": "maturity_framework.png",
        "prompt": f"{STYLE_PREFIX} Ascending staircase diagram with 4 clearly labeled levels. Level 1 'AI User' with person typing and AI bubble. Level 2 'AI First' with person pointing to AI as first action. Level 3 'AI Native Individual' with person orchestrating multiple agents. Level 4 'AI Native Team' with group connected by shared infrastructure web. Arrows between levels labeled: 'Frequency', 'Structure', 'Collective'. Right side callout: 'Target: Everyone L3, Team L4'. {STYLE_SUFFIX}"
    },
    {
        "filename": "be_pirates.png",
        "prompt": f"{STYLE_PREFIX} Pirate ship diagram with labeled parts: the sails labeled 'Education Fund', the flag labeled 'Director+ Sanction', the hull labeled 'Psychological Safety', cannons labeled 'Tool Scouting' and 'Free Experimentation'. Ocean waves labeled 'Enterprise Procurement' and 'Fear of Getting in Trouble' crossed out. Banner: 'Be Pirates -- Break Rules, Expense Tools, Move Fast'. {STYLE_SUFFIX}"
    },
    {
        "filename": "core_principle.png",
        "prompt": f"{STYLE_PREFIX} Circular diagram showing the core principle in center reading 'If a task can be delegated to AI, invest time to build it and share it' with 3 ground rules radiating outward: 'Crazier = Better', 'Simple Implementation', 'Usable by Everyone'. Outer ring shows 8 prototype ideas A through H as small labeled icons arranged around the circle. {STYLE_SUFFIX}"
    },
    {
        "filename": "prototype_ideas.png",
        "prompt": f"{STYLE_PREFIX} Grid matrix layout of 8 labeled cards A through H, each with a small icon and one-line summary: A=Screen Buddy with eye icon, B=Meeting Pipeline with microphone icon, C=Auto-Demo with video icon, D=Feedback-to-Fix with loop icon, E=Self-Improving Loop with spiral icon, F=Cookbook with book icon, G=Status Harvester with dashboard icon, H=Workflow Shadowing with mirror icon. Connecting lines between related ideas. {STYLE_SUFFIX}"
    },
    {
        "filename": "pipeline_pattern.png",
        "prompt": f"{STYLE_PREFIX} Horizontal flow diagram with 5 stages as labeled containers connected by arrows: 'Trigger (Passive)' then 'Capture' then 'Process/Reason' then 'Produce Artifact' then 'Distribute'. Below: 3 example rows showing the pattern applied to internal tools, the product, and engineering practice. Labels: 'No manual trigger. No manual formatting. No manual distribution. Human stays in creative decision layer.' {STYLE_SUFFIX}"
    },
    {
        "filename": "experience_gap.png",
        "prompt": f"{STYLE_PREFIX} Two-world split diagram: LEFT 'Discovery' in grey, generic, search bar, plain text, labeled 'outside the brand' vs RIGHT 'Brand Experience' colorful, app-like, Disneyland castle gate entrance. Three labeled pillars on the brand side: 'More Actionable', 'Trust Signals', 'Meaningful Events'. Arrow from left to right showing user crossing the threshold. Callout: 'Context is the raw material for exceptional experience'. {STYLE_SUFFIX}"
    },
    {
        "filename": "speed_usage.png",
        "prompt": f"{STYLE_PREFIX} Dashboard-style diagram with a large speedometer gauge labeled 'Usage' as the central element. Around it: funnel diagram showing 'Usage then Value then Lighthouse Customer then Advocacy'. Side panel: 'Track weekly, not monthly'. Bottom callout: 'Are we moving fast enough?' and lighthouse icon for 'lighthouse customer goal'. {STYLE_SUFFIX}"
    },
    {
        "filename": "design_diff.png",
        "prompt": f"{STYLE_PREFIX} Before and after split diagram: LEFT 'Old Site' grey wireframe, plain, labeled 'functionally equivalent' vs RIGHT 'New Site' colorful, polished, labeled 'visually better'. Arrow between them labeled 'AI-Native Design Migration'. Callout boxes: 'Brand Guidelines Understanding', 'Creative Application', 'Output a designer would be proud of'. Bottom: 'Turn migration from cost conversation into value-add'. {STYLE_SUFFIX}"
    },
    {
        "filename": "tech_boundaries.png",
        "prompt": f"{STYLE_PREFIX} Three connected experiment stations labeled: 'I: Agent Endurance' with clock showing 1h to 4h to 8h with agent icon, 'J: Overnight Factory' with moon plus factory with conveyor belt of PRs, 'K: Tool Scouting' with magnifying glass over rotating tool icons. Shared infrastructure below them: timeline from 'Day' to 'Night' showing continuous operation. Label: 'Testing the limits of what is possible'. {STYLE_SUFFIX}"
    },
    {
        "filename": "culture_boundaries.png",
        "prompt": f"{STYLE_PREFIX} Four pillars or columns labeled: 'L: Permission to Experiment' with open door icon, 'M: Be Pirates' with skull flag, 'N: Parallel Innovation' with two parallel paths converging, 'O: Sustainable Fun' with smiling face plus rocket. Foundation block beneath all four: 'Explicit is greater than Implicit Permission'. Top banner: 'Director+ Sanctioned'. Callout: 'Silent duplication is waste. Visible duplication is evolution.' {STYLE_SUFFIX}"
    },
    {
        "filename": "new_eng_role.png",
        "prompt": f"{STYLE_PREFIX} Hierarchical org chart diagram: Top: 'Engineer' with person icon labeled 'Design, Plan, Judge'. Below: 'Orchestrator Agent' labeled 'Decompose, Assign, Coordinate'. Below that, branching to: 'Execution Agent A', 'Execution Agent B', 'Critic Agent'. Three evolution stages shown as timeline at bottom: 'Today: Engineer writes code' then 'Next: Engineer designs, AI codes' then 'Frontier: Engineer orchestrates agent team'. {STYLE_SUFFIX}"
    },
    {
        "filename": "cursor_pm.png",
        "prompt": f"{STYLE_PREFIX} Three-panel diagram: Panel 1 'Applied Research' with lab beaker plus code editor merged, text 'Research your own job, ship it as product'. Panel 2 'Team Recomposition' with left side 10 people one initiative, right side 4 crews of 2 spreading out, text 'Same headcount, 4X initiatives'. Panel 3 'Parallel Tasks' with single person with multiple task streams flowing in parallel, text 'Keep the fleet loaded'. Connected by 'Cursor PM Principles' banner. {STYLE_SUFFIX}"
    },
    {
        "filename": "boris_300prs.png",
        "prompt": f"{STYLE_PREFIX} Workstation cutaway diagram: 5 terminal windows plus 5 browser sessions equals '10-15 concurrent agents'. Flow: 'Plan Mode iterate until solid' then 'Execute with auto-accept' then 'Auto commit-push-PR' then '3 GitHub workflows to production'. Side labels: 'Quality: Opus plus thinking', 'Memory: shared CLAUDE.md', 'Verification loops'. Large counter: '300 PRs per December'. {STYLE_SUFFIX}"
    },
    {
        "filename": "ai_evolution.png",
        "prompt": f"{STYLE_PREFIX} Detailed matrix table diagram: 4 rows for Level 1 through 4, columns for 'Name', 'Description', 'Observable Signals', 'Where We Are'. Level transitions labeled on left side: '1 to 2: Frequency', '2 to 3: Structure', '3 to 4: Collective'. Right side callout: 'L3 to L4 Gap: Training problem vs Systems problem'. Bottom: four infrastructure elements for L4: 'Shared Tooling', 'Shared Norms', 'Shared Context', 'Shared Identity'. {STYLE_SUFFIX}"
    },
    {
        "filename": "pattern_cat4.png",
        "prompt": f"{STYLE_PREFIX} Five stacked horizontal layers forming a complete system: 'Technical' at top with agents plus parallelism, 'Cultural' with permission plus friction removal, 'Emotional' with fun plus sustainable plus safe, 'Skill Shift' with design plan verify, 'Organisational' at bottom with 1-2 person crews plus agents. Arrows connecting all layers showing interdependence. Center label: 'No single layer works alone. The 10X comes from all five.' {STYLE_SUFFIX}"
    },
    {
        "filename": "culture_pillars.png",
        "prompt": f"{STYLE_PREFIX} Nine columns or pillars diagram: first 5 in blue labeled 'Anthropic Pillars' with names AI-First, Push Boundaries, Write and Share, Fail Fast, Stay Skeptical. Last 4 in warm orange labeled 'Our Additions' with names Build for Team, Make Visible, Have Fun, Elevate Not Grind. Foundation: 'Individual Practice 1-5 plus Collective Practice 6-9 equals Level 4'. Each pillar has a small icon and one-line description. {STYLE_SUFFIX}"
    },
]


def generate_image(prompt, filename):
    """Call Imagen 4 API and save the resulting image."""
    output_path = os.path.join(OUTPUT_DIR, filename)

    if os.path.exists(output_path):
        print(f"  [SKIP] {filename} already exists")
        return True

    payload = {
        "instances": [{"prompt": prompt}],
        "parameters": {
            "sampleCount": 1,
            "aspectRatio": "16:9"
        }
    }

    data = json.dumps(payload).encode('utf-8')
    req = urllib.request.Request(
        API_URL,
        data=data,
        headers={'Content-Type': 'application/json'},
        method='POST'
    )

    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            result = json.loads(resp.read().decode('utf-8'))

        predictions = result.get('predictions', [])
        if not predictions:
            print(f"  [ERROR] No predictions returned for {filename}")
            return False

        image_b64 = predictions[0].get('bytesBase64Encoded')
        if not image_b64:
            print(f"  [ERROR] No image data for {filename}")
            return False

        with open(output_path, 'wb') as f:
            f.write(base64.b64decode(image_b64))

        print(f"  [OK] {filename} saved ({os.path.getsize(output_path)} bytes)")
        return True

    except urllib.error.HTTPError as e:
        body = e.read().decode('utf-8', errors='replace')
        print(f"  [ERROR] HTTP {e.code} for {filename}: {body[:300]}")
        return False
    except Exception as e:
        print(f"  [ERROR] {filename}: {e}")
        return False


def main():
    print(f"Generating {len(IMAGES)} infographic images with Imagen 4...")
    print(f"Output directory: {OUTPUT_DIR}")
    print(f"To regenerate all images, delete existing files first: rm {OUTPUT_DIR}/*.png\n")

    success = 0
    for i, img in enumerate(IMAGES, 1):
        print(f"[{i}/{len(IMAGES)}] {img['filename']}")
        if generate_image(img['prompt'], img['filename']):
            success += 1
        # Rate limiting: wait between requests
        if i < len(IMAGES):
            print("  Waiting 5s for rate limiting...")
            time.sleep(5)

    print(f"\nDone: {success}/{len(IMAGES)} images generated successfully.")


if __name__ == '__main__':
    main()
