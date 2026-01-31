# One AEM Workshop Highlights

> Directors+ workshop on becoming an AI-native organisation.
> Personal lens: how to transform my team to become 10X fast with AI.

---

## Top Insights

_Highest-priority ideas surfaced from the workshop. Flag with `!!` to promote here._

### !! 10X While Having Fun `#culture`
The goal of this transformation is not to burn harder. It's to work at a higher and higher level. We are ahead of the majority of the industry and above the company average -- that's the baseline, not the ceiling. The push forward should feel like fun, not pressure. The framing:
- Not more time or more effort -- **different ways of doing things, or not doing them at all**
- Everything we can delegate, we delegate -- to AI, to automation, to systems
- Psychological safety is non-negotiable: no danger of "doing the wrong thing" when experimenting
- The energy has to be sustainable -- this is a permanent shift, not a sprint

> **Why this is the #1 insight:** Every other idea in this document (agents, pipelines, pirates, overnight factories) could be read as "do more." This note reframes the entire agenda: **delegate more, think higher, enjoy the ride.** If the team feels burned by this transformation, it failed -- regardless of output.

### !! AI Evolution Framework: 4 Levels to AI Native Team `#culture` `#learning`
The maturity model that makes everything else measurable. Level 1 (AI User) → Level 2 (AI First) → Level 3 (AI Native Individual) → Level 4 (AI Native Team). Most of the team is at Level 1. Target: every individual at Level 3, team at Level 4. The critical insight: Level 4 is not "everyone is Level 3" -- it's shared infrastructure and culture that makes AI-native the default, even for new joiners. _(Full note: Category 4, Idea W)_

### !! "Be Pirates" `#culture`
Break the rules. Use what you need. Expense the tools. **Explicitly sanctioned across the organisation at director+ level.** This is the cultural unlock that makes everything else possible -- long-running agents, overnight factories, tool scouting, free experimentation. Without this permission, every other idea in this document hits a friction wall. With it, the team moves at the speed of the AI ecosystem itself. _(Full note: Category 4, Idea M)_

---

## 1. Ideas to Make the Team 10X Faster

_How we change the way we work, build, and deliver with AI._

### Core Principle: Automate Everything `#automation` `#culture`

**If a task can be delegated to AI, invest time to build it and share it as a working tool with the team.**

Ground rules:
- The crazier the idea, the better
- Implementation should be simple -- low effort, high leverage
- Must be usable by everyone, not just the builder

### Prototype Ideas

#### A) Ambient Screen Buddy `#automation` `#tooling` `#learning` [EXPLORING]
An always-on assistant that screenshots the user's screen every few seconds, silently reasons about what the user is doing, accumulates learnings over time, and proactively suggests faster ways to accomplish the task -- or offers to automate it entirely.

> **Connection:** This is the "observe, learn, suggest" loop. Over time it becomes a personalised productivity coach that knows your workflows.

#### B) Zero-Touch Meeting Pipeline `#automation` `#customer` `#process` [EXPLORING]
A team member joins a customer call. Meeting ends. No manual action required. In the background:
1. Transcript/summary is generated
2. Fed into a shared general context store
3. A pipeline distils: key learnings, data points (e.g. for the pancake chart), and candidate next actions/experiments

> **Connection:** Eliminates the "meeting notes tax" and ensures nothing falls through the cracks. Every customer conversation feeds the team's shared intelligence automatically.

#### C) Auto-Demo Generator for POCs `#automation` `#visibility` `#tooling` [EXPLORING]
Someone works on a POC for a week. The system inspects the code and produces a full demo package -- with no manual effort:
1. Analyse the code and generate a structured summary (technical steps, results, learnings)
2. Write a demo script from the summary
3. Record the screen walkthrough (Puppeteer)
4. Generate a talk track
5. Produce a voiceover (ElevenLabs API)
6. Post the 1-minute demo to Slack

> **Connection:** This solves the chronic "great work, nobody saw it" problem. Every POC gets visibility by default. Also forces clarity -- if the system can explain it, the work is well-structured.

#### D) Feedback-to-Fix Pipeline `#automation` `#customer` `#process` [EXPLORING]
User feedback from relevant Slack channels is continuously ingested:
1. Raw feedback is acquired into context
2. Compacted into structured data (themes, severity, frequency)
3. Each item is classified as a **fix** or an **idea**
4. For each: the system opens a branch in the correct repo, generates the change in a PR, and sends a Slack message to the right person to test and review

> **Connection:** Closes the loop from customer voice to shipped code with minimal human intervention. The human role shifts from "do the work" to "review and approve."

#### E) Self-Improving Feedback Loop `#automation` `#learning` [EXPLORING]
Each of the tools above should report back on whether its output was useful. Did the user act on the Buddy's suggestion? Was the PR merged or closed? Was the demo shared further? This lightweight signal feeds back into the system so it learns what's valuable and stops producing noise.

> **Why it matters:** Without this, the tools degrade into notification spam. With it, they compound in quality over time.

#### F) Shared Automation Library ("The Cookbook") `#tooling` `#culture` `#visibility` [EXPLORING]
Every automation a team member builds gets published to an internal catalog -- a simple repo or Slack-integrated index with: what it does, how to trigger it, and a 30-second video. Lowers the barrier from "I built a cool thing" to "everyone uses it by Monday."

> **Why it matters:** The principle says "share it as a working tool with others." This is the mechanism that makes sharing frictionless and discoverable.

#### G) AI Standup / Async Status Harvester `#automation` `#process` `#visibility` [EXPLORING]
Instead of people writing status updates, the system pulls signals from Git activity, PR status, Slack threads, and Jira/ticket movement. It composes a per-person and per-team summary daily. Humans review and annotate only if something is wrong.

> **Connection to B & C:** Same "capture and summarise" pattern, applied to internal work visibility instead of customer meetings or POCs.

#### H) Prompt & Workflow Shadowing `#learning` `#culture` `#automation` [EXPLORING]
When someone on the team finds an effective AI workflow (a prompt chain, a Claude Code pattern, a shortcut), the system captures it and proposes it to others in similar contexts. Like the Screen Buddy (A), but for AI usage itself -- the team's collective AI skill rises automatically.

> **Connection to A:** The Buddy watches how you work with your tools. This watches how you work with AI. Together they cover the full surface.

### Pattern Across All Ideas

All ideas share the same architecture:
```
Trigger (passive) --> Capture --> Process/Reason --> Produce Artifact --> Distribute
```
No manual trigger. No manual formatting. No manual distribution. The human stays in the creative/decision layer; the system handles everything else.

---

## 2. Vision for the Product

_Where AEM is headed and how AI reshapes the product itself._

### The Experience Gap: Discovery vs. Brand

#### P) "Disneylandification" of the Brand Experience `#product` `#customer` [STRONG]
There are two worlds: **discovery** (outside the brand -- search, social, generic chat) and **brand experience** (inside the brand's owned surface). The unbranded chat experience is generic. The brand experience must delight. Users entering the brand expect Disneyland, not a search bar.

What this means concretely:
- **More actionable** -- the brand experience should feel like an app, not a brochure. Users do things, not just read things.
- **Trust signals** -- find and surface the signals that actually change user behaviour. Not generic badges, but context-aware proof points that matter to *this* user at *this* moment.
- **Meaningful events** -- track events related to the user that are useful to build context. Context is the raw material for exceptional experience. Without it, personalisation is guesswork.

> **-- Loni**

> **Connection to B (Meeting Pipeline) & D (Feedback Pipeline):** The "meaningful events" concept mirrors the team-internal pattern of capturing signals passively and processing them into intelligence. Loni is describing the same architecture applied to the *end user*: capture events --> build context --> deliver personalised experience. The pipeline pattern from Category 1 is also the product architecture.

> **Connection to O (Sustainable Fun):** "Disneylandification" is the product equivalent of "10X while having fun." The user should feel delighted, not overwhelmed. The team should feel the same way about building it.

> **Suggestion:** "Meaningful events" is the concept to unpack. What counts as meaningful? Some candidates: purchase history, content engagement patterns, support interactions, lifecycle stage, expressed preferences vs. revealed preferences. The research question is which events actually move the needle on experience quality -- and which are noise. This is testable.

### Speed & Usage as North Star

#### Q) "Are We Moving Fast Enough?" `#product` `#process` [STRONG]
We are doing the right things. The question is speed. The first key objective is **usage**: track it and maximise it everywhere, as much as possible. Usage is the leading indicator of value, adoption, and retention. If people aren't using it, nothing else matters.

> **-- Amit (Product SVP)**

> **Connection to D (Feedback-to-Fix Pipeline):** Usage data is the richest feedback channel. If the Feedback-to-Fix pipeline (D) ingests usage telemetry alongside Slack feedback, it can auto-detect drop-off points and generate fixes before anyone files a complaint.

> **Connection to Category 4 (Frontier Engineers):** "Moving fast enough" is exactly what the overnight factory (J), long-running agents (I), and pirate culture (M) are designed to solve on the engineering side. Amit's challenge to the product is the same challenge the team is answering with AI tooling.

> **Suggestion:** Define a usage dashboard that the team checks weekly -- not monthly. Make it the first slide in every standup or review. If the team builds the AI Standup Harvester (G), usage metrics should be auto-included in the daily summary.

#### Q2) The Lighthouse Customer `#product` `#customer` [STRONG]
Key goal for this year: have a customer who can say **"I have embarked with Adobe on this agentic evolution, and this is the value I'm getting."** Not a case study written by marketing -- a customer who believes it and says it unprompted.

> **-- Amit (Product SVP)**

> **Connection to Q:** Usage is the precondition. You can't have a lighthouse customer who doesn't use the product heavily. Usage --> value realisation --> advocacy.

> **Connection to B (Meeting Pipeline):** Every customer conversation is a chance to detect whether someone is on the path to becoming this lighthouse. The meeting pipeline should flag: "This customer is showing lighthouse signals" -- high engagement, positive sentiment, expanding use cases.

> **Tension:** A lighthouse customer requires deep partnership, not just a good product. Someone on the team (or across teams) needs to own that relationship end-to-end. This is a candidate for an action item with a named owner.

### Design as Differentiator

#### R) Beautiful Design as Migration Lever `#product` `#customer` [EXPLORING]
When customers migrate to AEM, what if the output is not just functionally equivalent but *visually better*? Turn migration from a cost-of-switching conversation into a value-add conversation: "Your old site worked. Your new site is beautiful."

Research area: how to generate designs that are both beautiful and aligned with the brand's identity. This is an AI-native design problem -- the system needs to understand brand guidelines, apply them creatively, and produce output that a human designer would be proud of.

> **Connection to P (Disneylandification):** Loni's vision of the brand experience as Disneyland starts with how it looks. If the migration tool produces generic designs, the Disneyland promise breaks on day one. Beautiful, brand-aligned design is the first trust signal.

> **Connection to K (Tool Scouting):** This is a prime scouting target. AI design generation is evolving fast (Midjourney, Figma AI, Vercel v0, etc.). The scout role (K) should be tracking this space continuously and feeding findings back to whoever owns this research.

> **Suggestion:** Prototype this with a single customer migration. Take their existing site, run it through an AI design pipeline, and compare the output side by side. If the result is compelling, you have a demo that sells itself -- and it becomes a lighthouse story (Q2).

---

## 4. Becoming AI Frontier Engineers

_Pushing the technical and cultural boundaries of what's possible with AI as a daily engineering practice._

### Technical Boundaries to Explore

#### I) Long-Running Autonomous Agents `#tooling` `#automation` [EXPLORING]
How long can we sustain a single agent session? Can we hand an agent a task that takes hours -- or an entire workday -- and have it deliver a finished result? This is about testing the limits of agent endurance: context management, error recovery, self-correction over extended runs.

> **Connection to C:** The Auto-Demo Generator already implies multi-step agent work. This pushes the question further -- what if the agent doesn't just summarise, but *builds the whole thing*? The constraint isn't the AI's capability, it's our ability to define the task clearly enough for a long autonomous run.

> **Suggestion:** Start with a benchmark: give an agent a well-scoped task (e.g. "build a working integration test suite for module X") and measure how far it gets in 1h, 4h, 8h. Map the failure modes. That data tells you where to invest in better scaffolding.

#### J) Overnight Idea Factory `#automation` `#process` `#learning` [STRONG]
The system generates ideas automatically, lists them in a backlog, and implements them overnight. Multiple agents try different approaches to the same idea, criticise each other's results, and elect winners. The engineer arrives in the morning to a set of ranked, working prototypes ready for review.

This turns sleep into productive time. A team of 10 engineers effectively becomes a team of 10 engineers + N overnight agents. The number of experiments the team can run increases **100X**.

> **Connection to Cat.1 pattern:** This is the `Trigger --> Capture --> Process --> Artifact --> Distribute` pipeline on steroids. The trigger is "end of workday." The artifact is working code.

> **Connection to E (feedback loop):** The morning review becomes the feedback signal. Which overnight results get picked up? That trains the system on what "good" looks like for this team.

> **Suggestion:** The critical design choice is the idea queue. Where do ideas come from? Options: manually seeded, extracted from Slack/meetings (ties to B), generated by analysing gaps in test coverage or customer feedback (ties to D). The richer the input funnel, the more valuable the overnight runs.

#### K) Continuous AI Tool Scouting `#tooling` `#learning` [STRONG]
Experiment with AI tools continuously -- not as a one-off evaluation, but as an ongoing practice. The purpose is twofold: (1) discover new capabilities that inspire ideas, and (2) find tools that make existing ideas faster to implement by leveraging what already exists.

> **Connection to H (Workflow Shadowing):** When someone discovers a powerful tool, Shadowing captures and propagates it. Scouting is the upstream activity that feeds the discovery pipeline.

> **Suggestion:** Assign a rotating "scout" role -- each sprint, one person spends a fixed block of time trying new tools and reports back. Low overhead, high serendipity. The Cookbook (F) is where findings get published.

### Cultural Boundaries to Break

#### L) Permission to Experiment Freely `#culture` `#learning` [STRONG]
Everyone on the team has explicit permission to spend time on whatever experiment they have in mind -- even personal ideas. The only obligation: report back to the team what you learned. With the Auto-Demo Generator (C), even that obligation is automated. You experiment, the system tells the story.

> **Connection to C:** This is the cultural policy that makes the Auto-Demo Generator essential. Without (C), the "report back" requirement becomes a tax that kills experimentation. With (C), experimentation is frictionless end-to-end.

> **Tension:** "Whatever experiment" is deliberately broad. The risk is diffusion -- people optimise for personal interest over team leverage. The mitigating design: the Cookbook (F) and overnight factory (J) create natural gravity toward ideas that compound for the team.

#### M) "Be Pirates" `#culture` [STRONG]
Break the rules. Use what you need. Leverage the education fund to expense subscriptions to tools that make you faster. Don't ask for a procurement cycle -- just do it. **This was explicitly sanctioned across the organisation at the workshop level.**

> **Why this matters enormously:** Most "innovation culture" initiatives fail because the permission is implicit. This one is explicit, named, and endorsed by directors+. "Be pirates" is a cultural licence that removes the #1 blocker to experimentation: fear of getting in trouble.

> **Connection to K (Tool Scouting):** Pirates + education fund + scouting mandate = the team can move at the speed of the AI ecosystem itself. No waiting for enterprise procurement to evaluate a tool for 6 months.

> **Suggestion:** Make the pirate stories visible. When someone breaks a rule and it pays off, celebrate it loudly (Slack, demos, retros). That reinforces the permission and gives others courage. When it doesn't pay off, celebrate the learning. Both outcomes compound.

#### N) Parallel Innovation & Internal Competition `#culture` `#process` [STRONG]
Different teams may build similar things in parallel -- and that's not waste, it's expected. At some point one version gets promoted and ships. The others aren't failures; they're exploration that informed the winner.

**Case study from Anthropic (Alex Koren):** His team was working on something similar to what became Cowork. Then Cowork was built and shipped in 10 days over the Christmas holidays. His team's parallel work wasn't lost -- it was part of the broader exploration that made the winning version possible.

The principles:
- **Embrace competition** -- parallel efforts sharpen ideas, not dilute them
- **Share continuously** -- so parallel tracks cross-pollinate instead of diverging in silence
- **Finalise milestones** -- at some point, converge. Pick a winner and ship it.
- **Continuously innovate** -- the "losing" team doesn't stop. They take their learnings and start the next thing.

> **Connection to J (Overnight Factory):** The overnight factory is this principle on autopilot. Multiple agents try multiple approaches, criticise results, elect winners. What Anthropic does across teams over weeks, agents can do overnight.

> **Connection to L & M (Permission + Pirates):** This only works if people aren't punished for building something that doesn't get picked. "Be pirates" protects the parallel explorers. Without that cultural safety, people wait for consensus before starting -- and the 10-day sprint that ships Cowork never happens.

> **Tension:** There's a real cost to duplication. The mitigation is the "share continuously" part. If teams are transparent about what they're building (Cookbook F, async status G), parallel work converges faster and cross-pollinates. Silent duplication is waste. Visible duplication is evolution.

> **Suggestion:** For your team specifically, this reframes how you handle overlap with other AEM teams. Don't coordinate to avoid overlap. Coordinate to stay visible while you overlap. The best version wins, and the losers are just early drafts of the next winner.

#### O) Sustainable Intensity: 10X While Having Fun `#culture` `#learning` [STRONG]
We are already outperforming the industry and the company average. The next leap isn't about adding hours or pressure -- it's about fundamentally changing what humans spend their energy on. Delegate the grind. Keep the creative, strategic, high-judgment work. Make the transformation feel like play, not survival.

Three pillars:
1. **Challenge what we do** -- question every task. Can it be done differently? Can it be eliminated? Can an agent do it?
2. **Psychological safety** -- experimenting with new ways of working can't carry the risk of "doing the wrong thing." Safe to try, safe to fail.
3. **Sustainable energy** -- this isn't a hack week. It's a permanent operating model. If it drains people, it's broken.

> **Connection to M (Be Pirates):** "Be pirates" gives permission to break rules. This note adds the emotional contract: the goal is joy and elevation, not extraction. Pirates have fun -- that's the point.

> **Connection to L (Permission to Experiment):** Free experimentation works only if people don't feel guilty about the time. This note removes that guilt by redefining what "productive" means: working at a higher level IS the output.

> **Tension with J (Overnight Factory):** The overnight factory multiplies throughput. But if the morning review becomes an obligation that feels like checking homework, it backfires. The design has to make the morning review feel like opening presents, not processing a queue.

> **Suggestion:** At Feb 9, make this the opening frame. Before any tools, pipelines, or agents -- set the tone: "We're going to become 10X faster, and it's going to be more fun, not less. Here's why." Every subsequent exercise gets filtered through this lens.

### The New Engineering Role

#### S) Engineers as Managers of Agents `#culture` `#process` `#learning` [STRONG]
The frontier engineer's job shifts upward. More high-level thinking: **design, plan, verify.** Less low-level coding -- potentially zero coding. The engineer becomes a manager of agents: give instructions, monitor direction, verify results.

This is a *harder* job, not an easier one. Writing code is a well-understood skill. Decomposing a problem into agent-executable tasks, choosing the right delegation strategy, spotting when an agent is going off-track, and verifying output quality at speed -- these are new muscles that need deliberate training.

The progression:
1. **Today:** Engineer writes code, AI assists
2. **Next:** Engineer designs and plans, AI writes code, engineer verifies
3. **Frontier:** Engineer orchestrates a team of agents -- an orchestrator agent decomposes work, execution agents implement in parallel, engineer reviews and steers

#### The Agent Management Stack
```
Engineer (design, plan, judge)
    └── Orchestrator Agent (decompose, assign, coordinate)
            ├── Execution Agent A (implement approach 1)
            ├── Execution Agent B (implement approach 2)
            ├── Critic Agent (evaluate outputs, rank results)
            └── ...
```

> **Connection to I (Long-Running Agents):** This is the natural evolution. A single long-running agent is step one. An orchestrator managing multiple execution agents running for hours is the endgame. The long-running agent benchmark (I) is training wheels for this.

> **Connection to J (Overnight Factory):** The overnight factory IS this architecture running unsupervised. The engineer seeds the orchestrator before leaving, and the agent team works through the night. What makes it "overnight" is just that the engineer isn't monitoring.

> **Connection to O (10X While Having Fun):** This reframe is critical for morale. "You're not being replaced by AI. You're being promoted. Your job is now harder and more interesting -- you're managing a team of tireless, fast, imperfect agents." That's an exciting pitch, not a threatening one.

> **Tension:** This requires a real skill shift, and not everyone will find it natural. Some engineers love being in the code. Telling them "you don't code anymore, you manage agents" could feel like a loss. The framing matters: it's an *additional* capability, not a replacement of identity. And the best agent managers will be people who deeply understand code -- you can't verify what you don't understand.

> **Suggestion:** This is the single most trainable skill in the document. Build a training progression:
> 1. **Level 1:** Use AI to write a function. Review and ship.
> 2. **Level 2:** Give an agent a full task (feature, bugfix). Review the PR.
> 3. **Level 3:** Run an agent for hours on a complex task. Monitor, redirect, accept.
> 4. **Level 4:** Orchestrate multiple agents on related tasks. Manage the orchestrator.
> 5. **Level 5:** Design the system that generates and assigns tasks to agents autonomously.
>
> Each level is a workshop exercise for Feb 9.

### Insights from Cursor PM

#### T) "Applied Research Team" Identity `#culture` `#process` `#learning` [STRONG]
Cursor sees themselves as an **applied research team**: they research how to improve their own job, then ship the results as product. Research and product are the same loop. This is directly applicable to our team -- we can adopt the same identity.

What this means in practice:
- Every workflow improvement the team builds for itself is a candidate for the product
- The team's internal pain points are product research signals
- "Dogfooding" isn't a side activity -- it's the core R&D methodology

> **-- Cursor PM**

> **Connection to A-H (Prototype Ideas):** Every automation tool the team builds (Screen Buddy, Meeting Pipeline, Auto-Demo, etc.) is applied research. The team is researching "how do AI-native engineers work?" and shipping the answers. Some of those answers may literally become product features -- or at minimum inform what AEM's customers need.

> **Connection to F (The Cookbook):** The Cookbook becomes the team's research output log. It's not just an internal tool catalog -- it's a record of applied research findings. Reframe it that way and it gains weight and purpose.

> **Suggestion:** Adopt the label explicitly. Call the team (or a track within it) an "applied research team." Language shapes identity. When someone builds an internal automation, they're not doing a side project -- they're doing applied research. That reframe changes how the work is valued, reported, and funded.

#### U) "Cover More Ground, With Less" -- Team Recomposition `#process` `#culture` [STRONG]

The traditional team structure:
```
Before:  1 PM + 1 Design + 8 SWEs = 10 people, one initiative
After:   1 PM + 1 Design + 4 crews of 2 SWEs = same people, 4x the initiatives
```

The same headcount, radically different topology. Instead of 10 people working on one thing with heavy coordination, **the team fans out into 1-2 person crews, each covering an independent track.** PM and Design float across all crews, providing direction and quality -- not managing tickets.

Each crew owns a problem end-to-end. Agents handle the execution volume that previously required more people. The team covers **a lot more ground, with less per-track headcount.**

Consequence: **managers and PMs become less relevant** in the traditional coordination role. If the unit of work is 1-2 people + agents, there's less to coordinate. The value shifts from "keeping people aligned" to "setting direction and removing blockers."

> **-- Cursor PM**

> **Connection to S (Engineers as Agent Managers):** This is the organisational structure that matches the agent management stack. The engineer IS the manager -- of agents, not of people. The team shrinks in headcount per initiative but explodes in throughput.

> **Connection to G (Async Status Harvester):** With 4 parallel crews, no standup can cover everything. The harvester (G) becomes essential infrastructure -- it's how PM and Design maintain situational awareness without bottlenecking every crew.

> **Tension:** This is the most politically charged idea in the document. "Managers and PMs become less relevant" will not land well if said bluntly. The reframe: their role evolves from coordination to **strategy, direction-setting, and quality judgment**. The people who were good at coordination become good at something harder. Same pattern as engineers moving up from coding to agent management.

> **Tension #2:** 1-2 person crews can become silos. The mitigation is aggressive visibility: Cookbook (F), Async Status (G), Parallel Innovation norm (N). The crews are small but transparent.

#### V) Tasks Become Shorter, More Frequent, and Parallel `#process` `#automation` `#tooling` [STRONG]

The unit of work changes shape:

```
Before:  SWE ──────── Task ──────────────────────────────────>
         (1 person, 1 long task, sequential)

After:   SWE ── Task ──  ── Task ──  ── Task ──  ── Task ──
              ── Task ──  ── Task ──  ── Task ──  ── Task ──
              ── Task ──  ── Task ──  ── Task ──  ── Task ──
         (1 person, many short tasks, parallel via agents)
```

Each engineer runs **many short tasks in parallel** instead of one long task sequentially. Each task is a small, well-scoped unit delegated to an agent. The engineer's job is to keep the fleet loaded: define the next task before the current one finishes.

This is the micro-level manifestation of the team recomposition (U). The team fans out into crews; within each crew, the individual fans out into parallel agent tasks. **Parallelism at every layer.**

> **-- Cursor PM**

> **Connection to X (Boris Cherny):** Boris's 300 PRs/month is this principle in action. Each PR is a short, scoped task. 10-15 concurrent sessions = massive task parallelism from one person.

> **Connection to V-as-principle (Multi-Agent Default):** Multi-agent is the mechanism. Short parallel tasks are the outcome. The design question isn't "how long is this task?" but "how many parallel tasks can I decompose this into?"

> **Connection to J (Overnight Factory):** During the day, the engineer runs parallel tasks and monitors. At night, the factory continues the same pattern unattended. The throughput becomes continuous.

> **Connection to I (Long-Running Agents):** There's a spectrum. Some tasks are short (minutes). Some need long runs (hours). The engineer manages both: short tasks for quick wins, long tasks for deep problems, all running concurrently.

> **Suggestion:** Track a new metric: **tasks-in-flight per engineer.** Today it's probably 1. Boris is at 10-15. The framework target for Level 3 should include a tasks-in-flight minimum -- it's a concrete, measurable proxy for AI-native work.

### Case Study: Boris Cherny -- 300 PRs in December

#### X) What Level 3 Looks Like in Practice `#tooling` `#automation` `#learning` [STRONG]

Boris Cherny (Anthropic) shipped **>300 PRs in December** -- a personal record -- without working long hours. This is a concrete example of what an AI Native individual (Level 3) produces. His method:

1. **5 Claude Code terminals in parallel** on his machine, plus 5-10 browser sessions (~10-15 concurrent agents)
2. **Blanket Bash permissions** on each terminal so agents never block on approval (unsafe, he admits -- but eliminates the human bottleneck)
3. **Plan-first for every session**: turn on plan mode, iterate with Claude until the plan is solid, *then* switch to execution with auto-accept
4. **Auto-ship pipeline**: instructed each agent to run `/commit-push-pr` when done, with auto-enable merge
5. **3 GitHub workflows** to shepherd each PR to production: automated CI, review, and merge

The human role: **design the plan, verify the output, manage the fleet.** The agents do the coding, committing, and shipping.

Key practices from [detailed workflow analysis](https://karozieminski.substack.com/p/boris-cherny-claude-code-workflow):
- **Quality over speed**: Uses Opus with thinking enabled despite being slower -- reduces the "correction tax" of fixing bad output
- **Institutional memory**: Shared `CLAUDE.md` checked into git, documenting mistakes so agents don't repeat them
- **Verification loops**: Having Claude test its own changes and iterate until working -- "probably the most important thing"
- **Systems thinking**: The question isn't "how do I get better outputs?" but **"how do I build a system where AI reliably produces what I need?"**

> **Connection to W (AI Maturity Framework):** Boris is a textbook Level 3 individual. He has restructured his entire workflow around AI as infrastructure. This is the reference implementation for what the team is aiming at.

> **Connection to V (Multi-Agent Default):** 10-15 concurrent sessions IS multi-agent as default. He doesn't run one agent and wait. He runs a fleet. This validates the principle with hard numbers: 300 PRs/month.

> **Connection to S (Agent Management Stack):** Boris's workflow is the agent management stack made real. He designs plans (orchestrator role), agents execute in parallel, GitHub workflows handle the last mile. He is managing agents, not writing code.

> **Connection to J (Overnight Factory):** Boris runs his fleet during the day. Combine his approach with the overnight factory and you have agents shipping PRs 24 hours a day.

> **Connection to M (Be Pirates):** "Blanket Bash permissions -- unsafe, I know!" This is pirate behaviour. He traded safety rails for throughput because he trusts his verification loop. The team needs permission to make that trade.

> **Tension:** The "blanket permissions" approach has real risk. One rogue agent command could cause damage. The mitigation is the plan-first discipline: by the time execution starts, the agent is working within a well-defined scope. Still, this is a trade-off each person should make consciously, not blindly.

> **Feb 9 angle:** This is the most powerful demo for the workshop. Show Boris's numbers. Show the workflow. Then ask: "What would YOUR version of this look like? What's stopping you from running 5 agents in parallel tomorrow?"

### AI Evolution Framework (Assessment Model)

#### W) The Four Levels of AI Maturity `#culture` `#learning` `#process` [DOING]

Shared by Alex Koren. A framework to assess where individuals and teams sit on the AI adoption curve:

| Level | Name | Description | Where we are |
|-------|------|-------------|--------------|
| **1** | **AI User** | Uses AI as a tool -- autocomplete, Q&A, occasional code generation. Most engineers in the industry are here. | Most of the team |
| **2** | **AI First** | AI is the first option for the majority of tasks. The engineer reaches for AI before reaching for the keyboard. A few people on the team are here. | A few individuals |
| **3** | **AI Native (Individual)** | The engineer has restructured their entire workflow around AI as a structural framework. Not just using AI more -- working in a fundamentally different way. Designing, planning, orchestrating agents, verifying. | 1-2 people |
| **4** | **AI Native (Team)** | The whole team operates as AI-native. Shared tooling, shared norms, shared context infrastructure. The team's output is structurally impossible without AI. | **Target** |

**The goal: every individual at Level 3, the team at Level 4.**

#### What Changes at Each Level

```
Level 1 → 2:  Frequency.     AI goes from "sometimes" to "default first action"
Level 2 → 3:  Structure.     Workflows rebuilt around AI, not AI bolted onto old workflows
Level 3 → 4:  Collective.    Shared infrastructure, norms, and culture make the team
                              more than the sum of AI-native individuals
```

> **-- Alex Koren (Anthropic)**

> **Connection to S (Engineers as Agent Managers):** The Level 1→3 progression maps directly to the agent management training levels. Level 1 = AI assists your coding. Level 2 = AI does most coding, you review. Level 3 = you orchestrate agents, you don't code. The training progression in (S) is the how. This framework is the what.

> **Connection to O (10X While Having Fun):** The jump from Level 2 to 3 is the hardest -- it requires letting go of old workflows, not just adding AI on top. That's where psychological safety (O) matters most. People need permission to be bad at the new way before they're good at it.

> **Connection to U (1-2 Person Crews):** Level 4 (AI Native Team) is what makes 1-2 person crews viable. Without shared infrastructure and norms, small crews are just individuals working alone. Level 4 = the shared fabric that connects the crews.

> **Connection to T (Applied Research):** The jump from Level 3 to Level 4 is a research problem. Nobody has a playbook for "AI Native Team." Your team figures it out by doing it -- and that's applied research.

#### The Level 3 → Level 4 Gap

Getting individuals to Level 3 is a training problem. Getting the team to Level 4 is a **systems problem**. It requires:

- **Shared tooling**: The Cookbook (F), pipelines (B, D), status harvester (G)
- **Shared norms**: Multi-agent as default (V), be pirates (M), parallel innovation (N)
- **Shared context**: General context store (from B), feedback loops (E)
- **Shared identity**: Applied research team (T), explicit permission (L)

Level 4 is not "everyone is Level 3." Level 4 is "the team has infrastructure and culture that makes AI-native output the default, even for someone who just joined."

> **Suggestion:** Use this framework as the backbone of the Feb 9 workshop. Open with self-assessment: "Where are you? Where do you want to be by mid-year? By end of year?" Then map every workshop exercise to a level transition. The roundtable stretch goals (Category 3) become level-jump commitments.

> **Suggestion:** Define observable signals for each level so assessment isn't subjective:
> - **Level 1 signals**: Uses Copilot/Claude for individual tasks, still writes most code manually
> - **Level 2 signals**: Starts most tasks by prompting AI, rarely writes boilerplate, uses AI for code review
> - **Level 3 signals**: Has custom agent workflows, runs multi-step agents autonomously, designs tasks for agent execution, measures AI throughput
> - **Level 4 signals**: Team shares agent configurations, has automated pipelines (B-D-G), new member reaches Level 2 within a week because the infrastructure carries them

### Pattern Across Category 4

Five layers:
```
Technical:       Push agent duration + parallelism --> multiply experiment throughput 100X
Cultural:        Give explicit permission + remove friction --> multiply willingness to try
Emotional:       Make it fun + sustainable + safe --> multiply longevity of the transformation
Skill shift:     Train engineers to design/plan/verify instead of code --> unlock the agent workforce
Organisational:  Shrink teams to 1-2 person crews + agents --> remove coordination overhead
```
No single layer works alone. Agents without permission = shelfware. Permission without agents = slow ambition. Either without fun = burnout. Agents without skilled managers = chaos. Small crews without visibility = silos. **The 10X (or 100X) comes from all five.**

---

## 3. Ideas for My Team Workshop (Feb 9)

_Concrete activities, formats, and topics to bring back to my team._

### Team Culture Model: Anthropic as Starting Point `#culture` `#feb9` [DOING]

Anthropic shared their 5 culture pillars. We'll use these as a model for our team -- discuss which apply, adapt them, and identify what's missing for us.

#### Anthropic's Culture Pillars

| # | Pillar | Their Definition | How It Maps to Our Ideas | For Us? |
|---|--------|-----------------|--------------------------|---------|
| 1 | **AI-First** | Try to answer your own questions first. | Directly maps to Level 2 in the maturity framework (W). Before asking a colleague, before Googling -- ask AI. This is the entry-level habit that unlocks everything else. | **Adopt as-is.** The simplest, most immediate culture shift. |
| 2 | **Push Boundaries** | Every task you have is an opportunity to use AI. | Maps to "Be Pirates" (M) and Permission to Experiment (L). Not just using AI where it's obvious, but probing every task for AI leverage -- even the ones that seem impossible. | **Adopt and amplify.** We already have the pirate mandate. This adds the daily discipline. |
| 3 | **Write & Share** | When you learn something, share it with others. | Maps directly to the Cookbook (F), Prompt Shadowing (H), and the Applied Research identity (T). Learning that stays with one person is waste. Learning that's shared is a team multiplier. | **Adopt and systematise.** We have the tools (F, H). This is the norm that makes people use them. |
| 4 | **Fail Fast** | It won't all work, but it's worth a try. | Maps to Parallel Innovation (N), Permission to Experiment (L), and the "crazy ideas" principle. The cost of trying has collapsed with AI. The cost of not trying is falling behind. | **Adopt as-is.** Reinforce with the Overnight Factory (J) -- failing fast is even cheaper when agents do the failing. |
| 5 | **Stay Skeptical** | Challenge AI to ensure the best outputs. | Maps to the verification role in Engineers as Agent Managers (S). AI-first doesn't mean AI-trusting. The harder you lean on AI, the sharper your judgment needs to be. This is what makes the "agent manager" job harder, not easier. | **Adopt and emphasise.** This is the counterweight to all the "go fast" culture. Without skepticism, speed produces garbage at scale. |

#### What's Missing for Us?

Anthropic's 5 pillars are oriented around **individual practice** -- how one person works with AI. For a team aiming at Level 4 (AI Native Team), we need additional pillars that address the **collective layer**:

| # | Proposed Addition | Why It's Missing | Source |
|---|-------------------|-----------------|--------|
| 6 | **Build for the Team** | Anthropic's "Write & Share" covers knowledge. But we also need to share *working tools*. When you automate something, package it for others. | Cookbook (F), Core Principle |
| 7 | **Make It Visible** | Sharing knowledge is opt-in. Visibility should be opt-out. Work, results, experiments -- visible by default, not by effort. | Async Status (G), Auto-Demo (C), Parallel Innovation (N) |
| 8 | **Have Fun Doing It** | Anthropic's pillars are about effectiveness. Ours need to include sustainability. The transformation should feel like play, not pressure. | 10X While Having Fun (O) |
| 9 | **Elevate, Don't Grind** | Delegate everything you can. Spend your time at the highest level of thinking you're capable of. If you're doing something an agent could do, stop and delegate. | Engineers as Agent Managers (S), Core Principle |

> **Connection to W (Maturity Framework):** Pillars 1-5 (Anthropic's) get individuals to Level 3. Pillars 6-9 (our additions) get the team to Level 4. The distinction maps cleanly.

> **Connection to O (10X While Having Fun):** Pillar 8 is the one Anthropic doesn't have. For a company building AI, the fun might be assumed. For a team transforming to become AI-native inside a large enterprise, it needs to be explicit.

> **Feb 9 plan:** Present the 5 Anthropic pillars. Discuss each: does it apply? Then reveal the 4 proposed additions. Debate, refine, adopt. The team leaves Feb 9 with their own culture manifesto -- co-created, not imposed.

### Closing Roundtable: Two Sentences That Matter `#culture` `#learning` `#feb9` [DOING]

End the intro day with a roundtable where every person shares exactly two sentences:

1. **"My next-level focus"** -- What is the one thing you want to focus on first to get to the next level of AI fluency?
2. **"My stretch goal"** -- What is the one thing you want to have done by the end of the year? _(Must be a stretch -- if it doesn't scare you a little, aim higher.)_

Format:
- Everyone speaks. No skipping.
- One sentence each. No preamble, no hedging.
- Capture all responses live (or auto-capture with the meeting pipeline, B).
- Post the collected commitments to Slack the next day as a public artifact.

> **Why this works:** It forces commitment through specificity. "I want to get better at AI" means nothing. "I want to have an autonomous agent running my test suite by December" is a stretch goal that can be tracked, supported, and celebrated.

> **Connection to O (10X While Having Fun):** The stretch goal should excite, not terrify. Frame it as: "What would make you proud to demo at next year's workshop?"

> **Connection to Q2 (Lighthouse Customer):** Some stretch goals may naturally align with the lighthouse customer ambition. If someone's stretch is "I want a customer using my feature in production with AI agents" -- that's a lighthouse candidate surfacing from the team itself.

> **Connection to E (Feedback Loop) & C (Auto-Demo):** These commitments become the feedback signal for the year. Revisit them quarterly. The Auto-Demo Generator (C) can auto-produce progress updates against each person's stated goal.

> **Suggestion:** Collect the responses into a "Team Commitments 2025" page. Revisit at mid-year and end-of-year. Make the stretch goals visible -- they become the team's collective ambition, not just individual aspirations. When someone hits their stretch goal, celebrate it loudly.

---

## Emerging Patterns

_Cross-cutting themes that recur across categories._

| Pattern | Where it shows up | Implication |
|---|---|---|
| Passive trigger, zero manual action | A, B, C, D, G, J | The 10X gain comes from removing human-as-glue, not from making humans faster |
| Capture-and-summarise as a primitive | B, C, G | This is the foundational building block -- build it once, reuse everywhere |
| Sharing by default | C, F, H, L | Visibility is not a nice-to-have, it's the multiplier that turns individual work into team leverage |
| Self-improving systems | E, H, J | Without feedback loops, AI tools plateau. With them, they compound. |
| Technical ceiling x Cultural permission | I+L, J+M, K+M | Neither layer works alone. Capability without permission = shelfware. Permission without capability = slow ambition. |
| Time multiplication | J, I | Agents work while humans sleep or context-switch. The workday expands without expanding hours. |
| Explicit over implicit permission | L, M | "Be pirates" works because it's named and endorsed at director+ level. Most innovation culture fails because the permission stays vague. |
| Parallel exploration > consensus-first | N, J | Duplication isn't waste if it's visible. The winning version emerges from competition, not from committee. |
| Elevation, not extraction | O, L, M, S | The transformation succeeds only if people feel they're working at a higher level, not a harder one. Fun is the leading indicator. |
| Engineer as agent manager | S, I, J, V | The job shifts from writing code to orchestrating agents. Harder, higher-level, and trainable -- but requires deliberate skill-building. |
| Internal practice = product research | T, A-H | Every tool the team builds for itself is applied research. The Cookbook (F) is the research output log. |
| Small crews + aggressive visibility | U, G, F, N | 1-2 person crews replace 10-person teams, but only work if transparency infrastructure (G, F) prevents silos. |
| Multi-agent as default | V, S, J, I | Single-agent is the exception. Every task should assume parallel agents unless proven otherwise. |
| Level 3→4 is a systems problem, not a training problem | W, F, G, B, E, T | Individual skill gets you to Level 3. Shared infra, norms, and identity get the team to Level 4. |
| Anthropic's 5 pillars = individual; our 4 additions = collective | Culture model | The gap between Anthropic's culture and ours reveals the Level 3→4 gap: they optimise the individual, we need to also optimise the team. |
| Context is the product | P, B, D | Internally: capture signals to build team intelligence. Externally: capture user events to build experience intelligence. Same architecture, different audience. |
| Usage as leading indicator | Q, Q2, E | Usage proves value. Value creates lighthouse customers. Feedback loops (E) keep usage growing. Everything ladders to adoption. |

---

## Feb 9 Workshop Feed

_Ideas from this workshop that could become exercises or talking points for the Feb 9 team session._

- **"Crazy automation" brainstorm**: Give the team the same brief (automate everything, crazier = better, simple implementation) and have them pitch ideas in 10 minutes. Source: Core Principle above.
- **Build a pipeline in a day**: Pick one of the patterns (B, C, or D) and have the team prototype it live during the workshop. Source: Prototype Ideas.
- **Cookbook kickoff**: Use the workshop to seed the Shared Automation Library (F) with the team's existing hacks and shortcuts. Everyone contributes one.
- **AI workflow show-and-tell**: Each person demos their best AI trick for 3 minutes. Captures the raw material for Prompt Shadowing (H).
- **"Be Pirates" kickoff**: Open the Feb 9 workshop by announcing the pirate mandate. Give everyone 5 minutes to sign up for a tool they've wanted to try but haven't. Expense it on the spot. Source: Idea M.
- **Overnight agent challenge**: Before the workshop, set up an overnight agent run on a real team problem. Present the morning results live at the workshop as proof of concept. Source: Idea J.
- **Agent endurance experiment**: Pair up, define a task, launch an agent, and see how far it gets in the workshop session. Debrief on failure modes. Source: Idea I.
- **Scout rotation sign-up**: Establish the rotating AI tool scout role during the workshop. First scout starts the following week. Source: Idea K.
- **"Parallel is fine" talk**: Share the Cowork story as a framing device. Normalise overlap, reframe "someone else shipped it" as validation not failure. Source: Idea N.
- **Open with the emotional contract**: Before showing any tools -- set the frame: "We're going to become 10X faster, and it's going to be more fun, not less." Every exercise that follows gets filtered through this. Source: Idea O.
- **"What would Disneyland do?"** exercise: Take a real AEM customer journey and redesign it through the Disneylandification lens. What trust signals would you add? What meaningful events would you capture? Source: Idea P.
- **Usage obsession wall**: Print current usage metrics. As a team, brainstorm what would 10X each number. Vote on top 3 to pursue. Source: Idea Q.
- **Design migration challenge**: Take a real customer's existing site, give small teams 30 mins to sketch an AI-generated beautiful redesign concept. Source: Idea R.
- **Closing roundtable: Two Sentences That Matter**: Every person shares (1) their focus to reach next-level AI fluency, and (2) their stretch goal for end of year. One sentence each, no hedging. Capture and post to Slack as public commitments. Source: Category 3.
- **Agent management levelling exercise**: Present the 5-level progression (function --> task --> long-run --> orchestration --> autonomous). Each person self-assesses where they are today and where they want to be by mid-year. Source: Idea S.
- **Live orchestration demo**: Set up an orchestrator agent with 2-3 execution agents working on the same problem in parallel. Show the team what "managing agents" looks like in practice. Source: Idea S.
- **"We are an applied research team"**: Introduce the Cursor framing. Ask each person: "What have you built for yourself that could be research output?" Reframe internal hacks as applied research. Source: Idea T.
- **Crew formation exercise**: Pair people into 1-2 person crews for a workshop challenge. Experience what it feels like to own a problem end-to-end with agents, without a manager coordinating. Debrief on what changes. Source: Idea U.
- **AI maturity self-assessment**: Open Feb 9 with the 4-level framework. Everyone places themselves on the scale. Discuss: what would it take to move up one level by mid-year? Use observable signals to make it concrete. Source: Idea W.
- **"What does Level 4 look like?"** group design: After self-assessment, run a group exercise: "If our team were fully AI Native, what would a typical week look like? What infrastructure would exist? What would we never do manually?" Source: Idea W.
- **Boris Cherny case study**: Present the 300 PRs/month workflow. Show the slide. Then ask: "What would YOUR version of this look like? What's stopping you from running 5 agents in parallel tomorrow?" Source: Idea X.
- **Culture manifesto workshop**: Present Anthropic's 5 pillars. Discuss each: does it apply to us? Then present 4 proposed additions (Build for the Team, Make It Visible, Have Fun Doing It, Elevate Don't Grind). Debate, refine, adopt. Team leaves with a co-created culture document. Source: Culture Model.

---

## Action Items

_Extracted commitments, decisions, and next steps._

| # | Action | Owner | Status | Source |
|---|--------|-------|--------|--------|
| 1 | Evaluate which prototype idea (A-H) to build first | TBD | Open | Core Principle |
| 2 | Set up shared context store for meeting pipelines | TBD | Open | Idea B |
| 3 | Plan Feb 9 team workshop agenda incorporating these ideas | You | Open | Category 3 |
| 4 | Benchmark long-running agent: define a task, run for 1h/4h/8h, map failure modes | TBD | Open | Idea I |
| 5 | Design the overnight idea queue: where do ideas come from, how are they prioritised? | TBD | Open | Idea J |
| 6 | Establish rotating AI tool scout role and cadence | TBD | Open | Idea K |
| 7 | Communicate "Be Pirates" mandate to the team with explicit examples | You | Open | Idea M |
| 8 | Define what "meaningful events" are for context-building in brand experience | TBD | Open | Idea P |
| 9 | Set up weekly usage dashboard -- make it the first thing the team sees | TBD | Open | Idea Q |
| 10 | Identify lighthouse customer candidate and assign relationship owner | TBD | Open | Idea Q2 |
| 11 | Prototype AI design generation for one customer migration (side-by-side comparison) | TBD | Open | Idea R |
| 12 | Prepare roundtable format and framing for Feb 9 closing | You | Open | Category 3 |
| 13 | Create "Team Commitments 2025" page after Feb 9 roundtable; schedule mid-year revisit | You | Open | Category 3 |
| 14 | Design agent management training progression (Levels 1-5) with concrete exercises | TBD | Open | Idea S |
| 15 | Build a live orchestrator + execution agents demo for Feb 9 | TBD | Open | Idea S |
| 16 | Adopt "applied research team" label -- decide if formal or informal | You | Open | Idea T |
| 17 | Make "how many agents?" a standard design question in task planning | TBD | Open | Idea V |
| 18 | Run team-wide AI maturity self-assessment at Feb 9 using the 4-level framework | You | Open | Idea W |
| 19 | Define observable signals for each level (Level 1-4) so assessment is objective | You | Open | Idea W |
| 20 | Set individual level-up targets: each person commits to a level jump by mid-year | Team | Open | Idea W |
| 21 | Set up a parallel Claude Code workflow (5+ terminals) and test on a real task | You | Open | Idea X |
| 22 | Create shared CLAUDE.md with institutional memory for the team's repos | TBD | Open | Idea X |
| 23 | Prepare Anthropic culture pillars + proposed additions for Feb 9 discussion | You | Open | Culture Model |
| 24 | Finalise team culture manifesto after Feb 9 debate and publish to Slack/repo | You | Open | Culture Model |

---

## Attribution Index

_Who said what -- for follow-up and ownership._

| Person/Role | Idea/Statement | Context |
|-------------|---------------|---------|
| Alex Koren (Anthropic) | Parallel innovation is expected; Cowork shipped in 10 days over holidays while his team worked on something similar | Category 4, Idea N |
| Loni | "Disneylandification" -- brand experience must delight like Disneyland; meaningful events build context for exceptional experience | Category 2, Idea P |
| Amit (Product SVP) | "Are we moving fast enough?" -- usage is the #1 objective; track and maximise everywhere | Category 2, Idea Q |
| Amit (Product SVP) | Lighthouse customer goal: a customer who says "I embarked on agentic evolution with Adobe and this is my value" | Category 2, Idea Q2 |
| Cursor PM | "Applied research team" -- research how to improve your own job, ship it as product | Category 4, Idea T |
| Cursor PM | 10-person teams evolve to 1-2 person crews; managers/PMs become less relevant | Category 4, Idea U |
| Cursor PM | Multi-agent as the default | Category 4, Idea V |
| Alex Koren (Anthropic) | AI Evolution Framework: 4 levels from AI User to AI Native Team | Category 4, Idea W |
| Boris Cherny (Anthropic) | 300+ PRs in December using 10-15 parallel Claude Code sessions, plan-first, auto-ship pipeline | Category 4, Idea X |
| Anthropic (culture slide) | 5 pillars: AI-First, Push Boundaries, Write & Share, Fail Fast, Stay Skeptical | Category 3, Culture Model |

---

---

## Synthesis: Top Takeaways

_Executive summary of the One AEM workshop, through the lens of transforming the team to become 10X faster with AI._

### The One-Sentence Version

**Become an AI Native Team (Level 4) by giving engineers explicit permission to break rules, restructuring work around parallel agent fleets, and building shared infrastructure that makes the AI-native way the default -- while keeping it fun.**

### Three Takeaways to Share Today

**1. The goal is elevation, not extraction.**

Every idea in this workshop -- agents, pipelines, overnight factories -- could be misread as "work more." The real message is the opposite: **delegate more, think higher, enjoy it.** The team is already outperforming industry and company averages. The next leap is about changing *what* humans spend energy on, not how much. Engineers become managers of agent fleets. The job gets harder and more interesting, not busier. If the transformation feels like burnout, it failed -- regardless of output. _(Sources: O, S, Anthropic culture model)_

**2. We have a maturity framework and a concrete target.**

Level 1 (AI User) → Level 2 (AI First) → Level 3 (AI Native Individual) → Level 4 (AI Native Team). Most of the team is at Level 1. A few are at Level 2. Boris Cherny's 300 PRs/month shows what Level 3 looks like in practice. The target: every individual at Level 3, the team at Level 4. The critical insight: Level 3 is a training problem (teach individuals to orchestrate agents). Level 4 is a systems problem (build shared tooling, norms, and culture that make AI-native the default for everyone, including new joiners). _(Sources: W, X, S, U, V)_

**3. The cultural unlock is already granted: "Be Pirates."**

Explicitly sanctioned at the director+ level across the organisation. Break rules, expense tools, experiment freely, build in parallel, fail fast. This removes the #1 blocker to transformation: fear of getting in trouble. Combined with the "applied research team" identity from Cursor and Anthropic's 5 culture pillars, the team has a complete cultural model to adopt -- plus 4 additions we propose to cover the team-level gap (Build for the Team, Make It Visible, Have Fun, Elevate Don't Grind). _(Sources: M, L, N, T, Anthropic culture pillars)_

### The System That Connects Everything

Every idea in this document follows the same architecture:

```
Passive Trigger → Capture → AI Processing → Artifact → Auto-Distribute
```

This pattern applies to:
- **Internal tools** (A-H): meetings, demos, feedback, status -- all auto-processed
- **The product** (P, R): user events captured → context built → personalised experience delivered
- **The engineering practice** (I, J, V, X): tasks decomposed → agents execute in parallel → human verifies

The team that builds these pipelines internally IS the applied research team that informs the product. The internal and external loops are the same architecture at different scales.

### What This Means for Feb 9

The workshop has a natural arc:

1. **Open with the emotional contract** -- "10X faster AND more fun" (O)
2. **Assess where we are** -- AI maturity self-assessment, Level 1-4 (W)
3. **Show what's possible** -- Boris Cherny case study, Cursor team model (X, U, V)
4. **Co-create our culture** -- Anthropic's 5 pillars + our 4 additions → team manifesto
5. **Build something** -- pick a pipeline (B, C, or D) and prototype it live as crews
6. **Close with commitments** -- Two Sentences roundtable: focus + stretch goal

The team leaves Feb 9 with: a shared maturity assessment, a co-created culture manifesto, a working prototype, and personal commitments on paper.

### The Product Bet

Alongside the team transformation, the product direction is clear:
- **Usage is the north star** -- track it weekly, maximise it everywhere (Amit)
- **"Disneylandification"** -- brand experience must delight like an app, not a brochure (Loni)
- **Lighthouse customer by year-end** -- a real customer saying "I embarked on this agentic evolution with Adobe and this is my value" (Amit)
- **Design as migration lever** -- turn "your old site worked" into "your new site is beautiful" (R)

The team transformation (10X faster engineering) and the product bet (AI-native AEM experiences) reinforce each other. The faster the team moves, the faster the product evolves. The more the team dogfoods AI-native workflows, the more they understand what customers need.

### Open Questions

1. **Who owns the lighthouse customer relationship?** (Q2 -- needs a named owner)
2. **Which prototype idea (A-H) do we build first?** (Prioritisation needed before Feb 9)
3. **How do we measure "fun"?** (O -- the sustainability indicator needs a signal, even informal)
4. **What's the team's actual Level 1/2/3 distribution today?** (Run the assessment before Feb 9 so you arrive with data, not guesses)

---

> **Conviction guide:** [DOING] = committed | [STRONG] = high conviction | [EXPLORING] = needs thought | [MAYBE] = low commitment
> **Priority guide:** `!!` = top insight (surfaces above) | `!` = important | unmarked = standard
