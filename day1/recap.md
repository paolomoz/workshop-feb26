# Day 1 Recap — February 9, 2026

**Location**: Basel (in-person + remote participants)
**Sessions**: Morning (Paolo), Afternoon (Philipp Koch guest session + team discussion)

---

## Top Insights

### 1. The real bottleneck is ideas, not code `#culture` `#automation` [STRONG]
Coding is converging toward zero cost. The 75% of the team's effort should go into discovering what to build — getting to customers, understanding real pain points, abstracting small needs into bigger ideas. The remaining effort is execution (shrinking fast) and operationalisation (still hard but improving).
> **— Paolo**

### 2. The 8 Tiers of AI Adoption `#learning` `#culture` [STRONG]
Framework from Steven Yankee (Gaston/Bids creator). Tiers 1-4 are IDE-centric (tab completion → prompt-verify → YOLO mode → single agent). Tier 5+ shifts the mindset away from the IDE: multi-tab agents (Tier 6), managing many parallel projects (Tier 7), orchestrating hierarchical agent swarms (Tier 8). The team's immediate goal: get everyone confidently to Tier 7 and collectively figure out what Tier 8 looks like.
> **— Paolo, with references to Anthropic's agent teams release with Claude 4.6**

### 3. Fast ≠ extra hours — it's a team convention `#culture` `#process` [DOING]
When anyone says "fast" or "faster," it means improving efficiency, not working more. If you're stuck at a lower AI tier, no amount of extra hours gets you further — you hit 24h and that's it. The only way to go faster is to level up.
> **— Paolo, agreed by the team**

### 4. Unlearn is the #1 key to transformation `#culture` `#learning` [STRONG]
Philipp Koch's biggest takeaway from leading the Astra team: the hardest and most valuable thing is unlearning years of habits — sprint rituals, deference to PMs, reluctance to engage customers directly. Everything else follows from willingness to unlearn.
> **— Philipp Koch**

### 5. Trust is built through flawless execution and data, not stories `#customer` [STRONG]
Coca-Cola case study: a frustrated customer was won over by weekly demos, data-backed results (OpenTelemetry, etc.), and consistently delivering. Once trust is earned, the customer opens up to deeper co-innovation. Demo-driven cadence (status → demos → special topics) is the format.
> **— Philipp Koch**

---

## Session 1: Workshop Framing & Business Context (11:19 AM)

### What this team is `#culture` `#product`
This is not a team that owns a single product area. The mandate is to **discover accelerators** — things that work for customers and for internal Adobe sales. The team finds valuable ideas, validates them with customers, and either hands them off or continues building. Examples: Experience Catalyst, Digital Insights, generative websites, content discovery.

### The customer discovery model `#customer` `#process`
- **Current state**: mostly reactive — sales or field asks for help closing a deal, often with pre-shaped requirements that don't reflect the real need
- **Planned improvement**: leverage Cloud Service Matter Experts (CSMEs) in Adam's team who talk to customers daily — enable them with awareness of what the team builds, so they naturally feed back opportunities
- **Other channels**: ACS (Adobe Consulting), partner SIs (e.g. Netcentric), Adobe Support Slack channels with customer discussions
- **Key principle**: Don't take customer requests at face value. Dig to the real pain point. "If I only listened to the customer, we'd have faster horses." — but also don't ignore them

### The abstraction play `#product` `#culture`
When a customer gives you a 5-point need, deliver the 5 points. But abstract it into a 100-point idea. Test the bigger idea with the next customer. Two forces combined: serve the immediate need + explore the larger opportunity.

### The crosswalk/DA/UE debate `#product`
Active discussion about whether crosswalk should remain officially supported in Experience Catalyst. DA (Document Authoring) becoming more official, crosswalk becoming less so. Gabriel mentioned eventual support for SharePoint and Google Docs on DA. But the real winner might be a new conversational UI — "just type what you want" — rather than any current authoring paradigm.

---

## Session 2: The Anthropic Hive Mind — Video & Discussion (~1:19 PM)

### Key concepts from the Steven Yankee article `#culture` `#learning`
- **Golden Ages**: periods where there's more work than people — no politics, pure innovation. They die when there are more people than work. Anthropic is currently in a golden age.
- **Campfire Model**: no waterfall, no specs — a living prototype evolves via group sculpting. Anthropic ships within days of first idea (Claude Cowork: 10 days from idea to public).
- **Yes-And culture**: improvisational theatre approach. Every idea welcomed, examined, judged by the hive mind. No central decision authority. "Come in guns blazing, make it about yourself, and you're out."
- **Chaos as feature**: no OKRs, no strategy decks, 90-day max planning horizon. Vibes, not process.
- **Build for yourself**: the Settlers of Catan inventor spent years building games for his own family first.

### Team reactions and debate `#culture`
- **Skepticism about "just demo and see what sticks"**: Anthropic is too consistent in shipping great things — there must be a weighing/filtering mechanism above the chaos. They are surgically precise (Agent SDK, Cowork, Claude Code) vs. OpenAI which had a phase of throwing everything out.
- **IP and idea sharing**: In the new world, there's no separation between idea and code — anyone can prompt-reproduce your idea instantly. The team's advantage is **access to AEM customers** that the outside world doesn't have. Be open internally at Adobe, but thoughtful externally.
- **"The code itself is immaterial"**: What matters is the outcome for the customer, not the implementation. Any code we write will be trivially reproducible soon. But building it now is still the best way to ride the wave and stay ahead.
- **Context switching is the new burnout risk**: Managing many parallel streams is cognitively exhausting. "Like running marathon after marathon for 8 hours." The team needs to be conscious of this from the start.

---

## Session 3: Philipp Koch — Astra Team Journey (1:34 PM)

### Origin story `#culture` `#process`
In early 2025, Philipp gave up leadership of the 150-person AEM Assets Engineering org to lead Astra — a 7-8 person fast iteration team. Mandate from JM: **"Breathe new life into the assets ecosystem by thinking differently."** Challenge assumptions, embrace simplicity, move at a speed that traditional models can't support.

### 6 mindset shifts `#culture` `#learning`
1. **Unlearn** — question everything done the same way for years
2. **Be curious** — "I don't know" is a starting point, not a weakness
3. **Think out-of-the-box** — look at non-conventional, unknown industry approaches
4. **Get close to customers/practitioners** — direct, unfiltered feedback vs. filtered-through-PM feedback. Philipp's "huge aha moment."
5. **Find out what fast iteration means** — started exploring AI-assisted coding even when team was skeptical (end of 2024)
6. **Measure outcomes** — set aggressive KPIs to stay honest and on course

### 3 operating principles `#process`
1. **Move fast, learn faster** — no months-long cycles without customer validation
2. **Start with the real use** — every experiment grounded in actual practitioner need
3. **Apply AI intentionally** — don't overdo it, use AI where it makes sense

### AI as force multiplier — timeline `#automation` `#learning`
- **March 2025**: Philipp starts vibe coding personally (hadn't written code in 10 years). Built 3 apps in 14 hours.
- **April 2025**: Team hackathon in Bucharest — everyone on Cursor, vibe coding small projects
- **May-June 2025**: Loaned 2.5 engineers to build LLMO from scratch — first real push of AI coding boundaries
- **August 2025**: Took on KO Assets co-innovation — rebuilt a 3-year-old app in 4 months from scratch with AI
- **Key insight**: "There is no 'I caught up.' AI evolves every day. Unlearn what worked yesterday."

### Coca-Cola case study `#customer` `#process`
- **Problem**: Asset Share Commons app, 3 years of messy consulting iterations, skyrocketing TCO, no API separation, impossible to add new features (e.g. Content AI)
- **Solution**: Complete rebuild on EDS with APIs and Dynamic Media — massively reduced TCO
- **Trust-building method**: Weekly meetings with only 3 slides (status, demos, special topics). Most time spent on demos. Customer body language told them when they hit the mark.
- **Result**: Trust earned → customer opened up to deeper co-innovation opportunities (e.g. live data reporting)
- **Handover model**: Involve an SI early so they can take ownership when the team moves on. ACS already involved for Coca-Cola transition.

### 2026 KPIs `#process` `#visibility`
| Metric | Notes |
|---|---|
| Weekly customer interactions | Tracked in spreadsheet every Monday. Cumulative per-customer weekly touchpoints. |
| Number of experiments | Added "operational experiments" (simplify, scale, reduce cost) alongside customer-facing ones |
| Customer use | If no usage within a set period → throw it away |
| Made to product | Removed as KPI — forces shipping things without proven value. Let experiments organically graduate. |
| Knowledge sharing | Critical at high velocity. Team has 2 meetings/week specifically for sharing AI learnings. |

### Team size insights `#process`
- **Max ~4 people per workstream** for effective collaboration. Larger teams slow down dramatically, especially with AI-speed iteration.
- **Kanban over Scrum** — simple, transparent, no sprint ceremony overhead.
- When Coca-Cola onboarding brought in more people, the existing team pushed back: "Philippe, that doesn't work."

---

## Session 4: Experiment Dashboard Demo & Tooling Discussion

### Dashboard prototype `#tooling` `#visibility` [EXPLORING]
Inspired by Philipp's KPIs, a team member built a dashboard that:
- Accepts raw transcripts as input
- AI extracts potential experiments, learnings, and customer mentions
- Shows confidence percentages for each extraction
- Kanban board with explicit **Abandoned** column (with "why" captured)
- Goal: throw all meeting transcripts at it and auto-populate experiment tracking

### Tooling access — a recurring pain point `#tooling` `#process`
- **Cloudflare**: Team needs org-level access. Currently fragmented across personal accounts. Action item: get team added to Adobe Cloudflare org.
- **IMS authentication**: Needed for any tool handling customer data. Non-trivial setup (application config, group permissions).
- **Corporate tool procurement**: Too slow. ChatGPT took ~1.5 years to get official approval. "By the time it goes through, the next model is out."
- **Learning Fund**: $1,000/year per person available. Caveat: expenses through learning fund may be taxed as income (52% in Ireland, ~30% in Switzerland).
- **Paolo's directive** [DOING]: "Break the right rules." Using whatever technology helps is encouraged. Be creative. Manager support is there. Don't share customer data publicly — that's a rule you don't break.

### Shared tool access via coupons `#tooling`
Carlos shared access to a bundle including: ElevenLabs, Lovable, Manus, Railway, Drive, Whisper Flow. Team can share coupons for trying tools.

---

## Emerging Patterns

1. **Customer proximity is the #1 differentiator** — came up in every session. Direct practitioner feedback, not PM-filtered. Team's access to AEM customer base is the moat.
2. **Speed through AI tiers, not through hours** — consistent theme from Paolo's framing through Philipp's journey. The tier you're on determines your ceiling.
3. **Build → validate → abandon or graduate** — both teams (this one and Astra) converging on the same cycle. Kill things fast. Abandoning is not failure.
4. **Knowledge sharing is the bottleneck after speed** — Philipp and Paolo both flagged this. Auto-extracting learnings from transcripts is the answer both teams are pursuing.
5. **Tooling access is an organisational tax** — procurement, security, IMS setup all slow things down. Creative workarounds needed in the short term.
6. **"The code is immaterial"** — what you build today will be trivially reproducible soon. The value is in the customer relationship, the domain insight, and being first.

---

## Action Items

| Action | Owner | Status |
|---|---|---|
| Get team added to Adobe Cloudflare org | Paolo / super admin | Open |
| Share tool bundle coupons with team | Carlos | Open |
| Set up IMS authentication for dashboard | TBD | Open |
| Connect with Philipp's team on transcript→learnings automation | Paolo + Philipp | Open |
| Each person: define "what I want to get out of this week" | Everyone | For Day 2 roundtable |
| Explore AEM MCP server and published skills | Team | Open |
| Follow up with Netcentric (Angelo) on collaboration | Paolo | Open |

---

## Attribution Index

| Person | Key Contributions |
|---|---|
| **Paolo Mottadelli** | Workshop framing, 8 tiers model, "fast ≠ extra hours" convention, business context, hive mind video |
| **Philipp Koch** | Astra team journey, unlearn mindset, Coca-Cola case study, KPI framework, AI force multiplier timeline |
| **Carlos Sanchez** | Shared tool bundle access, remote participant |
| **Team member (dashboard)** | Built experiment tracking dashboard prototype, demonstrated transcript→experiment extraction |
| **Steven Yankee** | Author of the Anthropic Hive Mind article — referenced throughout |
| **Alex Koren** | Anthropic presenter at San Jose — shared Cowork origin story |

---

## Key Quotes

> "When we say fast, from now on, we don't mean extra hours." — **Paolo**

> "Unlearn was really one of the key areas." — **Philipp Koch**

> "Getting the unfiltered feedback and discussion with the customer is just one of the most wonderful gifts I've gotten." — **Philipp Koch**

> "The moment you share the idea, there's no separation between the idea and the code anymore." — **Team discussion**

> "We have access to our customers. The outer world doesn't have the same access. That's a huge differentiator." — **Team discussion**

> "Break the right rules, not the wrong ones." — **Paolo**
