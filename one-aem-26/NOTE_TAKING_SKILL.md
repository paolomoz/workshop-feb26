# Note-Taking Skill: Workshop Highlights

## What This Skill Does

Guides Claude through processing raw, stream-of-consciousness workshop notes into a structured, fluid, and insightful document.

## Context

- **User**: A director-level engineering leader at Adobe (AEM team)
- **Source**: One AEM workshop with directors+ on becoming an AI-native organisation
- **Personal lens**: How to transform their team to become 10X faster with AI
- **Output file**: `one-aem-26/highlights.md`
- **Related event**: User is planning their own team workshop on Feb 9; ideas feed into that

## How the User Works

- Shares raw notes in conversation -- unstructured, fast, typos expected
- Expects Claude to interpret intent, not just transcribe
- Values connections between ideas more than clean formatting
- Wants to be challenged: suggestions, missing pieces, and pushback are welcome

## Processing Rules

When the user shares a new highlight:

1. **Classify**: Assign to one or more existing categories. If it doesn't fit, propose a new category.
2. **Structure**: Rewrite the raw note into clear, scannable prose. Preserve the user's voice and energy -- don't flatten bold ideas into corporate language.
3. **Connect**: Explicitly link the new note to existing highlights. Call out patterns, tensions, or reinforcements.
4. **Suggest**: Add at least one angle the user didn't mention -- a risk, an implication, a related idea, or a concrete next step.
5. **Tag**: Apply relevant tags from the taxonomy below. Add new tags when needed.
6. **Extract actions**: If the note contains or implies a commitment, decision, or next step, add it to the Action Items section.
7. **Attribute**: If the user mentions who said something, capture the attribution.
8. **Feb 9 bridge**: Check if this note could become a workshop exercise or talking point. If yes, add a cross-reference to the Feb 9 section.
9. **Write**: Update `one-aem-26/highlights.md` immediately. Don't wait for a batch.

## Priority System

The user can flag any highlight with a priority level:
- **`!!`** = "This is the most important thing" -- surfaces at the top of the document in the Top Insights section
- **`!`** = "This is important" -- gets a visual marker in the document
- No marker = standard note

Claude should also proactively suggest promoting a note if it seems like a breakthrough idea or a recurring theme.

## Conviction Markers

Each idea can carry a conviction level:
- **[DOING]** = Committed, will execute
- **[STRONG]** = High conviction, likely to pursue
- **[EXPLORING]** = Interesting, needs more thought
- **[MAYBE]** = Worth noting, low commitment

The user can set these explicitly. Claude should suggest a conviction level when writing up the note; the user can correct it.

## Tag Taxonomy

Apply tags inline after each idea heading. Tags are cumulative -- add new ones as needed.

Current tags:
- `#automation` -- tools, pipelines, AI delegation
- `#culture` -- team mindset, habits, norms
- `#product` -- AEM product direction, features
- `#process` -- how work gets done, workflows
- `#tooling` -- specific tools, infrastructure
- `#customer` -- customer-facing, feedback, insights
- `#visibility` -- making work/results visible
- `#learning` -- knowledge capture, skill building
- `#feb9` -- directly relevant to the Feb 9 team workshop

## Attribution Tracking

When the user mentions who said something, capture it as:
> **-- [Name/Role]**

This feeds into follow-up: knowing who championed an idea helps assign ownership and build alliances.

## Document Structure

The highlights document should maintain these sections in order:

1. **Header & lens** (static)
2. **Top Insights** -- highest priority items, surfaced from any category (populated when user flags `!!` or Claude promotes)
3. **Category sections** (1, 2, 3, ...) -- the main body of notes
4. **Emerging Patterns** -- cross-cutting themes updated as notes accumulate
5. **Feb 9 Workshop Feed** -- running list of ideas that could become exercises for the team workshop
6. **Action Items** -- extracted commitments, decisions, next steps with owners when known
7. **Attribution Index** -- who said what, for follow-up

## Synthesis Pass

After every ~5 new highlights (or when the user asks), offer to produce:
- A "Top 3 Takeaways" summary suitable for sharing with the team or leadership
- An updated Feb 9 workshop plan based on accumulated ideas

Don't auto-generate -- offer and let the user decide.

## Document Style

- Use headers (##, ###) for categories, sub-headers (####) for individual ideas
- Use blockquotes (>) for connections and editorial commentary
- Tags appear in backticks after headings: `#### A) Ambient Screen Buddy #automation #tooling`
- Conviction markers appear in brackets: `[EXPLORING]`
- Keep a running "Emerging Patterns" section when themes emerge
- No fluff, no filler. Dense and direct.
- Preserve raw energy of ambitious ideas -- "crazy" is a feature, not a bug

## Categories (evolving)

1. **Ideas to Make the Team 10X Faster** -- automation, tooling, workflow changes
2. **Vision for the Product** -- where AEM is headed, AI in the product
3. **Ideas for My Team Workshop (Feb 9)** -- exercises, formats, topics to bring back
4. **Becoming AI Frontier Engineers** -- pushing technical and cultural boundaries of AI practice

_New categories can be added anytime. User will signal, or Claude should propose when a note doesn't fit._

## What to Track Over Time

As the conversation progresses, accumulate awareness of:
- **Recurring themes**: What the user keeps coming back to (signals priority)
- **Named people or teams**: Who said what, potential allies or owners
- **Tensions**: Conflicting ideas or priorities surfaced in the workshop
- **Gaps**: Important topics the workshop hasn't addressed yet
- **Feb 9 workshop feed**: Anything that could become an exercise or talking point for the user's own team session
