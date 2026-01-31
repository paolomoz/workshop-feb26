#!/usr/bin/env python3
"""Build the workshop experience HTML -- storyline mode, section-based with hierarchical navigation."""

import argparse
import base64
import os
import json

IMAGES_DIR = os.path.join(os.path.dirname(__file__), 'images')
OUTPUT = os.path.join(os.path.dirname(__file__), 'workshop_experience.html')
TONE_CACHE = os.path.join(os.path.dirname(__file__), '.tone_cache.json')

parser = argparse.ArgumentParser(description="Build the workshop experience HTML")
parser.add_argument('--rewrite-tone', action='store_true',
                    help='Rewrite stale fields via Claude API, update cache, build')
parser.add_argument('--clear-tone-cache', action='store_true',
                    help='Delete cache and rebuild all tone from scratch')
args = parser.parse_args()

def load_image_b64(filename):
    path = os.path.join(IMAGES_DIR, filename)
    if not os.path.exists(path):
        return ""
    with open(path, 'rb') as f:
        data = base64.b64encode(f.read()).decode('ascii')
    return f"data:image/png;base64,{data}"

images = {
    "hero": load_image_b64("hero_header.png"),
    "10x_fun": load_image_b64("10x_fun.png"),
    "maturity_framework": load_image_b64("maturity_framework.png"),
    "be_pirates": load_image_b64("be_pirates.png"),
    "core_principle": load_image_b64("core_principle.png"),
    "prototype_ideas": load_image_b64("prototype_ideas.png"),
    "pipeline_pattern": load_image_b64("pipeline_pattern.png"),
    "experience_gap": load_image_b64("experience_gap.png"),
    "speed_usage": load_image_b64("speed_usage.png"),
    "design_diff": load_image_b64("design_diff.png"),
    "tech_boundaries": load_image_b64("tech_boundaries.png"),
    "culture_boundaries": load_image_b64("culture_boundaries.png"),
    "new_eng_role": load_image_b64("new_eng_role.png"),
    "cursor_pm": load_image_b64("cursor_pm.png"),
    "boris_300prs": load_image_b64("boris_300prs.png"),
    "ai_evolution": load_image_b64("ai_evolution.png"),
    "pattern_cat4": load_image_b64("pattern_cat4.png"),
    "culture_pillars": load_image_b64("culture_pillars.png"),
}

# ---------------------------------------------------------------------------
# Section data  (replaces the old flat cards list)
# ---------------------------------------------------------------------------
sections = [
    # ===================== Act 1 – Top Insights =====================
    {
        "id": "O", "title": "10X While Having Fun",
        "chip": "10X Fun",
        "act": 1, "category": 4, "image": "10x_fun", "top": True,
        "conviction": "STRONG",
        "tags": ["culture", "learning"],
        "summary": "The goal is elevation, not extraction. We\u2019re already ahead of industry and company averages. The next leap isn\u2019t more hours or pressure \u2014 it\u2019s fundamentally changing what humans spend energy on. Delegate the grind, keep the creative work, make it feel like play.",
        "details": [
            "Not more time or effort \u2014 <strong>different ways of doing things, or not doing them at all</strong>",
            "Everything we can delegate, we delegate \u2014 to AI, to automation, to systems",
            "Psychological safety is non-negotiable: no danger of \u2018doing the wrong thing\u2019 when experimenting",
            "The energy has to be sustainable \u2014 this is a permanent shift, not a sprint"
        ],
        "why": "Every other idea in this document could be read as \u2018do more.\u2019 This reframes the entire agenda: <strong>delegate more, think higher, enjoy the ride.</strong> If the team feels burned by this transformation, it failed \u2014 regardless of output.",
        "connections": ["M", "L", "J", "S"],
        "sub_items": []
    },
    {
        "id": "W", "title": "AI Evolution Framework: 4 Levels",
        "chip": "AI Framework",
        "act": 1, "category": 4, "image": "maturity_framework", "top": True,
        "conviction": "DOING",
        "tags": ["culture", "learning", "process"],
        "summary": "The maturity model that makes everything measurable. Level 1 (AI User) \u2192 Level 2 (AI First) \u2192 Level 3 (AI Native Individual) \u2192 Level 4 (AI Native Team). Most of the team is at Level 1. Target: everyone at Level 3, team at Level 4.",
        "details": [
            "<strong>Level 1 \u2192 2:</strong> Frequency. AI goes from \u2018sometimes\u2019 to \u2018default first action\u2019",
            "<strong>Level 2 \u2192 3:</strong> Structure. Workflows rebuilt around AI, not AI bolted onto old workflows",
            "<strong>Level 3 \u2192 4:</strong> Collective. Shared infrastructure, norms, and culture make the team more than the sum of AI-native individuals",
            "Level 4 is not \u2018everyone is Level 3.\u2019 It\u2019s shared infrastructure and culture that makes AI-native the default, even for new joiners"
        ],
        "why": "This framework is the backbone for assessing progress and mapping every workshop exercise to a level transition. It turns vague ambition into measurable targets.",
        "connections": ["S", "X", "O", "U", "T"],
        "attribution": "Alex Koren (Anthropic)",
        "sub_items": []
    },
    {
        "id": "M", "title": "Be Pirates",
        "chip": "Be Pirates",
        "act": 1, "category": 4, "image": "be_pirates", "top": True,
        "conviction": "STRONG",
        "tags": ["culture"],
        "summary": "Break the rules. Use what you need. Expense the tools. Explicitly sanctioned at director+ level. This is the cultural unlock that makes everything else possible \u2014 without this permission, every other idea hits a friction wall.",
        "details": [
            "Use the education fund to expense subscriptions to tools that make you faster",
            "Don\u2019t ask for a procurement cycle \u2014 just do it",
            "Explicitly sanctioned across the organisation at the workshop level",
            "Removes the #1 blocker to experimentation: fear of getting in trouble"
        ],
        "why": "Most \u2018innovation culture\u2019 initiatives fail because the permission is implicit. This one is explicit, named, and endorsed by directors+. \u2018Be pirates\u2019 is a cultural licence that changes everything.",
        "connections": ["K", "L", "N", "O", "X"],
        "sub_items": []
    },

    # ===================== Act 2 – What We'll Build =====================
    {
        "id": "CORE", "title": "Core Principle: Automate Everything",
        "chip": "Core Principle",
        "act": 2, "category": 1, "image": "core_principle",
        "conviction": "STRONG",
        "tags": ["automation", "culture"],
        "summary": "If a task can be delegated to AI, invest time to build it and share it as a working tool with the team. The crazier the idea the better. Implementation should be simple \u2014 low effort, high leverage. Must be usable by everyone.",
        "connections": ["A", "B", "C", "D", "E", "F", "G", "H"],
        "sub_items": []
    },
    {
        "id": "PROTO_IDEAS", "title": "Prototype Ideas",
        "chip": "Prototypes",
        "act": 2, "category": 1, "image": "prototype_ideas",
        "sub_items": [
            {
                "id": "A", "title": "Ambient Screen Buddy",
                "conviction": "EXPLORING",
                "tags": ["automation", "tooling", "learning"],
                "summary": "An always-on assistant that screenshots the user\u2019s screen every few seconds, silently reasons about what the user is doing, accumulates learnings over time, and proactively suggests faster ways or offers to automate entirely.",
                "connections": ["H", "E"]
            },
            {
                "id": "B", "title": "Zero-Touch Meeting Pipeline",
                "conviction": "EXPLORING",
                "tags": ["automation", "customer", "process"],
                "summary": "Meeting ends, no manual action required. Transcript is generated, fed into shared context, then distilled into key learnings, data points, and candidate next actions. Eliminates the \u2018meeting notes tax.\u2019",
                "connections": ["P", "D", "G", "Q2"]
            },
            {
                "id": "C", "title": "Auto-Demo Generator for POCs",
                "conviction": "EXPLORING",
                "tags": ["automation", "visibility", "tooling"],
                "summary": "Someone works on a POC. The system analyses the code, generates a summary, writes a demo script, records a screen walkthrough, produces a voiceover, and posts a 1-minute demo to Slack. Zero manual effort.",
                "connections": ["L", "G", "F"]
            },
            {
                "id": "D", "title": "Feedback-to-Fix Pipeline",
                "conviction": "EXPLORING",
                "tags": ["automation", "customer", "process"],
                "summary": "User feedback from Slack channels is continuously ingested, compacted into structured data, classified as fix or idea, then the system opens a branch, generates the PR, and messages the right person to review.",
                "connections": ["B", "Q", "E"]
            },
            {
                "id": "E", "title": "Self-Improving Feedback Loop",
                "conviction": "EXPLORING",
                "tags": ["automation", "learning"],
                "summary": "Each tool reports back on whether its output was useful. Was the suggestion acted on? Was the PR merged? Was the demo shared? This signal feeds back so systems learn what\u2019s valuable and stop producing noise.",
                "connections": ["A", "D", "J", "H"]
            },
            {
                "id": "F", "title": "Shared Automation Library (The Cookbook)",
                "conviction": "EXPLORING",
                "tags": ["tooling", "culture", "visibility"],
                "summary": "Every automation a team member builds gets published to an internal catalog with: what it does, how to trigger it, and a 30-second video. Turns \u2018I built a cool thing\u2019 into \u2018everyone uses it by Monday.\u2019",
                "connections": ["T", "H", "K", "L", "W"]
            },
            {
                "id": "G", "title": "AI Standup / Async Status Harvester",
                "conviction": "EXPLORING",
                "tags": ["automation", "process", "visibility"],
                "summary": "Instead of people writing status updates, the system pulls signals from Git, PRs, Slack, and tickets. It composes per-person and per-team summaries daily. Humans review and annotate only if something is wrong.",
                "connections": ["B", "C", "U", "Q"]
            },
            {
                "id": "H", "title": "Prompt & Workflow Shadowing",
                "conviction": "EXPLORING",
                "tags": ["learning", "culture", "automation"],
                "summary": "When someone finds an effective AI workflow, the system captures it and proposes it to others in similar contexts. The team\u2019s collective AI skill rises automatically.",
                "connections": ["A", "K", "F"]
            },
        ]
    },
    {
        "id": "PIPELINE", "title": "The Universal Pipeline Pattern",
        "chip": "Pipeline",
        "act": 2, "category": 1, "image": "pipeline_pattern",
        "conviction": "STRONG",
        "tags": ["automation", "process"],
        "summary": "All ideas share the same architecture: Trigger (passive) \u2192 Capture \u2192 Process/Reason \u2192 Produce Artifact \u2192 Distribute. No manual trigger, no manual formatting, no manual distribution. The human stays in the creative/decision layer.",
        "connections": ["B", "C", "D", "G", "J"],
        "sub_items": []
    },

    # ===================== Act 3 – The Product Bet =====================
    {
        "id": "EXP_GAP", "title": "The Experience Gap",
        "chip": "Experience Gap",
        "act": 3, "category": 2, "image": "experience_gap",
        "sub_items": [
            {
                "id": "P", "title": "Disneylandification of Brand Experience",
                "conviction": "STRONG",
                "tags": ["product", "customer"],
                "summary": "Two worlds: discovery (outside the brand) and brand experience (inside). The brand experience must delight like Disneyland, not feel like a search bar. More actionable, trust signals, meaningful events.",
                "details": [
                    "<strong>More actionable</strong> \u2014 the brand experience should feel like an app, not a brochure",
                    "<strong>Trust signals</strong> \u2014 context-aware proof points that matter to this user at this moment",
                    "<strong>Meaningful events</strong> \u2014 track events useful to build context. Context is the raw material for exceptional experience"
                ],
                "connections": ["B", "D", "O", "R"],
                "attribution": "Loni"
            }
        ]
    },
    {
        "id": "SPEED_USAGE", "title": "Speed & Usage as North Star",
        "chip": "Speed & Usage",
        "act": 3, "category": 2, "image": "speed_usage",
        "sub_items": [
            {
                "id": "Q", "title": "Are We Moving Fast Enough?",
                "conviction": "STRONG",
                "tags": ["product", "process"],
                "summary": "We are doing the right things. The question is speed. The first key objective is usage: track it and maximise it everywhere. Usage is the leading indicator of value, adoption, and retention. If people aren\u2019t using it, nothing else matters.",
                "connections": ["D", "G", "Q2"],
                "attribution": "Amit (Product SVP)"
            },
            {
                "id": "Q2", "title": "The Lighthouse Customer",
                "conviction": "STRONG",
                "tags": ["product", "customer"],
                "summary": "Key goal: have a customer who says \u2018I embarked with Adobe on this agentic evolution, and this is the value I\u2019m getting.\u2019 Not a marketing case study \u2014 a customer who believes it and says it unprompted.",
                "connections": ["Q", "B"],
                "attribution": "Amit (Product SVP)"
            }
        ]
    },
    {
        "id": "DESIGN_DIFF", "title": "Design as Differentiator",
        "chip": "Design",
        "act": 3, "category": 2, "image": "design_diff",
        "sub_items": [
            {
                "id": "R", "title": "Beautiful Design as Migration Lever",
                "conviction": "EXPLORING",
                "tags": ["product", "customer"],
                "summary": "When customers migrate to AEM, what if the output is visually better? Turn migration from a cost conversation into value-add: \u2018Your old site worked. Your new site is beautiful.\u2019 AI-native design that understands brand guidelines.",
                "connections": ["P", "K", "Q2"]
            }
        ]
    },

    # ===================== Act 4 – Becoming Frontier Engineers =====================
    {
        "id": "TECH_BOUNDS", "title": "Technical Boundaries to Explore",
        "chip": "Technical",
        "act": 4, "category": 4, "image": "tech_boundaries",
        "sub_items": [
            {
                "id": "I", "title": "Long-Running Autonomous Agents",
                "conviction": "EXPLORING",
                "tags": ["tooling", "automation"],
                "summary": "How long can we sustain a single agent session? Can we hand an agent a task that takes hours \u2014 or an entire workday? Testing the limits of agent endurance: context management, error recovery, self-correction over extended runs.",
                "connections": ["C", "S", "J", "V"]
            },
            {
                "id": "J", "title": "Overnight Idea Factory",
                "conviction": "STRONG",
                "tags": ["automation", "process", "learning"],
                "summary": "The system generates ideas automatically, implements them overnight. Multiple agents try different approaches, criticise each other\u2019s results, elect winners. Engineer arrives to ranked, working prototypes. Sleep becomes productive time.",
                "details": [
                    "A team of 10 engineers effectively becomes 10 engineers + N overnight agents",
                    "The number of experiments the team can run increases <strong>100X</strong>",
                    "The trigger is \u2018end of workday.\u2019 The artifact is working code."
                ],
                "connections": ["E", "N", "PIPELINE", "I", "V"]
            },
            {
                "id": "K", "title": "Continuous AI Tool Scouting",
                "conviction": "STRONG",
                "tags": ["tooling", "learning"],
                "summary": "Experiment with AI tools continuously \u2014 not as a one-off evaluation, but as an ongoing practice. Discover new capabilities that inspire ideas, and find tools that make existing ideas faster to implement.",
                "connections": ["H", "F", "R", "M"]
            }
        ]
    },
    {
        "id": "CULTURE_BOUNDS", "title": "Cultural Boundaries to Break",
        "chip": "Cultural",
        "act": 4, "category": 4, "image": "culture_boundaries",
        "sub_items": [
            {
                "id": "L", "title": "Permission to Experiment Freely",
                "conviction": "STRONG",
                "tags": ["culture", "learning"],
                "summary": "Everyone has explicit permission to spend time on whatever experiment they have in mind \u2014 even personal ideas. The only obligation: report back what you learned. With Auto-Demo (C), even that is automated.",
                "connections": ["C", "M", "O", "F"]
            },
            {
                "id": "M_CAT4", "title": "\u201cBe Pirates\u201d",
                "conviction": "STRONG",
                "tags": ["culture"],
                "summary": "Break the rules. Use what you need. Leverage the education fund to expense subscriptions to tools that make you faster. Don\u2019t ask for a procurement cycle \u2014 just do it. Explicitly sanctioned across the organisation at the workshop level.",
                "details": [
                    "Use the education fund to expense subscriptions to tools that make you faster",
                    "Don\u2019t ask for a procurement cycle \u2014 just do it",
                    "Explicitly sanctioned across the organisation at the workshop level",
                    "Removes the #1 blocker to experimentation: fear of getting in trouble"
                ],
                "connections": ["K", "L", "N", "O", "X"]
            },
            {
                "id": "N", "title": "Parallel Innovation & Competition",
                "conviction": "STRONG",
                "tags": ["culture", "process"],
                "summary": "Different teams may build similar things in parallel \u2014 and that\u2019s not waste, it\u2019s expected. Embrace competition, share continuously, finalise milestones, continuously innovate. The winning version emerges from competition, not committee.",
                "details": [
                    "<strong>Case study:</strong> Alex Koren\u2019s team at Anthropic was working on something similar to Cowork. Then Cowork was built and shipped in 10 days over Christmas.",
                    "The parallel work wasn\u2019t lost \u2014 it was part of the exploration that made the winner possible.",
                    "Silent duplication is waste. <strong>Visible duplication is evolution.</strong>"
                ],
                "connections": ["J", "L", "M", "F", "G"]
            },
            {
                "id": "O_CAT4", "title": "Sustainable Intensity: 10X While Having Fun",
                "conviction": "STRONG",
                "tags": ["culture", "learning"],
                "summary": "We are already outperforming the industry and the company average. The next leap isn\u2019t about adding hours or pressure \u2014 it\u2019s about fundamentally changing what humans spend their energy on. Delegate the grind. Keep the creative, strategic, high-judgment work.",
                "details": [
                    "<strong>Challenge what we do</strong> \u2014 question every task. Can it be done differently? Can it be eliminated? Can an agent do it?",
                    "<strong>Psychological safety</strong> \u2014 experimenting with new ways of working can\u2019t carry the risk of \u2018doing the wrong thing.\u2019",
                    "<strong>Sustainable energy</strong> \u2014 this isn\u2019t a hack week. It\u2019s a permanent operating model. If it drains people, it\u2019s broken."
                ],
                "connections": ["M", "L"]
            }
        ]
    },
    {
        "id": "NEW_ENG_ROLE", "title": "The New Engineering Role",
        "chip": "New Role",
        "act": 4, "category": 4, "image": "new_eng_role",
        "sub_items": [
            {
                "id": "S", "title": "Engineers as Managers of Agents",
                "conviction": "STRONG",
                "tags": ["culture", "process", "learning"],
                "summary": "The frontier engineer\u2019s job shifts upward. More design, plan, verify. Less coding \u2014 potentially zero. The engineer becomes a manager of agents. This is a harder job, not an easier one.",
                "details": [
                    "<strong>Today:</strong> Engineer writes code, AI assists",
                    "<strong>Next:</strong> Engineer designs and plans, AI writes code, engineer verifies",
                    "<strong>Frontier:</strong> Engineer orchestrates a team of agents \u2014 orchestrator decomposes, execution agents implement, engineer reviews and steers"
                ],
                "connections": ["I", "J", "O", "W", "X", "V"]
            }
        ]
    },
    {
        "id": "CURSOR_PM", "title": "Insights from Cursor PM",
        "chip": "Cursor PM",
        "act": 4, "category": 4, "image": "cursor_pm",
        "sub_items": [
            {
                "id": "T", "title": "Applied Research Team Identity",
                "conviction": "STRONG",
                "tags": ["culture", "process", "learning"],
                "summary": "Cursor sees themselves as an applied research team: research how to improve your own job, then ship the results as product. Every workflow improvement is a candidate for the product. Dogfooding is the core R&D methodology.",
                "connections": ["F", "W"],
                "attribution": "Cursor PM"
            },
            {
                "id": "U", "title": "Team Recomposition: Cover More Ground",
                "conviction": "STRONG",
                "tags": ["process", "culture"],
                "summary": "Same headcount, radically different topology. Instead of 10 people on one initiative, the team fans out into 1-2 person crews, each covering an independent track. PM and Design float across, providing direction \u2014 not managing tickets.",
                "details": [
                    "<strong>Before:</strong> 1 PM + 1 Design + 8 SWEs = 10 people, one initiative",
                    "<strong>After:</strong> 1 PM + 1 Design + 4 crews of 2 SWEs = same people, 4x the initiatives",
                    "Managers and PMs evolve from coordination to <strong>strategy, direction-setting, and quality judgment</strong>"
                ],
                "connections": ["S", "G", "F", "N", "V", "W"],
                "attribution": "Cursor PM"
            },
            {
                "id": "V", "title": "Short, Frequent, Parallel Tasks",
                "conviction": "STRONG",
                "tags": ["process", "automation", "tooling"],
                "summary": "Each engineer runs many short tasks in parallel instead of one long task sequentially. Each task is delegated to an agent. The engineer\u2019s job: keep the fleet loaded \u2014 define the next task before the current one finishes. Parallelism at every layer.",
                "connections": ["X", "U", "J", "I", "S"],
                "attribution": "Cursor PM"
            }
        ]
    },
    {
        "id": "BORIS_CASE", "title": "Case Study: Boris Cherny",
        "chip": "Boris Case",
        "act": 4, "category": 4, "image": "boris_300prs",
        "sub_items": [
            {
                "id": "X", "title": "Boris Cherny: 300 PRs in December",
                "conviction": "STRONG",
                "tags": ["tooling", "automation", "learning"],
                "summary": "Boris shipped >300 PRs in December without long hours. 5 Claude Code terminals + 5-10 browser sessions. Plan-first discipline, blanket bash permissions, auto-ship pipeline. The reference implementation for Level 3.",
                "details": [
                    "<strong>10-15 concurrent agents</strong> running in parallel",
                    "<strong>Plan-first for every session:</strong> iterate until the plan is solid, then execute with auto-accept",
                    "<strong>Quality over speed:</strong> Uses Opus with thinking enabled \u2014 reduces the \u2018correction tax\u2019",
                    "<strong>Systems thinking:</strong> \u2018How do I build a system where AI reliably produces what I need?\u2019"
                ],
                "connections": ["W", "V", "S", "J", "M"],
                "attribution": "Boris Cherny (Anthropic)"
            }
        ]
    },
    {
        "id": "AI_EVOLUTION", "title": "AI Evolution Framework",
        "chip": "AI Evolution",
        "act": 4, "category": 4, "image": "ai_evolution",
        "sub_items": [
            {
                "id": "W_CAT4", "title": "The Four Levels of AI Maturity",
                "conviction": "DOING",
                "tags": ["culture", "learning", "process"],
                "summary": "Shared by Alex Koren. A framework to assess where individuals and teams sit on the AI adoption curve. Level 1 (AI User) \u2192 Level 2 (AI First) \u2192 Level 3 (AI Native Individual) \u2192 Level 4 (AI Native Team).",
                "details": [
                    "<strong>Level 1 \u2192 2: Frequency.</strong> AI goes from \u2018sometimes\u2019 to \u2018default first action\u2019",
                    "<strong>Level 2 \u2192 3: Structure.</strong> Workflows rebuilt around AI, not AI bolted onto old workflows",
                    "<strong>Level 3 \u2192 4: Collective.</strong> Shared infrastructure, norms, and culture",
                    "<strong>The L3\u21924 Gap:</strong> Getting individuals to Level 3 is a training problem. Getting the team to Level 4 is a <strong>systems problem</strong> requiring shared tooling, norms, context, and identity"
                ],
                "connections": ["S", "X", "O", "U", "T"],
                "attribution": "Alex Koren (Anthropic)"
            }
        ]
    },
    {
        "id": "PATTERN_C4", "title": "Pattern Across Category 4",
        "chip": "Pattern",
        "act": 4, "category": 4, "image": "pattern_cat4",
        "conviction": "STRONG",
        "tags": ["culture", "process", "automation"],
        "summary": "Five layers of transformation, none of which works alone. The 10X (or 100X) comes from all five working together.",
        "details": [
            "<strong>Technical:</strong> Push agent duration + parallelism \u2192 multiply experiment throughput 100X",
            "<strong>Cultural:</strong> Give explicit permission + remove friction \u2192 multiply willingness to try",
            "<strong>Emotional:</strong> Make it fun + sustainable + safe \u2192 multiply longevity of the transformation",
            "<strong>Skill shift:</strong> Train engineers to design/plan/verify instead of code \u2192 unlock the agent workforce",
            "<strong>Organisational:</strong> Shrink teams to 1-2 person crews + agents \u2192 remove coordination overhead"
        ],
        "why": "No single layer works alone. Agents without permission = shelfware. Permission without agents = slow ambition. Either without fun = burnout. Agents without skilled managers = chaos. Small crews without visibility = silos.",
        "connections": [],
        "sub_items": []
    },

    # ===================== Act 5 – Culture & Close =====================
    {
        "id": "CULTURE", "title": "Team Culture Model: 9 Pillars",
        "chip": "Culture Model",
        "act": 5, "category": 3, "image": "culture_pillars",
        "conviction": "DOING",
        "tags": ["culture", "feb9"],
        "summary": "Anthropic\u2019s 5 pillars (AI-First, Push Boundaries, Write & Share, Fail Fast, Stay Skeptical) plus 4 additions for the team level: Build for the Team, Make It Visible, Have Fun Doing It, Elevate Don\u2019t Grind.",
        "details": [
            "<strong>1. AI-First</strong> \u2014 Try to answer your own questions first",
            "<strong>2. Push Boundaries</strong> \u2014 Every task is an opportunity to use AI",
            "<strong>3. Write & Share</strong> \u2014 When you learn something, share it",
            "<strong>4. Fail Fast</strong> \u2014 It won\u2019t all work, but it\u2019s worth a try",
            "<strong>5. Stay Skeptical</strong> \u2014 Challenge AI to ensure the best outputs",
            "<strong>6. Build for the Team</strong> \u2014 When you automate, package it for others",
            "<strong>7. Make It Visible</strong> \u2014 Visibility should be opt-out, not opt-in",
            "<strong>8. Have Fun Doing It</strong> \u2014 The transformation should feel like play",
            "<strong>9. Elevate, Don\u2019t Grind</strong> \u2014 Delegate everything you can"
        ],
        "connections": ["W", "O", "M", "F"],
        "attribution": "Anthropic + Team Additions",
        "sub_items": []
    },
    {
        "id": "ROUNDTABLE", "title": "Two Sentences That Matter",
        "chip": "Roundtable",
        "act": 5, "category": 3,
        "conviction": "DOING",
        "tags": ["culture", "learning", "feb9"],
        "summary": "Every person shares exactly two sentences: (1) \u2018My next-level focus\u2019 \u2014 what to focus on to reach the next level of AI fluency. (2) \u2018My stretch goal\u2019 \u2014 what to have done by end of year. Must be a stretch \u2014 if it doesn\u2019t scare you a little, aim higher.",
        "connections": ["O", "Q2", "E", "C", "W"],
        "sub_items": []
    },
]

# ---------------------------------------------------------------------------
# Supporting data structures
# ---------------------------------------------------------------------------
STORY_ORDER = [
    "O", "W", "M",
    "CORE", "PROTO_IDEAS", "PIPELINE",
    "EXP_GAP", "SPEED_USAGE", "DESIGN_DIFF",
    "TECH_BOUNDS", "CULTURE_BOUNDS", "NEW_ENG_ROLE",
    "CURSOR_PM", "BORIS_CASE", "AI_EVOLUTION", "PATTERN_C4",
    "CULTURE", "ROUNDTABLE",
]

ACT_LABELS = {
    "O": "Act 1 \u2014 The Emotional Contract",
    "CORE": "Act 2 \u2014 What We\u2019ll Build",
    "EXP_GAP": "Act 3 \u2014 The Product Bet",
    "TECH_BOUNDS": "Act 4 \u2014 Becoming Frontier Engineers",
    "CULTURE": "Act 5 \u2014 Culture & Close",
}

ACTS = {
    1: {"name": "Act 1", "subtitle": "Top Insights"},
    2: {"name": "Act 2", "subtitle": "10X Faster"},
    3: {"name": "Act 3", "subtitle": "Product Vision"},
    4: {"name": "Act 4", "subtitle": "Frontier Engineers"},
    5: {"name": "Act 5", "subtitle": "Culture & Close"},
}

CARD_TO_SECTION = {
    "A": "PROTO_IDEAS", "B": "PROTO_IDEAS", "C": "PROTO_IDEAS", "D": "PROTO_IDEAS",
    "E": "PROTO_IDEAS", "F": "PROTO_IDEAS", "G": "PROTO_IDEAS", "H": "PROTO_IDEAS",
    "P": "EXP_GAP", "Q": "SPEED_USAGE", "Q2": "SPEED_USAGE", "R": "DESIGN_DIFF",
    "I": "TECH_BOUNDS", "J": "TECH_BOUNDS", "K": "TECH_BOUNDS",
    "L": "CULTURE_BOUNDS", "N": "CULTURE_BOUNDS",
    "S": "NEW_ENG_ROLE",
    "T": "CURSOR_PM", "U": "CURSOR_PM", "V": "CURSOR_PM",
    "X": "BORIS_CASE",
    "O": "O", "W": "W", "M": "M",
    "CORE": "CORE", "PIPELINE": "PIPELINE",
    "PROTO_IDEAS": "PROTO_IDEAS",
    "EXP_GAP": "EXP_GAP", "SPEED_USAGE": "SPEED_USAGE", "DESIGN_DIFF": "DESIGN_DIFF",
    "TECH_BOUNDS": "TECH_BOUNDS", "CULTURE_BOUNDS": "CULTURE_BOUNDS",
    "NEW_ENG_ROLE": "NEW_ENG_ROLE", "CURSOR_PM": "CURSOR_PM",
    "BORIS_CASE": "BORIS_CASE", "AI_EVOLUTION": "AI_EVOLUTION",
    "PATTERN_C4": "PATTERN_C4",
    "CULTURE": "CULTURE", "ROUNDTABLE": "ROUNDTABLE",
    "M_CAT4": "CULTURE_BOUNDS", "O_CAT4": "CULTURE_BOUNDS",
    "W_CAT4": "AI_EVOLUTION",
}

categories = {
    1: {"name": "10X Faster", "color": "#3b82f6"},
    2: {"name": "Product Vision", "color": "#8b5cf6"},
    3: {"name": "Workshop", "color": "#f59e0b"},
    4: {"name": "Frontier", "color": "#ef4444"},
}

# ---------------------------------------------------------------------------
# Hero & Synthesis text  (extracted for tone rewriting at build time)
# ---------------------------------------------------------------------------
HERO_SUB = "Interactive exploration of the ideas, culture shifts, and technical boundaries discussed at the workshop \u2014 through the lens of transforming our team to become 10X faster with AI."

HERO_QUOTE = "Become an AI Native Team (Level 4) by giving engineers explicit permission to break rules, restructuring work around parallel agent fleets, and building shared infrastructure that makes the AI-native way the default \u2014 while keeping it fun."

SYNTH_BLOCKS = [
    {
        "heading": "1. The goal is elevation, not extraction.",
        "body": (
            "Every idea \u2014 agents, pipelines, overnight factories \u2014 could be misread "
            "as \u201cwork more.\u201d The real message: <strong>delegate more, think higher, "
            "enjoy it.</strong> Engineers become managers of agent fleets. The job gets harder "
            "and more interesting, not busier. If the transformation feels like burnout, it failed."
        ),
    },
    {
        "heading": "2. We have a maturity framework and a concrete target.",
        "body": (
            "Level 1 (AI User) \u2192 Level 2 (AI First) \u2192 Level 3 (AI Native Individual) "
            "\u2192 Level 4 (AI Native Team). Boris Cherny\u2019s 300 PRs/month shows Level 3 "
            "in practice. <strong>Target: every individual at Level 3, the team at Level 4.</strong> "
            "Level 3 is a training problem. Level 4 is a systems problem."
        ),
    },
    {
        "heading": "3. The cultural unlock is already granted: \u201cBe Pirates.\u201d",
        "body": (
            "Explicitly sanctioned at director+ level. Break rules, expense tools, experiment "
            "freely, fail fast. Combined with the \u201capplied research team\u201d identity and "
            "9 culture pillars, the team has a <strong>complete cultural model</strong> to adopt."
        ),
    },
    {
        "heading": "The Universal Pipeline",
        "pipeline": "Passive Trigger \u2192 Capture \u2192 AI Processing \u2192 Artifact \u2192 Auto-Distribute",
        "body": (
            "This pattern applies to internal tools (A-H), the product (P, R), and engineering "
            "practice (I, J, V, X). The team that builds these pipelines internally IS the applied "
            "research team that informs the product."
        ),
    },
    {
        "heading": "Five Layers of Transformation",
        "body": (
            "<strong>Technical:</strong> Push agent duration + parallelism \u2192 100X experiment throughput<br>"
            "<strong>Cultural:</strong> Explicit permission + remove friction \u2192 multiply willingness<br>"
            "<strong>Emotional:</strong> Fun + sustainable + safe \u2192 multiply longevity<br>"
            "<strong>Skill shift:</strong> Design/plan/verify instead of code \u2192 unlock the agent workforce<br>"
            "<strong>Organisational:</strong> 1-2 person crews + agents \u2192 remove coordination overhead<br><br>"
            "No single layer works alone. <strong>The 10X (or 100X) comes from all five.</strong>"
        ),
    },
]

# Build image map for sections
image_map = {}
for sec in sections:
    img_key = sec.get("image")
    if img_key:
        image_map[sec["id"]] = images.get(img_key, "")

# ---------------------------------------------------------------------------
# Tone rewriting  (optional, via CLI flags)
# ---------------------------------------------------------------------------
if args.rewrite_tone or args.clear_tone_cache:
    from tone_rewriter import rewrite_all
    sections, HERO_SUB, HERO_QUOTE, SYNTH_BLOCKS = rewrite_all(
        sections, HERO_SUB, HERO_QUOTE, SYNTH_BLOCKS,
        clear_cache=args.clear_tone_cache)
elif os.path.exists(TONE_CACHE):
    from tone_rewriter import apply_cached
    sections, HERO_SUB, HERO_QUOTE, SYNTH_BLOCKS = apply_cached(
        sections, HERO_SUB, HERO_QUOTE, SYNTH_BLOCKS)

sections_json = json.dumps(sections)
image_map_json = json.dumps(image_map)
story_order_json = json.dumps(STORY_ORDER)
act_labels_json = json.dumps(ACT_LABELS)
acts_json = json.dumps(ACTS)
card_to_section_json = json.dumps(CARD_TO_SECTION)
categories_json = json.dumps(categories)
hero_image = images.get("hero", "")

# Build synthesis slide HTML from SYNTH_BLOCKS
def _synth_block_html(b):
    pipeline = f'        <div class="synth-pipeline">{b["pipeline"]}</div>\n' if b.get("pipeline") else ''
    return (
        f'      <div class="synth-block">\n'
        f'        <h3>{b["heading"]}</h3>\n'
        f'{pipeline}'
        f'        <p>{b["body"]}</p>\n'
        f'      </div>'
    )

synth_blocks_html = '\n\n'.join(_synth_block_html(b) for b in SYNTH_BLOCKS)

html = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>One AEM Workshop \u2014 Interactive Experience</title>
<style>
*, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}

:root {{
  --bg: #0a0a0f;
  --surface: #14141e;
  --surface-alt: #1a1a28;
  --border: #2a2a3a;
  --text: #e8e8f0;
  --text-secondary: #9898b0;
  --text-dim: #585870;
  --accent-blue: #3b82f6;
  --accent-purple: #8b5cf6;
  --accent-orange: #f59e0b;
  --accent-red: #ef4444;
  --accent-green: #059669;
  --accent-cyan: #06b6d4;
  --radius: 20px;
  --radius-sm: 10px;
}}

html, body {{ height: 100%; overflow: hidden; }}

body {{
  font-family: -apple-system, BlinkMacSystemFont, 'SF Pro Display', 'Segoe UI', system-ui, sans-serif;
  background: var(--bg);
  color: var(--text);
  line-height: 1.6;
}}

/* ===== SLIDE CONTAINER ===== */
#app {{
  height: 100vh;
  display: flex;
  flex-direction: column;
}}

/* --- Top bar --- */
.top-bar {{
  flex-shrink: 0;
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 10px 24px;
  background: rgba(10,10,15,0.9);
  backdrop-filter: blur(16px);
  border-bottom: 1px solid var(--border);
  z-index: 10;
}}

.top-bar-title {{
  font-size: 13px;
  font-weight: 600;
  color: var(--text-secondary);
  letter-spacing: 0.5px;
  white-space: nowrap;
}}

.progress-track {{
  flex: 1;
  height: 3px;
  background: var(--border);
  border-radius: 2px;
  overflow: hidden;
  min-width: 80px;
}}

.progress-fill {{
  height: 100%;
  background: linear-gradient(90deg, var(--accent-blue), var(--accent-purple));
  border-radius: 2px;
  transition: width 0.4s ease;
}}

.progress-label {{
  font-size: 12px;
  color: var(--text-dim);
  white-space: nowrap;
  font-variant-numeric: tabular-nums;
}}

.overview-btn {{
  padding: 6px 14px;
  background: var(--surface-alt);
  border: 1px solid var(--border);
  border-radius: 6px;
  color: var(--text-secondary);
  font-size: 12px;
  cursor: pointer;
  white-space: nowrap;
  transition: all 0.2s;
}}

.overview-btn:hover {{
  background: var(--border);
  color: var(--text);
}}

/* --- Breadcrumb bar (NEW) --- */
.breadcrumb-bar {{
  flex-shrink: 0;
  display: none;
  align-items: center;
  gap: 0;
  padding: 8px 24px 4px;
  background: rgba(10,10,15,0.85);
  backdrop-filter: blur(12px);
  font-size: 12px;
  z-index: 9;
}}

.breadcrumb-bar.visible {{
  display: flex;
}}

.bc-act {{
  color: var(--accent-orange);
  font-weight: 600;
  cursor: pointer;
  transition: color 0.15s;
}}
.bc-act:hover {{ color: #fbbf24; }}

.bc-sep {{
  color: var(--text-dim);
  margin: 0 8px;
  font-size: 11px;
}}

.bc-category {{
  color: var(--text-secondary);
  font-weight: 500;
}}

.bc-section {{
  color: var(--text);
  font-weight: 600;
}}

/* --- Section nav strip (NEW) --- */
.section-nav {{
  flex-shrink: 0;
  display: none;
  gap: 6px;
  padding: 4px 24px 8px;
  background: rgba(10,10,15,0.85);
  backdrop-filter: blur(12px);
  border-bottom: 1px solid var(--border);
  overflow-x: auto;
  scrollbar-width: none;
  z-index: 9;
}}

.section-nav.visible {{
  display: flex;
}}

.section-nav::-webkit-scrollbar {{ display: none; }}

.sec-chip {{
  flex-shrink: 0;
  padding: 4px 12px;
  background: var(--surface-alt);
  border: 1px solid var(--border);
  border-radius: 14px;
  font-size: 11px;
  font-weight: 500;
  color: var(--text-dim);
  cursor: pointer;
  transition: all 0.15s;
  white-space: nowrap;
}}

.sec-chip:hover {{
  background: var(--border);
  color: var(--text-secondary);
}}

.sec-chip.active {{
  background: rgba(59,130,246,0.15);
  border-color: rgba(59,130,246,0.35);
  color: var(--accent-blue);
  font-weight: 600;
}}

/* --- Slide area --- */
.slide-area {{
  flex: 1;
  position: relative;
  overflow: hidden;
}}

/* Each slide */
.slide {{
  position: absolute;
  inset: 0;
  display: flex;
  opacity: 0;
  pointer-events: none;
  transition: opacity 0.35s ease, transform 0.35s ease;
  transform: translateX(40px);
  overflow-y: auto;
  scrollbar-width: thin;
  scrollbar-color: var(--border) transparent;
}}

.slide::-webkit-scrollbar {{ width: 6px; }}
.slide::-webkit-scrollbar-track {{ background: transparent; }}
.slide::-webkit-scrollbar-thumb {{ background: var(--border); border-radius: 3px; }}

.slide.active {{
  opacity: 1;
  pointer-events: auto;
  transform: translateX(0);
  z-index: 2;
}}

.slide.exit-left {{
  opacity: 0;
  transform: translateX(-40px);
}}

/* --- Hero slide --- */
.hero-slide {{
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center;
  padding: 48px 32px;
  position: relative;
}}

.hero-slide::before {{
  content: '';
  position: absolute;
  inset: 0;
  background: url('{hero_image}') center/cover no-repeat;
  opacity: 0.15;
  filter: blur(2px);
}}

.hero-slide::after {{
  content: '';
  position: absolute;
  inset: 0;
  background: radial-gradient(ellipse at center, rgba(10,10,15,0.4) 0%, var(--bg) 80%);
}}

.hero-inner {{
  position: relative;
  z-index: 1;
  max-width: 820px;
}}

.hero-badge {{
  display: inline-block;
  padding: 5px 14px;
  background: rgba(59,130,246,0.12);
  border: 1px solid rgba(59,130,246,0.25);
  border-radius: 20px;
  font-size: 11px;
  font-weight: 600;
  letter-spacing: 1.5px;
  text-transform: uppercase;
  color: var(--accent-blue);
  margin-bottom: 28px;
}}

.hero-inner h1 {{
  font-size: clamp(2.4rem, 5.5vw, 4rem);
  font-weight: 800;
  line-height: 1.08;
  letter-spacing: -0.025em;
  margin-bottom: 20px;
  background: linear-gradient(135deg, #fff 0%, #a8b4ff 50%, #c084fc 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}}

.hero-sub {{
  font-size: clamp(1rem, 2.2vw, 1.25rem);
  color: var(--text-secondary);
  max-width: 680px;
  margin: 0 auto 36px;
  line-height: 1.7;
}}

.hero-quote {{
  font-size: clamp(0.9rem, 1.8vw, 1.05rem);
  color: var(--text-secondary);
  max-width: 780px;
  margin: 0 auto 40px;
  padding: 18px 24px;
  background: rgba(139,92,246,0.07);
  border: 1px solid rgba(139,92,246,0.18);
  border-radius: 14px;
  font-style: italic;
  line-height: 1.7;
}}

.hero-start {{
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 14px 32px;
  background: linear-gradient(135deg, var(--accent-blue), var(--accent-purple));
  border: none;
  border-radius: 12px;
  color: #fff;
  font-size: 15px;
  font-weight: 600;
  cursor: pointer;
  transition: transform 0.2s, box-shadow 0.2s;
}}

.hero-start:hover {{
  transform: translateY(-1px);
  box-shadow: 0 8px 32px rgba(99,102,241,0.35);
}}

.hero-start svg {{
  width: 18px;
  height: 18px;
}}

/* --- Card / Section slide layout --- */
.card-slide {{
  padding: 40px;
  display: flex;
  gap: 36px;
  align-items: flex-start;
  justify-content: center;
}}

.card-visual {{
  flex: 0 0 420px;
  max-width: 420px;
  position: sticky;
  top: 40px;
}}

.card-visual img {{
  width: 100%;
  border-radius: var(--radius);
  display: block;
  box-shadow: 0 8px 40px rgba(0,0,0,0.5);
}}

.card-visual-placeholder {{
  width: 100%;
  aspect-ratio: 16/9;
  border-radius: var(--radius);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 48px;
  font-weight: 800;
  letter-spacing: -2px;
}}

.card-visual-placeholder[data-cat="1"] {{ background: linear-gradient(135deg, rgba(59,130,246,0.15), rgba(59,130,246,0.05)); color: rgba(59,130,246,0.5); }}
.card-visual-placeholder[data-cat="2"] {{ background: linear-gradient(135deg, rgba(139,92,246,0.15), rgba(139,92,246,0.05)); color: rgba(139,92,246,0.5); }}
.card-visual-placeholder[data-cat="3"] {{ background: linear-gradient(135deg, rgba(245,158,11,0.15), rgba(245,158,11,0.05)); color: rgba(245,158,11,0.5); }}
.card-visual-placeholder[data-cat="4"] {{ background: linear-gradient(135deg, rgba(239,68,68,0.15), rgba(239,68,68,0.05)); color: rgba(239,68,68,0.5); }}

.card-content {{
  flex: 1;
  max-width: 560px;
  padding-bottom: 80px;
}}

.act-label {{
  font-size: 11px;
  font-weight: 600;
  letter-spacing: 1.5px;
  text-transform: uppercase;
  color: var(--accent-orange);
  margin-bottom: 16px;
  display: none;
}}

.act-label.visible {{
  display: block;
}}

.card-meta {{
  display: flex;
  align-items: center;
  gap: 10px;
  margin-bottom: 16px;
  flex-wrap: wrap;
}}

.card-id {{
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-width: 34px;
  height: 34px;
  padding: 0 10px;
  border-radius: 9px;
  font-size: 14px;
  font-weight: 700;
}}

.cat-1 .card-id {{ background: rgba(59,130,246,0.15); color: #3b82f6; }}
.cat-2 .card-id {{ background: rgba(139,92,246,0.15); color: #8b5cf6; }}
.cat-3 .card-id {{ background: rgba(245,158,11,0.15); color: #f59e0b; }}
.cat-4 .card-id {{ background: rgba(239,68,68,0.15); color: #ef4444; }}

.cat-label {{
  font-size: 12px;
  color: var(--text-dim);
}}

.conviction-badge {{
  padding: 4px 10px;
  border-radius: 6px;
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.5px;
}}

.conviction-DOING {{ background: rgba(5,150,105,0.18); color: #34d399; }}
.conviction-STRONG {{ background: rgba(37,99,235,0.18); color: #60a5fa; }}
.conviction-EXPLORING {{ background: rgba(217,119,6,0.18); color: #fbbf24; }}

.card-title {{
  font-size: clamp(1.6rem, 3vw, 2.2rem);
  font-weight: 800;
  line-height: 1.15;
  letter-spacing: -0.02em;
  margin-bottom: 8px;
}}

.card-attribution {{
  font-size: 13px;
  color: var(--text-secondary);
  font-style: italic;
  margin-bottom: 16px;
}}

.card-top-badge {{
  display: inline-block;
  padding: 3px 10px;
  background: rgba(245,158,11,0.12);
  border: 1px solid rgba(245,158,11,0.25);
  border-radius: 6px;
  font-size: 10px;
  font-weight: 700;
  letter-spacing: 1px;
  text-transform: uppercase;
  color: var(--accent-orange);
  margin-bottom: 16px;
}}

.card-summary {{
  font-size: 1.05rem;
  color: var(--text-secondary);
  line-height: 1.75;
  margin-bottom: 20px;
}}

/* Details and Why -- always visible */
.card-details {{
  margin-bottom: 20px;
}}

.card-details ul {{
  list-style: none;
  padding: 0;
}}

.card-details li {{
  padding: 8px 0 8px 18px;
  font-size: 0.93rem;
  color: var(--text-secondary);
  line-height: 1.6;
  border-left: 2px solid var(--border);
  margin-left: 2px;
  margin-bottom: 2px;
}}

.card-details li strong {{
  color: var(--text);
}}

.card-why {{
  padding: 14px 18px;
  background: rgba(139,92,246,0.06);
  border: 1px solid rgba(139,92,246,0.15);
  border-radius: var(--radius-sm);
  font-size: 0.9rem;
  color: var(--text-secondary);
  line-height: 1.65;
  margin-bottom: 20px;
}}

.card-why strong {{
  color: var(--text);
}}

/* Tags */
.card-tags {{
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
  margin-bottom: 20px;
}}

.tag {{
  padding: 4px 11px;
  background: rgba(255,255,255,0.05);
  border: 1px solid rgba(255,255,255,0.08);
  border-radius: 10px;
  font-size: 11px;
  color: var(--text-dim);
}}

/* Connections */
.card-connections {{
  padding-top: 16px;
  border-top: 1px solid var(--border);
}}

.card-connections-label {{
  font-size: 11px;
  color: var(--text-dim);
  text-transform: uppercase;
  letter-spacing: 0.5px;
  margin-bottom: 10px;
}}

.conn-chips {{
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
}}

.conn-link {{
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 6px 14px;
  background: rgba(6,182,212,0.08);
  border: 1px solid rgba(6,182,212,0.18);
  border-radius: 8px;
  font-size: 12px;
  font-weight: 500;
  color: var(--accent-cyan);
  cursor: pointer;
  transition: all 0.2s;
  text-decoration: none;
}}

.conn-link:hover {{
  background: rgba(6,182,212,0.18);
  border-color: rgba(6,182,212,0.35);
  transform: translateY(-1px);
}}

.conn-link .conn-title {{
  color: var(--text-secondary);
  font-weight: 400;
  max-width: 180px;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}}

/* ===== SUB-ITEM BLOCKS (NEW) ===== */
.sub-items-container {{
  margin-top: 20px;
  display: flex;
  flex-direction: column;
  gap: 16px;
}}

.sub-item {{
  padding: 16px 18px;
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: var(--radius-sm);
  transition: border-color 0.2s;
}}

.sub-item:target,
.sub-item.highlight {{
  border-color: var(--accent-cyan);
  box-shadow: 0 0 0 1px rgba(6,182,212,0.2);
}}

.sub-header {{
  display: flex;
  align-items: center;
  gap: 10px;
  margin-bottom: 10px;
  flex-wrap: wrap;
}}

.sub-id {{
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-width: 28px;
  height: 28px;
  padding: 0 8px;
  border-radius: 7px;
  font-size: 12px;
  font-weight: 700;
  background: rgba(6,182,212,0.12);
  color: var(--accent-cyan);
}}

.sub-title {{
  font-size: 1rem;
  font-weight: 700;
  color: var(--text);
  flex: 1;
}}

.sub-attribution {{
  font-size: 11px;
  color: var(--text-dim);
  font-style: italic;
  margin-bottom: 6px;
}}

.sub-summary {{
  font-size: 0.9rem;
  color: var(--text-secondary);
  line-height: 1.65;
  margin-bottom: 10px;
}}

.sub-details {{
  margin-bottom: 10px;
}}

.sub-details ul {{
  list-style: none;
  padding: 0;
}}

.sub-details li {{
  padding: 5px 0 5px 14px;
  font-size: 0.85rem;
  color: var(--text-secondary);
  line-height: 1.55;
  border-left: 2px solid var(--border);
  margin-left: 2px;
  margin-bottom: 1px;
}}

.sub-details li strong {{
  color: var(--text);
}}

.sub-why {{
  padding: 10px 14px;
  background: rgba(139,92,246,0.05);
  border: 1px solid rgba(139,92,246,0.12);
  border-radius: 8px;
  font-size: 0.83rem;
  color: var(--text-secondary);
  line-height: 1.6;
  margin-bottom: 10px;
}}

.sub-why strong {{ color: var(--text); }}

.sub-tags {{
  display: flex;
  flex-wrap: wrap;
  gap: 4px;
  margin-bottom: 10px;
}}

.sub-tags .tag {{
  font-size: 10px;
  padding: 2px 8px;
}}

.sub-connections {{
  padding-top: 8px;
  border-top: 1px solid rgba(255,255,255,0.05);
}}

.sub-connections .conn-chips {{
  gap: 6px;
}}

.sub-connections .conn-link {{
  padding: 4px 10px;
  font-size: 11px;
}}

/* --- Synthesis slide --- */
.synthesis-slide {{
  flex-direction: column;
  align-items: center;
  padding: 48px 32px 80px;
}}

.synthesis-inner {{
  max-width: 720px;
  width: 100%;
}}

.synthesis-title {{
  font-size: clamp(1.8rem, 4vw, 2.6rem);
  font-weight: 800;
  margin-bottom: 36px;
  background: linear-gradient(135deg, #c084fc, #60a5fa);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  text-align: center;
}}

.synth-block {{
  margin-bottom: 32px;
}}

.synth-block h3 {{
  font-size: 1.15rem;
  font-weight: 700;
  margin-bottom: 8px;
}}

.synth-block p {{
  font-size: 0.98rem;
  color: var(--text-secondary);
  line-height: 1.75;
}}

.synth-block strong {{ color: var(--text); }}

.synth-pipeline {{
  text-align: center;
  padding: 18px 24px;
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: var(--radius-sm);
  font-family: 'SF Mono', 'Fira Code', monospace;
  font-size: 0.9rem;
  color: var(--accent-cyan);
  margin: 16px 0 24px;
  letter-spacing: 0.5px;
}}

/* --- Bottom nav --- */
.bottom-nav {{
  flex-shrink: 0;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 12px 24px;
  background: rgba(10,10,15,0.9);
  backdrop-filter: blur(16px);
  border-top: 1px solid var(--border);
  z-index: 10;
}}

.nav-btn {{
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 10px 20px;
  background: var(--surface-alt);
  border: 1px solid var(--border);
  border-radius: 10px;
  color: var(--text);
  font-size: 14px;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s;
  white-space: nowrap;
}}

.nav-btn:hover {{
  background: var(--border);
}}

.nav-btn:disabled {{
  opacity: 0.3;
  cursor: default;
}}

.nav-btn:disabled:hover {{
  background: var(--surface-alt);
}}

.nav-btn.primary {{
  background: linear-gradient(135deg, var(--accent-blue), var(--accent-purple));
  border-color: transparent;
  color: #fff;
}}

.nav-btn.primary:hover {{
  box-shadow: 0 4px 20px rgba(99,102,241,0.3);
}}

.nav-btn svg {{
  width: 16px;
  height: 16px;
}}

.nav-center {{
  display: flex;
  align-items: center;
  gap: 8px;
}}

.return-btn {{
  display: none;
  align-items: center;
  gap: 6px;
  padding: 8px 16px;
  background: rgba(245,158,11,0.1);
  border: 1px solid rgba(245,158,11,0.25);
  border-radius: 8px;
  color: var(--accent-orange);
  font-size: 13px;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s;
}}

.return-btn.visible {{
  display: inline-flex;
}}

.return-btn:hover {{
  background: rgba(245,158,11,0.18);
}}

.return-btn svg {{
  width: 14px;
  height: 14px;
}}

.key-hint {{
  font-size: 11px;
  color: var(--text-dim);
}}

.key-hint kbd {{
  display: inline-block;
  padding: 2px 6px;
  background: var(--surface-alt);
  border: 1px solid var(--border);
  border-radius: 4px;
  font-family: inherit;
  font-size: 10px;
}}

/* --- Overview modal --- */
.overview-overlay {{
  position: fixed;
  inset: 0;
  background: rgba(0,0,0,0.7);
  backdrop-filter: blur(8px);
  z-index: 200;
  display: none;
  align-items: center;
  justify-content: center;
  padding: 24px;
}}

.overview-overlay.visible {{
  display: flex;
}}

.overview-panel {{
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  max-width: 800px;
  width: 100%;
  max-height: 80vh;
  overflow-y: auto;
  padding: 28px;
}}

.overview-header {{
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 20px;
}}

.overview-header h2 {{
  font-size: 1.3rem;
  font-weight: 700;
}}

.overview-close {{
  width: 32px;
  height: 32px;
  background: var(--surface-alt);
  border: 1px solid var(--border);
  border-radius: 8px;
  color: var(--text-secondary);
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 16px;
  transition: all 0.2s;
}}

.overview-close:hover {{
  background: var(--border);
  color: var(--text);
}}

.overview-act {{
  margin-bottom: 16px;
}}

.overview-act-label {{
  font-size: 11px;
  font-weight: 600;
  letter-spacing: 1px;
  text-transform: uppercase;
  color: var(--accent-orange);
  margin-bottom: 8px;
}}

.overview-list {{
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
}}

.overview-item {{
  padding: 6px 14px;
  background: var(--surface-alt);
  border: 1px solid var(--border);
  border-radius: 8px;
  font-size: 13px;
  color: var(--text-secondary);
  cursor: pointer;
  transition: all 0.15s;
}}

.overview-item:hover {{
  background: var(--border);
  color: var(--text);
}}

.overview-item.current {{
  border-color: var(--accent-blue);
  color: var(--accent-blue);
}}

.overview-item .ov-id {{
  font-weight: 700;
  margin-right: 4px;
}}

/* Responsive */
@media (max-width: 900px) {{
  .card-slide {{
    flex-direction: column;
    padding: 24px 20px;
    gap: 20px;
  }}
  .card-visual {{
    flex: none;
    max-width: 100%;
    position: static;
  }}
  .card-content {{
    max-width: 100%;
    padding-bottom: 40px;
  }}
  .card-title {{ font-size: 1.5rem; }}
  .hero-inner h1 {{ font-size: 2rem; }}
  .breadcrumb-bar {{ padding: 6px 16px 2px; }}
  .section-nav {{ padding: 2px 16px 6px; }}
}}

@media (max-width: 480px) {{
  .top-bar {{ padding: 8px 12px; }}
  .bottom-nav {{ padding: 8px 12px; }}
  .card-slide {{ padding: 16px 12px; }}
  .nav-btn {{ padding: 8px 14px; font-size: 13px; }}
  .key-hint {{ display: none; }}
  .breadcrumb-bar {{ padding: 4px 12px 2px; font-size: 11px; }}
  .section-nav {{ padding: 2px 12px 4px; }}
  .sec-chip {{ font-size: 10px; padding: 3px 8px; }}
}}
</style>
</head>
<body>

<div id="app">
  <!-- Top bar -->
  <div class="top-bar">
    <span class="top-bar-title">One AEM Workshop</span>
    <div class="progress-track"><div class="progress-fill" id="progressFill"></div></div>
    <span class="progress-label" id="progressLabel">1 / 1</span>
    <button class="overview-btn" id="overviewBtn">Overview</button>
  </div>

  <!-- Breadcrumb (NEW) -->
  <div class="breadcrumb-bar" id="breadcrumbBar"></div>

  <!-- Section navigator (NEW) -->
  <div class="section-nav" id="sectionNav"></div>

  <!-- Slides -->
  <div class="slide-area" id="slideArea"></div>

  <!-- Bottom nav -->
  <div class="bottom-nav">
    <button class="nav-btn" id="prevBtn" disabled>
      <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" d="M15.75 19.5 8.25 12l7.5-7.5"/></svg>
      Previous
    </button>
    <div class="nav-center">
      <button class="return-btn" id="returnBtn">
        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" d="M9 15 3 9m0 0 6-6M3 9h12a6 6 0 0 1 0 12h-3"/></svg>
        Back to story
      </button>
      <span class="key-hint"><kbd>\u2190</kbd> <kbd>\u2192</kbd> to navigate</span>
    </div>
    <button class="nav-btn primary" id="nextBtn">
      Next
      <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" d="m8.25 4.5 7.5 7.5-7.5 7.5"/></svg>
    </button>
  </div>
</div>

<!-- Overview modal -->
<div class="overview-overlay" id="overviewOverlay">
  <div class="overview-panel" id="overviewPanel"></div>
</div>

<script>
// Data
const sections = {sections_json};
const imageMap = {image_map_json};
const storyOrder = {story_order_json};
const actLabels = {act_labels_json};
const acts = {acts_json};
const cardToSection = {card_to_section_json};
const categories = {categories_json};

// Index lookups
const sectionById = {{}};
sections.forEach(s => {{ sectionById[s.id] = s; }});

// itemById includes both sections and sub-items (for connection label resolution)
const itemById = {{}};
sections.forEach(s => {{
  itemById[s.id] = s;
  (s.sub_items || []).forEach(sub => {{ itemById[sub.id] = sub; }});
}});

// Total slides = hero(0) + sections(1..N) + synthesis(N+1)
const totalSlides = 1 + storyOrder.length + 1;

// State
let currentSlide = 0;
let storyPosition = 0;
let jumpStack = [];

// --- Build slides ---
const slideArea = document.getElementById('slideArea');

function buildHeroSlide() {{
  const d = document.createElement('div');
  d.className = 'slide hero-slide';
  d.dataset.slideIndex = '0';
  d.innerHTML = `
    <div class="hero-inner">
      <div class="hero-badge">One AEM Directors+ Workshop</div>
      <h1>Becoming an AI Native Team</h1>
      <p class="hero-sub">{HERO_SUB}</p>
      <div class="hero-quote">{HERO_QUOTE}</div>
      <button class="hero-start" onclick="goTo(1)">
        Begin the story
        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" d="m8.25 4.5 7.5 7.5-7.5 7.5"/></svg>
      </button>
    </div>
  `;
  slideArea.appendChild(d);
}}

function buildConnectionChips(connections) {{
  if (!connections || connections.length === 0) return '';
  const chips = connections.map(cid => {{
    const target = itemById[cid];
    const title = target ? target.title : cid;
    return `<span class="conn-link" onclick="jumpTo('${{cid}}')"><strong>${{cid}}</strong> <span class="conn-title">${{title}}</span></span>`;
  }}).join('');
  return `<div class="card-connections"><div class="card-connections-label">Connections \u2014 jump to explore</div><div class="conn-chips">${{chips}}</div></div>`;
}}

function buildSubConnectionChips(connections) {{
  if (!connections || connections.length === 0) return '';
  const chips = connections.map(cid => {{
    const target = itemById[cid];
    const title = target ? target.title : cid;
    return `<span class="conn-link" onclick="jumpTo('${{cid}}')"><strong>${{cid}}</strong> <span class="conn-title">${{title}}</span></span>`;
  }}).join('');
  return `<div class="sub-connections"><div class="conn-chips">${{chips}}</div></div>`;
}}

function buildSubItem(sub) {{
  const convBadge = sub.conviction
    ? `<span class="conviction-badge conviction-${{sub.conviction}}">${{sub.conviction}}</span>`
    : '';

  const attrHtml = sub.attribution
    ? `<div class="sub-attribution">\u2014 ${{sub.attribution}}</div>`
    : '';

  let detailsHtml = '';
  if (sub.details && sub.details.length > 0) {{
    detailsHtml = `<div class="sub-details"><ul>${{sub.details.map(d => `<li>${{d}}</li>`).join('')}}</ul></div>`;
  }}

  let whyHtml = '';
  if (sub.why) {{
    whyHtml = `<div class="sub-why">${{sub.why}}</div>`;
  }}

  const tagsHtml = (sub.tags || []).map(t => `<span class="tag">#${{t}}</span>`).join('');
  const connHtml = buildSubConnectionChips(sub.connections);

  return `
    <div class="sub-item" id="sub-${{sub.id}}">
      <div class="sub-header">
        <span class="sub-id">${{sub.id.replace('_CAT4', '')}}</span>
        <span class="sub-title">${{sub.title}}</span>
        ${{convBadge}}
      </div>
      ${{attrHtml}}
      <p class="sub-summary">${{sub.summary}}</p>
      ${{detailsHtml}}
      ${{whyHtml}}
      <div class="sub-tags">${{tagsHtml}}</div>
      ${{connHtml}}
    </div>
  `;
}}

function buildSectionSlide(sectionId, slideIndex) {{
  const sec = sectionById[sectionId];
  if (!sec) return;
  const cat = sec.category || 1;
  const catData = categories[cat] || {{}};
  const hasSubs = sec.sub_items && sec.sub_items.length > 0;

  const d = document.createElement('div');
  d.className = 'slide card-slide cat-' + cat;
  d.dataset.slideIndex = slideIndex;
  d.dataset.sectionId = sectionId;

  // Visual
  let visualHtml;
  if (imageMap[sectionId]) {{
    visualHtml = `<div class="card-visual"><img src="${{imageMap[sectionId]}}" alt="${{sec.title}}" /></div>`;
  }} else {{
    visualHtml = `<div class="card-visual"><div class="card-visual-placeholder" data-cat="${{cat}}">${{sectionId}}</div></div>`;
  }}

  // Act label
  const act = actLabels[sectionId];
  const actHtml = act ? `<div class="act-label visible">${{act}}</div>` : '';

  // Build content based on whether section has sub-items
  let contentHtml;

  if (hasSubs) {{
    // Section with sub-items: show section title + sub-item blocks
    const subsHtml = sec.sub_items.map(sub => buildSubItem(sub)).join('');
    contentHtml = `
      ${{actHtml}}
      <div class="card-meta">
        <span class="card-id">${{sectionId}}</span>
        <span class="cat-label">${{catData.name || ''}}</span>
      </div>
      <div class="card-title">${{sec.title}}</div>
      <div class="sub-items-container">${{subsHtml}}</div>
    `;
  }} else {{
    // Standalone section: show full card
    const topHtml = sec.top ? `<div class="card-top-badge">\u2b50 Top Insight</div>` : '';
    const attrHtml = sec.attribution ? `<div class="card-attribution">\u2014 ${{sec.attribution}}</div>` : '';

    let detailsHtml = '';
    if (sec.details && sec.details.length > 0) {{
      detailsHtml = `<div class="card-details"><ul>${{sec.details.map(d => `<li>${{d}}</li>`).join('')}}</ul></div>`;
    }}

    let whyHtml = '';
    if (sec.why) {{
      whyHtml = `<div class="card-why">${{sec.why}}</div>`;
    }}

    const tagsHtml = (sec.tags || []).map(t => `<span class="tag">#${{t}}</span>`).join('');
    const connHtml = buildConnectionChips(sec.connections);

    contentHtml = `
      ${{actHtml}}
      <div class="card-meta">
        <span class="card-id">${{sectionId}}</span>
        <span class="cat-label">${{catData.name || ''}}</span>
        ${{sec.conviction ? `<span class="conviction-badge conviction-${{sec.conviction}}">${{sec.conviction}}</span>` : ''}}
      </div>
      ${{topHtml}}
      <div class="card-title">${{sec.title}}</div>
      ${{attrHtml}}
      <div class="card-summary">${{sec.summary || ''}}</div>
      ${{detailsHtml}}
      ${{whyHtml}}
      <div class="card-tags">${{tagsHtml}}</div>
      ${{connHtml}}
    `;
  }}

  d.innerHTML = `
    ${{visualHtml}}
    <div class="card-content">
      ${{contentHtml}}
    </div>
  `;
  slideArea.appendChild(d);
}}

function buildSynthesisSlide(slideIndex) {{
  const d = document.createElement('div');
  d.className = 'slide synthesis-slide';
  d.dataset.slideIndex = slideIndex;
  d.innerHTML = `
    <div class="synthesis-inner">
      <div class="synthesis-title">Synthesis: Top Takeaways</div>

{synth_blocks_html}
    </div>
  `;
  slideArea.appendChild(d);
}}

// Build all slides
buildHeroSlide();
storyOrder.forEach((id, i) => buildSectionSlide(id, i + 1));
buildSynthesisSlide(totalSlides - 1);

const allSlides = slideArea.querySelectorAll('.slide');

// --- Breadcrumb & Section Nav ---
const breadcrumbBar = document.getElementById('breadcrumbBar');
const sectionNav = document.getElementById('sectionNav');

function updateBreadcrumbAndNav() {{
  // Hide for hero and synthesis
  if (currentSlide === 0 || currentSlide === totalSlides - 1) {{
    breadcrumbBar.classList.remove('visible');
    sectionNav.classList.remove('visible');
    return;
  }}

  const storyIdx = currentSlide - 1;
  const sectionId = storyOrder[storyIdx];
  const sec = sectionById[sectionId];
  if (!sec) return;

  const actData = acts[sec.act] || {{ name: '', subtitle: '' }};

  // Breadcrumb
  breadcrumbBar.classList.add('visible');
  breadcrumbBar.innerHTML = `
    <span class="bc-act" onclick="openOverview()">${{actData.name}}</span>
    <span class="bc-sep">\u203a</span>
    <span class="bc-category">${{actData.subtitle}}</span>
    <span class="bc-sep">\u203a</span>
    <span class="bc-section">${{sec.title}}</span>
  `;

  // Section nav chips -- siblings in the same act
  sectionNav.classList.add('visible');
  const siblings = storyOrder.filter(id => {{
    const s = sectionById[id];
    return s && s.act === sec.act;
  }});

  sectionNav.innerHTML = siblings.map(id => {{
    const s = sectionById[id];
    const isActive = id === sectionId;
    const label = s.chip || s.title;
    return `<span class="sec-chip ${{isActive ? 'active' : ''}}" onclick="goToSection('${{id}}')">${{label}}</span>`;
  }}).join('');

  // Scroll active chip into view
  setTimeout(() => {{
    const activeChip = sectionNav.querySelector('.sec-chip.active');
    if (activeChip) activeChip.scrollIntoView({{ behavior: 'smooth', block: 'nearest', inline: 'center' }});
  }}, 50);
}}

function goToSection(sectionId) {{
  const storyIdx = storyOrder.indexOf(sectionId);
  if (storyIdx === -1) return;
  const slideIdx = storyIdx + 1;
  goTo(slideIdx);
  storyPosition = slideIdx;
  jumpStack = [];
}}

// --- Navigation ---
function updateUI() {{
  // Update slides
  allSlides.forEach((s, i) => {{
    s.classList.remove('active', 'exit-left');
    if (i === currentSlide) {{
      s.classList.add('active');
      s.scrollTop = 0;
    }}
  }});

  // Progress
  const pct = ((currentSlide) / (totalSlides - 1)) * 100;
  document.getElementById('progressFill').style.width = pct + '%';
  document.getElementById('progressLabel').textContent = (currentSlide + 1) + ' / ' + totalSlides;

  // Prev/Next
  document.getElementById('prevBtn').disabled = currentSlide === 0;
  const nextBtn = document.getElementById('nextBtn');
  nextBtn.disabled = currentSlide === totalSlides - 1;
  nextBtn.innerHTML = currentSlide === 0
    ? 'Begin <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" d="m8.25 4.5 7.5 7.5-7.5 7.5"/></svg>'
    : 'Next <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" d="m8.25 4.5 7.5 7.5-7.5 7.5"/></svg>';

  // Return button
  const returnBtn = document.getElementById('returnBtn');
  returnBtn.classList.toggle('visible', jumpStack.length > 0);

  // Breadcrumb + section nav
  updateBreadcrumbAndNav();
}}

function goTo(index) {{
  if (index < 0 || index >= totalSlides) return;
  allSlides[currentSlide].classList.add('exit-left');
  currentSlide = index;
  if (index >= 1 && index <= storyOrder.length) {{
    storyPosition = index;
  }}
  updateUI();
}}

function goNext() {{
  if (jumpStack.length > 0) {{
    const nextStory = storyPosition + 1;
    if (nextStory < totalSlides) {{
      jumpStack = [];
      goTo(nextStory);
    }}
  }} else {{
    goTo(currentSlide + 1);
    storyPosition = currentSlide;
  }}
}}

function goPrev() {{
  if (jumpStack.length > 0) {{
    returnToStory();
  }} else {{
    goTo(currentSlide - 1);
    storyPosition = currentSlide;
  }}
}}

function jumpTo(cardId) {{
  // Resolve card ID to parent section
  const sectionId = cardToSection[cardId] || cardId;
  const storyIdx = storyOrder.indexOf(sectionId);
  if (storyIdx === -1) return;
  const slideIdx = storyIdx + 1;

  // If already on this section, just scroll to sub-item
  if (slideIdx === currentSlide) {{
    const subEl = document.getElementById('sub-' + cardId);
    if (subEl) {{
      subEl.scrollIntoView({{ behavior: 'smooth', block: 'center' }});
      subEl.classList.add('highlight');
      setTimeout(() => subEl.classList.remove('highlight'), 2000);
    }}
    return;
  }}

  // Navigate to section
  jumpStack.push(storyPosition);
  goTo(slideIdx);

  // If targeting a sub-item, scroll to it after transition
  if (cardId !== sectionId) {{
    setTimeout(() => {{
      const subEl = document.getElementById('sub-' + cardId);
      if (subEl) {{
        subEl.scrollIntoView({{ behavior: 'smooth', block: 'center' }});
        subEl.classList.add('highlight');
        setTimeout(() => subEl.classList.remove('highlight'), 2000);
      }}
    }}, 400);
  }}
}}

function returnToStory() {{
  if (jumpStack.length === 0) return;
  const pos = jumpStack.pop();
  goTo(pos);
  storyPosition = pos;
}}

// Events
document.getElementById('nextBtn').addEventListener('click', goNext);
document.getElementById('prevBtn').addEventListener('click', goPrev);
document.getElementById('returnBtn').addEventListener('click', returnToStory);

document.addEventListener('keydown', (e) => {{
  if (document.getElementById('overviewOverlay').classList.contains('visible')) {{
    if (e.key === 'Escape') closeOverview();
    return;
  }}
  if (e.key === 'ArrowRight' || e.key === ' ') {{ e.preventDefault(); goNext(); }}
  if (e.key === 'ArrowLeft') {{ e.preventDefault(); goPrev(); }}
  if (e.key === 'Escape' && jumpStack.length > 0) {{ returnToStory(); }}
}});

// Touch / swipe
let touchStartX = 0;
slideArea.addEventListener('touchstart', e => {{ touchStartX = e.touches[0].clientX; }}, {{ passive: true }});
slideArea.addEventListener('touchend', e => {{
  const dx = e.changedTouches[0].clientX - touchStartX;
  if (Math.abs(dx) > 60) {{
    if (dx < 0) goNext();
    else goPrev();
  }}
}}, {{ passive: true }});

// --- Overview ---
function openOverview() {{
  const panel = document.getElementById('overviewPanel');
  let html = `<div class="overview-header"><h2>All Sections</h2><button class="overview-close" onclick="closeOverview()">\u2715</button></div>`;

  let currentAct = '';
  storyOrder.forEach((id, i) => {{
    const slideIdx = i + 1;
    const sec = sectionById[id];
    const act = actLabels[id];
    if (act) {{
      if (currentAct) html += `</div></div>`;
      html += `<div class="overview-act"><div class="overview-act-label">${{act}}</div><div class="overview-list">`;
      currentAct = act;
    }}
    const isCurrent = slideIdx === currentSlide ? ' current' : '';
    html += `<span class="overview-item${{isCurrent}}" onclick="goToFromOverview(${{slideIdx}})"><span class="ov-id">${{id}}</span>${{sec ? sec.title : id}}</span>`;
  }});
  html += `</div></div>`;

  panel.innerHTML = html;
  document.getElementById('overviewOverlay').classList.add('visible');
}}

function closeOverview() {{
  document.getElementById('overviewOverlay').classList.remove('visible');
}}

function goToFromOverview(idx) {{
  closeOverview();
  jumpStack = [];
  storyPosition = idx;
  goTo(idx);
}}

document.getElementById('overviewBtn').addEventListener('click', openOverview);
document.getElementById('overviewOverlay').addEventListener('click', (e) => {{
  if (e.target === e.currentTarget) closeOverview();
}});

// Init
updateUI();
allSlides[0].classList.add('active');
</script>
</body>
</html>'''

with open(OUTPUT, 'w') as f:
    f.write(html)

print(f"Workshop experience built: {OUTPUT}")
print(f"Total sections: {len(STORY_ORDER)}")
print(f"Total slides: {1 + len(STORY_ORDER) + 1} (hero + {len(STORY_ORDER)} sections + synthesis)")
print(f"File size: {os.path.getsize(OUTPUT) / 1024 / 1024:.1f} MB")
