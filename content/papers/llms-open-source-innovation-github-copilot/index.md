---
title: "The Impact of Large Language Models on Open-Source Innovation: Evidence from GitHub Copilot"
url: /papers/llms-open-source-innovation-github-copilot/
date: 2026-08-25T23:40:39+05:30
paper:
  authors:
    - name: "Doron Yeverechyahu"
      affiliation: "Tel Aviv University, Coller School of Management"
    - name: "Raveesh Mayya"
      self: true
      affiliation: "New York University, Stern School of Business"
    - name: "Gal Oestreicher-Singer"
      affiliation: "Tel Aviv University, Coller School of Management"
  year: 2024
  arxiv: "2409.08379"
  status: "Working paper"
summary: "Extended narrative summary of the working paper by Doron Yeverechyahu, Raveesh Mayya, and Gal Oestreicher-Singer: GitHub Copilot raised open-source contributions by 28 to 40 percent, but tilted them toward incremental maintenance work over substantive new features."
description: "Extended summary of the GitHub Copilot working paper on how LLMs reshape open-source innovation, by Raveesh Mayya (NYU Stern) and coauthors at Tel Aviv University."
searchHidden: true
ShowBreadCrumbs: false
---

**Paper:** The Impact of Large Language Models on Open-Source Innovation: Evidence from GitHub Copilot

**Authors:** Doron Yeverechyahu (Tel Aviv University, Coller School of Management), Raveesh Mayya (New York University, Stern School of Business), and Gal Oestreicher-Singer (Tel Aviv University, Coller School of Management)

**Status:** Working paper, available on arXiv (arXiv:2409.08379)

**Finding in one line:** Raveesh Mayya and his coauthors show that GitHub Copilot's launch increased open-source contributions to supported languages by 28 to 40 percent, but the growth tilted toward incremental maintenance work rather than substantive new features, and the tilt widened as the underlying model improved.

**Method contribution:** A natural experiment built on GitHub's business decision to support Python but not R at Copilot's launch, paired with two independent ways of classifying over 620,000 commits: parsing code diffs for net new function definitions, and GPT-4o annotation of commit messages benchmarked against expert human annotators.

*This is an extended narrative summary written for readers who want more detail than an abstract offers without reading the full paper.*

## Why this question matters

We have seen many well-done research that show that LLMs help productivity or creativity. However, most of them are on individual productivity or individual creativity and mostly measured when individuals complete assigned tasks in a controlled setting, with and without LLMs, i.e., guided work. However, think about how knowledge economy works: it does not run that way. Contributions seldom happen in isolation. Teams collaborate, and contributors build on each other's work. How LLM assistance plays out in the field, in that kind of collaborative setting, is not well-estabilished, and the answer cannot simply be extrapolated from individual experiments.

To predict what an LLM does to a collaborative project, Doron Yeverechyahu (Tel Aviv Coller), Raveesh Mayya (NYU Stern), and Gal Oestreicher-Singer (Tel Aviv Coller) argue you first need a typology of the work itself, and what separates tasks in collaborative knowledge work is the cognitive input each demands from the person doing it. Some contributions introduce functionality the project has never had, and the contributor has to formulate the problem before any code gets written, something the paper calls question ingenuity. The authors label these substantive. Others, labeled incremental, start from code that already exists, usually written by someone else, and refine or repair it; here the problem arrives mostly formed. A healthy project needs a steady supply of both.

LLMs generate output by recognizing patterns across large corpora of existing text and code. Copilot in particular completes the code you are writing from the code around it, so prior work is its raw material. An incremental task, where the codebase already constrains what a fix can look like, gives the model plenty to work with. A substantive task gives it much less, since no context window tells a contributor what new question is worth asking. The prediction follows: where Copilot is available, contributions of both kinds should rise, incremental ones should rise faster, and collaborative innovation should tilt, commit by commit, toward refining what exists.

## Setting and data

The ideal test needs collaborative work, tasks of both kinds, a granular log of every action, and an LLM that reached some projects while skipping comparable ones. GitHub's open-source ecosystem supplies all four, the last one by accident. When GitHub and OpenAI launched Copilot in October 2021 via some IDEs, Python was supported and R was not. This was a business decision, made even though Codex, the model underneath Copilot, handles R code fine. Python and R are both data-oriented languages, pandas in one and ggplot2 in the other, with heavy overlap in what their communities build. Yet for the five quarters until ChatGPT arrived in late 2022, contributors to R packages had no mainstream LLM assistant at all. Comparable ecosystems, one treated, one not.

The commit data run from October 2019 to October 2022 and cover the 2,000 most popular Python packages plus everything on CRAN, R's central registry, minus packages that had gone quiet in the two years before launch. Propensity score matching on pre-launch activity pairs each Python package with an R twin: 1,187 matched pairs, over 620,000 commits, aggregated by quarter. The same procedure applied to Rust (supported) and Haskell (not) yields 1,373 more pairs for a replication outside data science, and 273,000 older Python commits from 2016 to 2018 are held aside for a design described below.

Labeling 620,000 commits as substantive or incremental is its own problem, and the paper attacks it from two unrelated directions. The first is structural. Parse each commit's diff, count net new function definitions, and call the commit substantive if the count is positive, since new features usually arrive as new functions. The second reads the commit messages: GPT-4o assigns each message to one of five categories, two of which, code development and maintenance, map onto substantive and incremental. Before trusting the model, the authors had three expert annotators hand-tag 400 commits and benchmarked five LLMs against them, with Cohen's Kappa clearing 0.6 for the best performers. DeepSeek was cheaper than GPT-4o but at 80 tokens per second could not chew through a 720-million-token corpus in any reasonable time, so GPT-4o did the tagging.

## The research questions and how they are answered

The main causal question Raveesh Mayya and his coauthors ask is, what happens to the volume and the composition of contributions in an open-source ecosystem once an LLM assistant becomes available to it? Difference-in-differences on the matched Python and R panel does the main work, estimated with two-way fixed effects and, separately, with synthetic difference-in-differences, which reweights control packages and pre-treatment quarters to tighten the counterfactual. Lead-lag estimates show the two ecosystems moving together before launch (Figure 4), which is what parallel trends requires.

One could still worry that Python and R were on different trajectories for reasons unrelated to Copilot. Hence a second design that never compares languages at all: the same Python packages set against their own past, a 2016 to 2018 control era aligned calendar-quarter by calendar-quarter with the treatment era. And a third, rerunning everything on Rust versus Haskell, statically typed systems languages with a different community culture, plus a pooled analysis across all four languages. Three designs converging on the same answer is the shape of the paper.

## What the study finds

Volume first. Supported packages gain 28 to 40 percent more commits per quarter across specifications, against a pre-treatment mean of about 17 (Table 3). The temporal-controls design, which never touches R, lands at 20 to 27 percent. Version releases rise about 10 percent. Copilot grew open-source activity, no question.

Then the composition of contributions, where the differential impact lives and which the paper treats as its primary finding. Commits that add new functions rise by 0.800 per package-quarter; commits that do not, by 6.016 (Table 4). The LLM classification agrees, with maintenance up 2.299 against 1.472 for code development (Table 5). In logged specifications that reads as roughly 49 percent growth in incremental work against 20 percent in substantive work. Triple-difference tests say the gaps are statistically real, and the Rust and Haskell pair reproduces them.

Two more results say this is not a passing adoption blip. The gap is nearly three times larger in high-activity projects, exactly where codebases, documentation, and issue threads give the model the most context to lean on (Table 6). And when Copilot\'s underlying model was upgraded in June 2022, maintenance commits got a further significant boost while code development did not (Table 7). A better model widened the gap.

## What it means

March\'s old vocabulary of exploration and exploitation fits here. The authors\' reading is that an LLM amplifies whatever the existing context can support. It speeds up the exploitation of established codebases while offering far less to the exploratory work of conceiving features nobody has specified yet. In a firm, a manager can push against that pull. Open source has no manager. Contributors drift toward the tasks the tool makes easy, and the drift compounds as models improve.

What to do about it depends on who you are. Platforms could lean against the drift with grants, recognition programs, or targeted challenges for substantive feature development. Organizations that encourage employees to contribute to open source might direct them to early-stage projects, where context is thin, the model helps least, and human creativity is worth the most. For researchers, the accident matters as much as the finding. Generative AI spread so fast that credible control groups barely exist, which makes these five quarters one of the rare windows for causal field evidence on what LLMs do outside assigned-task settings.

Two caveats. The window closes before ChatGPT, when Copilot offered code completion and nothing conversational, so the estimates describe early completion tools rather than the agentic systems that came later. And not every Python contributor used Copilot during the period, so the numbers are plausibly a lower bound on the true effect.

## Where this sits in the broader agenda

This paper anchors Raveesh Mayya\'s research stream on generative AI and collaborative work, which runs alongside his stream on platform policy and digital regulation. The commit classification applies the SILICON procedure for reproducible LLM annotation that Mayya developed with coauthors, and the concern with which tasks AI helps most reappears in his field experiment on structured prompting for developers who speak low-resource languages. The common thread across these projects is not whether AI helps, but whom, and at what kind of work.

**Full citation:** Yeverechyahu, D., Mayya, R., and Oestreicher-Singer, G. "The Impact of Large Language Models on Open-Source Innovation: Evidence from GitHub Copilot." Working paper. arXiv:2409.08379.
