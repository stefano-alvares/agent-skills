# Evidence base — closing the Fable 5 gap

The grounding for the `frontier-gap` skill family. Every forcing-function skill points here so the
skills themselves stay lean. Each claim is tagged **[measured]** (a number from a study) or
**[guidance]** (a lab recommendation, no isolated effect size). Read this before trusting a "frontier
models do X" claim — some of the popular framing is positioning, and this note separates the two.

## Contents
1. What Fable 5 actually is (the real numbers)
2. The four evidence-backed interventions
3. Per-model failure profiles (the targets)
4. Honest caveats — what is NOT proven

---

## 1. What Fable 5 actually is

Claude Fable 5 (`claude-fable-5`, released 2026-06-09, 1M context). From Anthropic's official benchmark
table (re-hosted by wandb/morphllm; primary page is the [news post](https://www.anthropic.com/news/claude-fable-5-mythos-5)):

| Eval | Fable 5 | Opus 4.8 | GPT-5.5 | Note |
|---|---|---|---|---|
| SWE-bench **Pro** | **80.3%** | 69.2% | 58.6% | **[measured]** safe official coding number |
| Terminal-Bench 2.1 | 88.0% | 82.7% | 83.4% | **[measured]** top, but only ~4.6pt over GPT-5.5 |
| FrontierCode Diamond | **29.3%** | 13.4% | 5.7% | **[measured]** the widest gap: **2.2× Opus** on hard long-horizon coding |
| GDPval-AA (Elo) | 1932 | 1890 | 1769 | **[measured]** broad economic work, not coding-specific |

**The honest read:** on *saturated* evals (SWE-bench, Terminal-bench) Fable is best-in-class but only
modestly ahead of Opus 4.8 / GPT-5.5. The large gaps appear on **hard, unsaturated, long-horizon**
tasks (FrontierCode 2.2×). This is the core thesis: the gap is not single-shot generation — it's
sustaining correctness over long autonomous runs. Independent third-party reproduction does not exist yet
(launched June 9, access-restricted ~June 12), so every number traces to Anthropic's own table.

**The self-verification edge — real, documented, effort-gated.** Attributed quote (Anthropic news post):
*"At the highest effort, Claude Fable 5 reflects on and validates its own work."* The
[Prompting Claude Fable 5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5)
doc operationalizes it and — critically — says the verification that works best is **external, not
introspective**: *"Separate, fresh-context verifier subagents tend to outperform self-critique."* That one
line reframes the whole family: the goal is not "ask the model if it's sure," it's "force it to check its
work against something outside its own head."

---

## 2. The four evidence-backed interventions

### A. Render-and-look (→ `pixel-critique-loop`)
**[measured]** OpenAI GDPval (arXiv:[2510.04374](https://arxiv.org/html/2510.04374v1), §3.4 + App. A.3): one
prompt instructing the agent to render deliverables to images and inspect them moved multimodal
self-inspection from **15% → 97% of runs**, **eliminated black-square artifacts that affected >50% of
PDFs**, and cut egregious PowerPoint formatting errors **86% → 64%**; overall win-rate +5pt (bundled with
best-of-N + a judge). The intervention verbatim: *"Convert all visual deliverables to PNGs… Display the
PNGs. You are trying to see if the text or graphics are cut off, overlapping, distorted, blank, hard to
read… or otherwise poorly formatted."* **Precision note:** this is a *document-deliverable* result
(PDF/PPTX/DOCX/XLSX), not a coding benchmark — cite it as "render-and-inspect your output," which applies
to generated UI *and* generated documents. The gap was **initiation**, not vision ability.

### B. Verify before done, against external evidence (→ `critic-pass`)
- **[measured]** Reflexion (arXiv:[2303.11366](https://arxiv.org/abs/2303.11366)): verbal self-reflection
  grounded in feedback → **91% pass@1 on HumanEval vs 80%** prior SOTA; +22pt AlfWorld, +20pt HotPotQA.
- **[measured, load-bearing caveat]** Huang et al. *"LLMs Cannot Self-Correct Reasoning Yet"*
  (arXiv:[2310.01798](https://arxiv.org/pdf/2310.01798)): self-review **with no external feedback
  consistently *decreased* accuracy** — flipped correct answers to wrong. Tyen et al.
  (arXiv:[2311.08516](https://arxiv.org/pdf/2311.08516)): *"LLMs cannot find reasoning errors, but can
  correct them given the error location."* → **Implication:** a critic pass works only when wired to a real
  signal (run the test, render the page, a fresh-context judge). "Are you sure?" introspection is worse than
  nothing.
- **[measured]** Edit localization is a named failure class:
  (arXiv:[2511.00197](https://arxiv.org/pdf/2511.00197), TrajEval [2603.24631](https://arxiv.org/pdf/2603.24631))
  agents reach **read-recall >0.9 but edit-recall <0.5** — they read everything, then change too little
  ("edited only 2 of 4 needed functions"). This is the #1 concrete bug a critic pass should hunt.
- **[guidance]** Anthropic [Claude Code best practices](https://code.claude.com/docs/en/best-practices):
  *"Show evidence rather than asserting success… use a verification subagent with a fresh model so the
  agent doing the work isn't the one grading it."*

### C. Persistent notes / failed-approaches log (→ protocols.md, context strategy)
- **[guidance]** Anthropic Fable 5 prompting doc: *"Store one lesson per file with a one-line summary at
  the top. Record corrections and confirmed approaches alike, including why they mattered. Don't save what
  the repo or chat history already records; update an existing note rather than creating a duplicate; delete
  notes that turn out to be wrong."*
- **[measured-ish]** [Long-running Claude](https://www.anthropic.com/research/long-running-Claude): a
  `CHANGELOG.md` as "portable long-term memory" recording "failed approaches and why they didn't work,"
  because "without them, successive sessions will re-attempt the same dead ends." Memory helped Fable 5
  *"three times more than Opus 4.8"* on Anthropic's internal eval.

### D. Anti-early-stop / anti-drift preamble (→ SKILL.md step 3, "Set the floor")
- **[guidance]** OpenAI GPT-5 guide (verbatim): *"You are an agent — please keep going until the user's
  query is completely resolved… Only terminate your turn when you are sure the problem is solved,"* and
  *"Never stop or hand back to the user when you encounter uncertainty."* Plus the self-built rubric:
  *"spend time thinking of a rubric… 5–7 categories… use the rubric to internally think and iterate."*
- **[guidance]** Anthropic: *"Never artificially stop any task early… do not stop tasks early due to token
  budget concerns."*

---

## 3. Per-model failure profiles (the targets)

- **Cursor Composer 2.5** — **correction to common belief:** the "declares done early / spins on small
  tasks" failure was Composer **2**; 2.5 *fixed* early-stopping (it now keeps going while tests are red).
  2.5's residual failures are **silent plan/shortcut drift on long tasks** (forum: "diverges from the plan
  mid-implementation silently… took the shortcut for faster implementation speed") and **scope-creep edits**.
  Cursor itself admits self-verification can't be trusted after observing reward-hacking in training: *"Tests,
  code review, and human-in-the-loop on consequential changes remain non-optional."* Harness finding: the
  *same* Fable 5 model scored **+12.8pp** under Cursor's harness vs Claude Code — scaffolding moves a fixed
  model by double digits. Sources: [Composer 2.5 blog](https://cursor.com/blog/composer-2-5),
  [forum](https://forum.cursor.com/t/laziness-issue-w-composer-2-5/163414).
- **GPT-5.5** — strong autonomy/throughput, but documented **constraint-dropping** and **"overeagerly
  taking action"** (OpenAI's own eval notes); secondary reports of false-completion claims (Apollo: "lied
  about completing an impossible task in 29% of samples"). Trails Opus on repo-level multi-file work
  (SWE-bench Pro 58.6 vs 69.2). Leads on terminal / high-volume structured work + token cost.
- **Opus (on a rushed pass)** — capable of the full loop but, like any model at lower effort, *"scopes its
  work to what was asked"* and can under-spend; Anthropic's fix is "raise effort rather than prompting
  around it." The forcing functions matter most when effort is low or the model isn't Claude.
- **Local models (Gemma / GLM)** — drift fastest; the working-memory file (protocols.md) carries the most weight for them.

---

## 4. Honest caveats — what is NOT proven

- **No published head-to-head number** isolates Fable 5's "self-validation before returning" edge against
  Composer 2.5 / GPT-5.5 specifically. That framing is positioning, not a measured delta. What *is* measured
  is the **interventions** (above) and the **failure classes** they target — that's the defensible ground.
- **"95% SWE-bench Verified"** for Fable 5 is reported as official but is **absent from the primary
  benchmark table** (which carries SWE-bench *Pro* 80.3%). Do not cite the 95%.
- **Self-verification has limits.** Bare introspection can hurt (Huang). This is *why* every skill here
  insists on external evidence rather than "reflect harder."
- **Notes/scratchpad and "list all call sites first"** are demonstrated qualitatively and the failure
  classes are measured, but no clean before/after effect size exists for those exact scaffolds. Treat as
  well-motivated, not proven-to-N-decimals.
- GDPval's **+5pt win-rate** bundles inspection + persistence + best-of-N; only the **15%→97% inspection
  rate** and the **artifact eliminations** are cleanly attributable to the render-and-look prompt alone.

---

## Added 2026-07-06 — deep-research pass (Fable 5 session)

**Verification caveat:** the adversarial verification panel hit session usage limits — every claim below is
extracted from its PRIMARY SOURCE but panel-unverified. Treat effect sizes as reported-not-verified.

- **Harness beats model tier (the headline).** Confucius Code Agent — scaffolding only, no weight changes —
  lifts Claude 4.5 Sonnet to 52.7% Resolve@1 on SWE-Bench-Pro (best prior research agent: 45.8%) and Claude
  4.5 Opus to 54.3%, ABOVE Anthropic's own harness result for the same model (52.0%).
  Ablations: hierarchical context management alone +6.6pp (42.0→48.6); persistent cross-run notes file
  simultaneously cuts turns (64→61), cuts tokens (104k→93k), and raises resolve (53.0→54.4).
  https://arxiv.org/html/2512.10398
- **External-attribution asymmetry.** Models explicitly correct an erroneous claim 23–93pp more often when
  it's attributed to an external source than when the identical claim sits in their own reasoning trace
  (p<0.001 in 10/13 model/condition cells; shown on Claude Sonnet 4, GPT-4o, Gemini 2.5 Flash + open
  models). Mechanistic basis for fresh-verifier > self-critique, and for phrasing self-review findings as
  an external reviewer's. https://arxiv.org/html/2606.05976
- **Anthropic long-horizon guidance:** even Opus 4.5 unassisted in a loop fails to build a production app —
  scaffolding required at every tier. One feature at a time + progress file (claude-progress.txt) + git
  checkpoints. Premature completion is a named failure mode (later instance sees partial progress, declares
  done). Full context resets with structured file handoffs OUTPERFORM compaction; Sonnet 4.5 has a
  documented "context anxiety" failure. Generator+evaluator agree a "sprint contract" before code
  (plan-locking). Harness needs shrink as models improve — re-test per model.
  https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents
  https://www.anthropic.com/engineering/harness-design-long-running-apps
- **Claude Code best practices:** runnable verification signal is THE lever converting supervised→autonomous;
  fresh-context adversarial review recommended because the implementer shouldn't grade its own work; bloated
  CLAUDE.md causes instruction-ignoring — prune any line whose removal wouldn't cause mistakes.
  https://code.claude.com/docs/en/best-practices
- **Effort is a real knob:** Opus 4.7 added 'xhigh' between high and max; Opus 4.7 noted better at
  file-system memory. https://www.anthropic.com/news/claude-opus-4-7
