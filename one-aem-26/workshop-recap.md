# One AEM Workshop — Strategic Recap

> **February 26, 2025 | 9 Sessions | 6-Page Synthesis**
> Written as executive summary and podcast script. ~35 minutes read-aloud.

---

## Page 1: The Shift Has Already Happened

Amit opened the SVP Roundtable with a question that set the tone for the entire workshop: **"Are we moving fast enough?"** It was not a critique. It was a dare. Because in the same breath, he called the AEM team "poster children for reinvention" — a team that has already earned the right to ask the uncomfortable question. That productive tension — pride in how far we have come, restlessness about how far we need to go — ran through every session that followed.

The external speakers framed the stakes. Alex Koren from Anthropic delivered the opening keynote with a clear thesis: **AI-first does not mean AI-assisted.** It means AI as context engine, as capability multiplier, as ambient presence woven into every workflow. The shift is not from "sometimes using AI" to "often using AI." It is from AI as tool to AI as infrastructure — the substrate on which all work happens. Koren's framework was direct: most teams are at Level 1 on the AI maturity curve. The target is Level 4. The distance between those two points is not incremental. It is structural.

Brendan Burns from Microsoft offered a grounding counterpoint in his keynote on AI transformation in Azure. His message: **AI is a tool. Use the tools. Get everyone to use the tools. Repeat step one.** Burns was deliberately pragmatic. He emphasized learning, rethinking, and knowing your history. His three-step mantra — use it, get others to use it, do it again until it works — is deceptively simple. The first time someone tries an AI tool, they often think "this doesn't work." The second time, they realize "wait, this actually works." The gap between those two reactions is the gap between skepticism and adoption. Burns also stressed: **rethink everything, talk to everyone, and remember that the human role is learning and growing — that is part of the job, not a distraction from it.**

So the workshop started with two keynotes pointing in the same direction from different angles. Koren said: rebuild your workflows around AI, make it ambient, make it structural. Burns said: start simpler, use the tools on things you actually care about, get everyone doing it, and repeat. The synthesis is clear. We are not bolting AI onto old workflows. We are rebuilding how work operates. Not AI-assisted. AI-native.

The SVP Roundtable with Amit made this personal. He talked about the "sheer freakiness" of the agentic web — the pace of change, the new players entering the space, the strategic questions we need to be asking. But he also said something that landed hard: **"You've got to show me."** Not as a threat. As a standard. The era of promising transformation is over. The era of proving it has begun. Show the customer. Show the leadership. Show the market. Amit's challenge to the room was clear: we are uniquely positioned, we have product-market fit, we have established partnerships. Now we need to amplify our message, get louder, and demonstrate proven value. The question is not whether we are doing the right things. It is whether we are doing them fast enough to matter.

---

## Page 2: One AEM — The Product Bet

Every transformation needs a destination. Ours is One AEM — and the workshop made the product vision concrete in a way the team had not experienced before.

The Internal Keynote, led by Loni Stark, Alexander Saar, Conrad Walton, and Michael Marth, laid out the FY25-to-FY26 bridge. The mandate: shared understanding, ownership, accountability, and — above all — **usage.** Usage is the leading indicator of value, adoption, and retention. If people are not using it, nothing else matters. The keynote established a clear set of **big bets already in motion**: Site Optimizer, Live Preview, Product Telemetrics (the measurement backbone), EXP Hub, Content AI, AI Assistants, and Project 42 (P42) — Adobe's initiative to build a suite of agentic capabilities including experience production, discovery, content optimization, governance, and development agents, all managed through a unified control plane.

But the product bet is not just a feature list. It is a thesis about where the market is going. The Agentic Web and Market Trends session, led by Michael Marth with Cedric Mueller, Bertrand de Coatpont, Haresh Kumar, and Philipp Rinne, made the argument: **the market is bifurcating.** On one side, discovery — third-party, generic AI-driven experiences where the user gets answers but no brand. On the other side, brand experience — owned, differentiated, delightful surfaces where the brand controls the relationship. Experience equals Content plus Code. That equation is our territory.

Edge Delivery Services (EDS) — Adobe's lightweight, speed-first rendering framework — is the technical substrate for this vision. Speed, simplicity, built-up context, content browsing — EDS gives us the performance foundation. But the session went further. The competition is becoming agent-ready. The data renaissance is real. Governance is becoming a differentiator, not a checkbox. And the buy-versus-build dynamics are shifting fast. We need to triple our speed and own the end-to-end view from content to context to customer.

Loni Stark introduced a concept that stuck: **"Disneylandification."** The brand experience must delight like Disneyland, not read like a brochure. Users entering a brand surface expect an experience — actionable, immersive, trust-building. That means finding and surfacing the trust signals that actually change behavior. Not generic badges, but context-aware proof points that matter to this user at this moment. It means tracking meaningful events — interactions that build the context layer from which personalization becomes real, not guesswork.

The strategic priorities crystallized into four commitments. **First: grow the flagship product 30% year-over-year.** That is the revenue anchor. **Second: own Brand AI Intelligence** — the data and insight layer that makes brands smarter. **Third: power Brand Deployed AI** — the infrastructure that lets brands deploy AI in their own experiences. **Fourth: prove Humanity plus AI value** — demonstrate measurably that the combination of human creativity and AI capability produces outcomes neither can achieve alone.

Amit reinforced this in the SVP Roundtable with the lighthouse customer imperative. The goal for this year: **a real customer who can say, unprompted, "I embarked on this agentic evolution with Adobe, and this is the value I am getting."** Not a case study written by marketing. A customer who believes it and says it because it is true. That is the standard. That is what "show me" means at the product level.

---

## Page 3: The Engineer of 2026

If Page 2 is the destination, Page 3 is the engine. This is the conceptual heart of the workshop: how the engineering role itself transforms.

Alex Koren's AI maturity framework from the Anthropic Keynote gave us a shared vocabulary. **Four levels: AI User, AI First, AI Native Individual, AI Native Team.** Most of the industry — and most of our team — sits at Level 1. A few individuals have reached Level 2, where AI is the first option for the majority of tasks. One or two people operate at Level 3, where their entire workflow has been restructured around AI as infrastructure. Level 4 — AI Native Team — is the target. And here is the critical insight that Koren made explicit: **getting individuals to Level 3 is a training problem. Getting the team to Level 4 is a systems problem.** They require fundamentally different interventions.

The Engineering Culture session with Titus Winters made this tangible. Winters framed the new engineering role around three words: **Plan, Execute, Verify.** The engineer's job shifts from writing code to designing the plan, orchestrating execution through agents, and verifying the output. His point was sharp: **coding is probably not the bottleneck.** Thinking clearly is. Design and architecture, verification and validation, prompting and planning — these are the skills that matter when agents handle the implementation. The job gets harder, not easier. It demands more clarity of thought, better decomposition of problems, and sharper judgment about what "good" looks like.

Boris Cherny from Anthropic gave us the proof point. In December, Boris shipped **over 300 pull requests** — a personal record — without working long hours. His method: five Claude Code terminals running in parallel on his machine, plus five to ten browser sessions, totaling ten to fifteen concurrent agent sessions. A plan-first discipline for every session — iterate with the AI until the plan is solid, then switch to execution. An auto-ship pipeline where each agent runs commit, push, and pull request when done, with automated CI, review, and merge workflows shepherding each PR to production. One person, team-level throughput, zero extra hours. The human role: **design the plan, verify the output, manage the fleet.**

The Transformation Learnings session connected this individual transformation to team structure. The concept of **Fluid Teams** — small, flexible crews that form and reform around initiatives — replaces the traditional model. Instead of one team of ten people on one initiative, the same headcount fans out into four crews of one to two engineers plus agents, each covering an independent track. Product and design float across crews, providing direction and quality rather than managing tickets. Tasks become shorter, more frequent, and massively parallel. The unit of work changes shape: from one person on one long sequential task to one person running many short tasks in parallel through agents.

Project 42 (P42) exemplifies what these teams build: a suite of dedicated agents — experience production, discovery, content optimization, governance, development — managed through a unified control plane. ACE (Adobe's dedicated AI innovation framework) provides the structured environment. FDE (Frontend Developer Enablement) focuses on unlocking new capabilities where the frontline actually is. The Agents Playground gives teams a safe space to experiment, build trust, and discover what works.

The hard truth that Winters emphasized: this is a harder job, not an easier one. New muscles are required. The transition needs safety, training, and patience. But the payoff — one person with the throughput of a team, a team with the throughput of a division — is not theoretical. Boris proved it.

---

## Page 4: Culture Eats Strategy — So We Designed the Culture

The transformation sticks only if the culture supports it. The workshop did not leave this to chance.

The Anthropic Keynote introduced five culture pillars that their team lives by. **AI-First**: try to answer your own questions with AI before asking a colleague. **Push Boundaries**: every task is an opportunity to find AI leverage, even the ones that seem impossible. **Write and Share**: when you learn something, document it and share it — learning that stays with one person is waste. **Fail Fast**: the cost of trying has collapsed with AI, so the cost of not trying is falling behind. **Stay Skeptical**: the harder you lean on AI, the sharper your judgment needs to be. Challenge the output. Verify. This is the counterweight to speed.

These five pillars are powerful, but they are oriented around individual practice — how one person works with AI. For a team aiming at Level 4, we identified four collective additions. **Build for the Team**: when you automate something, package it for others, not just yourself. **Make It Visible**: work, results, and experiments should be visible by default, not by effort — opt-out, not opt-in. **Have Fun Doing It**: the transformation should feel like play, not pressure — if it drains people, it is broken regardless of output. **Elevate, Don't Grind**: delegate everything you can, spend your time at the highest level of thinking you are capable of, and if you are doing something an agent could do, stop and delegate.

The SVP Roundtable gave these principles teeth with two words: **"Be Pirates."** Explicitly sanctioned at the director-plus level. Break rules, expense tools, experiment freely, build in parallel. The single biggest blocker to transformation is fear of getting in trouble. "Be Pirates" removes it. It is not a slogan. It is a cultural license with organizational backing.

Titus Winters reinforced this from the systems side in the Engineering Culture session. His framework: **pave the road.** Use DORA metrics (the DevOps Research and Assessment framework) to measure engineering health. Position AI as an amplifier, not a replacement. Build a platform ladder that lets teams climb to higher-leverage work. Give teams good incentives and flexibility. And above all, create the conditions for **least fear and most trust.** Winters was explicit about what kills transformation: bureaucracy, powerlessness, skepticism without agency. The antidote is psychological safety, a generative culture of learning, ownership of outcomes, and investment in internal documentation so knowledge compounds.

The Transformation Learnings session provided the process architecture that channels all this energy into shipped product. A **co-innovation pipeline** — Discovery to Alpha to Beta to GA (General Availability) — structures how ideas move from experiment to production. The Agents Playground gives teams a space to experiment, build trust, and discover what works without risking production systems. FDE serves as the engineering enablement layer, meeting frontline developers where they are and unlocking new capabilities from the phone to the browser.

The emotional contract underlying all of this: **we aim for 10X while having fun.** Elevation, not extraction. The goal is not to burn harder. It is to work at a fundamentally higher level. We are already ahead of the industry and above the company average — that is the baseline, not the ceiling. The push forward should feel like fun, not survival. Different ways of doing things, or not doing them at all. Everything we can delegate, we delegate. Psychological safety is non-negotiable. If people feel burned by this transformation, it failed.

---

## Page 5: Innovation in Action

The workshop was not all frameworks and strategy. The Dragon's Den session proved that the culture is already alive — and building.

Six teams pitched ideas they had prototyped or designed. **A 1-on-1 Management Tool** for performance reviews and goal setting — turning a manual, often-dreaded process into something AI-assisted and continuous. **AEM Co-Innovation Single Site** — a unified showcase for what the platform can do, built with the platform itself. **Visualize Customer Data** — multiple design approaches to making complex customer data intuitive and actionable. **A Page Speed Budgeter** — because performance is not a nice-to-have when EDS positions speed as a core differentiator. **Roadmap Roulette** — a creative take on prioritization that uses elements of chance and constraint (high roller, tasks, table types, dependencies) to break teams out of predictable planning patterns. And **SkillSeed, also called Knowledge Garden** — a tool to grow your team's skills through structured filtering and progressive learning paths.

What struck about the Dragon's Den was not any single pitch. It was the pattern. Every pitch demonstrated people building things because they wanted to, not because they were told to. That is "Be Pirates" in action. That is what an organization looks like when permission to experiment is real, not performative.

The prototypes discussed throughout the workshop share a common architecture that is worth naming: **Passive Trigger, Capture, AI Processing, Artifact, Auto-Distribute.** No manual trigger. No manual formatting. No manual distribution. The human stays in the creative and decision layer; the system handles everything else. Consider three examples. The **Zero-Touch Meeting Pipeline**: a team member joins a customer call, the meeting ends, and without any manual action a transcript is generated, fed into a shared context store, and distilled into key learnings, data points, and candidate next actions. Meetings become intelligence without manual notes. The **Auto-Demo Generator**: someone works on a proof-of-concept, and the system inspects the code, generates a structured summary, writes a demo script, records a screen walkthrough, produces a voiceover, and posts a one-minute demo to Slack. Every POC gets visibility by default. The **Overnight Idea Factory**: agents generate ideas, implement them overnight using multiple approaches, critique each other's results, and elect winners. The engineer arrives in the morning to ranked, working prototypes ready for review. Sleep becomes productive time.

There is a deeper identity emerging here that the Transformation Learnings session and the highlights synthesis both surfaced: **we are becoming an applied research team.** Borrowing a framing from the Cursor product team — the team researching how AI-native engineering works by doing it. Every internal tool we build is a product insight. Every workflow experiment is R&D. The Cookbook of shared automations is not just an internal catalog — it is a research output log. When someone builds a meeting pipeline or an auto-demo generator, they are not doing a side project. They are conducting applied research into the future of work.

---

## Page 6: What We Do Monday Morning

Frameworks are useful. Culture is essential. But neither matters without specificity. Here is what the workshop committed to.

The Leading for Scale session closed the workshop with a leadership-focused lens. Four competencies for scaling leaders: **Organizational Excellence, Technical Leadership, Business Acumen and Impact, and Influence.** Under these, four themes: **Vision and Scale** — be clear, compelling, and inspiring. **Understand the DX Product Portfolio** — leverage your own experience and your organization's experience to solve challenges. **Set Production Direction** — align goals, create KPIs, drive value. **Achieve Results** — through collaboration, mentoring the team, and organizational strategy.

The session was equally clear about blockers — and how to overcome them. **Stretch or go around: "Be Pirates."** Do not wait for the process to accommodate you. If the process is the blocker, route around it. **Do not reinvent the wheel every time.** Learn from what already exists, inside and outside Adobe. **Go big, do not wait.** Ambition and urgency are not opposites; they are partners. **Build context, customer-facing.** Understand what customers actually measure and care about. Get into their world. Different points of view, stepping into each other's shoes, rotation programs that broaden perspective — these are not soft skills. They are strategic capabilities.

The session also carried a caution that matters: **be careful not to rely too heavily on just AI.** The human role — judgment, context, relationships, creativity — is not diminished by AI. It is amplified by it. That balance runs through the entire workshop.

From everything we heard across nine sessions, five strategic commitments emerge.

**One: Usage as north star.** Track it weekly, not monthly. Make it the first metric the team sees. If usage is not growing, nothing else matters. This is the Internal Keynote's mandate and Amit's SVP Roundtable challenge made operational.

**Two: Lighthouse customer by year-end.** Not a marketing case study. A real customer partnership with a named owner, active engagement, and a customer who can say — unprompted — that the agentic evolution with Adobe is delivering value. "You've got to show me" is the standard.

**Three: AI maturity jump.** Every individual moves up at least one level by mid-year. Team-level Level 4 infrastructure — shared tooling, shared norms, shared context systems — is in place by year-end. Level 3 is a training investment. Level 4 is a systems investment. Both start now.

**Four: Be Pirates, visibly.** Experimentation is not just permitted — it is sanctioned, celebrated, and shared. When someone breaks a rule and it pays off, we celebrate it loudly. When it does not pay off, we celebrate the learning. Both outcomes compound. The Dragon's Den proved this energy already exists. The job now is to sustain and amplify it.

**Five: Prove Humanity plus AI.** Measurable outcomes, not aspirational statements. The combination of human creativity and AI capability must produce results that neither achieves alone — and we must be able to point to those results with specifics. Amit's "show me" standard applies to every initiative.

So let us return to where we started. In the SVP Roundtable, Amit asked: **"Are we moving fast enough?"** After two days and nine sessions, the answer is not "yes" or "no." The answer is: **now we know what fast enough looks like.** It looks like engineers managing fleets of agents, shipping 300 PRs in a month without burning out. It looks like fluid teams of one or two people covering what used to require ten. It looks like a co-innovation pipeline that takes experiments from discovery to general availability. It looks like a culture where "Be Pirates" is not a poster on the wall but a daily practice backed by leadership.

We have the vision. We have the framework. We have the permission. The work now is making it real — and showing the world what happens when the team Amit called "poster children for reinvention" decides to reinvent again.

---

*Based on 9 sessions from the One AEM Workshop, February 26, 2025. Sources: session infographics and workshop highlights synthesis.*
