---
title: "To Err Is Human; To Annotate, SILICON? Toward Robust Reproducibility in LLM Annotation"
url: /papers/silicon-robust-reproducibility-llm-annotation/
date: 2026-10-26T14:45:30-04:00
paper:
  authors:
    - name: "Xiang Cheng"
      affiliation: "University of Maryland, Smith School of Business"
    - name: "Raveesh Mayya"
      self: true
      affiliation: "New York University, Stern School of Business"
    - name: "João Sedoc"
      affiliation: "New York University, Stern School of Business"
  year: 2024
  arxiv: "2412.14461"
  status: "Working paper"
summary: "Extended narrative summary of the working paper by Xiang Cheng, Raveesh Mayya, and João Sedoc: LLM providers retire the models researchers use to label data, sometimes before the research is published. The SILICON workflow controls four sources of measurement error and tests open-weight models as permanent backups, and every task tested had at least one open-weight model with no statistically detectable difference from the best model."
description: "Extended summary of the working paper on model retirement, robust reproducibility, and measurement error in LLM text annotation (the SILICON workflow), by Xiang Cheng (UMD Smith), Raveesh Mayya (NYU Stern), and João Sedoc (NYU Stern)."
searchHidden: true
ShowBreadCrumbs: false
---

**Paper:** To Err Is Human; To Annotate, SILICON? Toward Robust Reproducibility in LLM Annotation

**Authors:** Xiang Cheng (University of Maryland, Smith School of Business), Raveesh Mayya (New York University, Stern School of Business), and João Sedoc (New York University, Stern School of Business)

**Status:** Working paper (R&R), latest version posted to arXiv in May 2026

**Findings in three sentences:** In research that uses large language models (LLMs) to label text, where the model behind the labels can be retired before the paper clears review, Xiang Cheng, Raveesh Mayya, and João Sedoc show how researchers can keep results reproducible by first controlling measurement error and then finding an open-weight model that can stand in for the original. Their SILICON workflow reduces error from annotation guidelines, human baselines, prompts, and model choice across nine management research tasks, and every task tested had at least one open-weight model with no statistically detectable difference in accuracy from the best model. In a simulated study where the true effect is set to 1.0, a regression that uses LLM labels estimates it at about 0.70 when the labels carry conventional error rates and at about 0.93 when they carry the lower error rates SILICON aims for.

**Method contribution:** An analytical framework that splits measurement error in LLM annotation into four sources (guidelines, human baselines, prompts, and models) and shows formally that agreement with human labels rises when a model moves closer to the truth and also when it repeats the humans' mistakes, which the authors call co-labeling covariance. The SILICON workflow targets each source, then adds a regression test that finds open-weight backup models with no statistically detectable difference from the focal model and a confidence-based routing procedure that shows when extra models improve labels and when they degrade them. It runs on validation samples of 100 to 200 documents.

*This is an extended narrative summary written for readers who want more detail than an abstract offers without reading the full paper.*

## Why this question matters

A research team spends thousands of dollars having a commercial LLM label customer reviews, social media posts, or business documents, and builds its main analysis on those labels. A year later, reviewers ask for new analyses, and the provider has retired the model. A successor model may label the same texts differently, and the team may find that its results no longer reproduce. Providers retire models on their own schedules. Some do so faster than a paper moves through review.

Some published studies already fail to reproduce for this reason. When software engineering researchers tried to reproduce the 18 studies from two leading 2024 conferences that shared their research materials and used OpenAI models, only five could be run at all, and none of those five reproduced fully. Retired models affected at least four of the studies and were the only obstacle specific to LLMs. Even a model that stays available can change, as researchers at Stanford and UC Berkeley found when the March and June 2023 versions of GPT-4 and GPT-3.5 behaved very differently on the same tasks. Outside academia, the parcel firm DPD disabled part of its customer service chatbot in January 2024 after a "system update" left it swearing at a customer and criticizing the company, at one point in a haiku.

Human annotators leave projects too, but a team can train new ones on the same guidelines. A retired model is gone for good. No successor is guaranteed to label the way it did. João Sedoc, Xiang Cheng, and Raveesh Mayya call the ability to reproduce annotation results after the original model becomes unavailable robust reproducibility, and they argue that the problem will not go away, because researchers keep adopting LLMs for labeling while frontier providers retire models as a matter of routine. The question the paper asks is simple: if the model a study was built on can vanish tomorrow, how can researchers make sure the science does not vanish with it?

## Setting and data

Raveesh Mayya (NYU Stern), João Sedoc (NYU Stern), and Xiang Cheng (UMD Smith) test their approach on nine classification tasks from management research. In six of them the team controls every step, labeling business proposals from decentralized autonomous organizations, product attributes in online reviews, the intent of customer service utterances and whether a conversation breaks down, and whether product descriptions convey a sense of connectedness and of what kind. The other three (fear and hate speech, criticism in tweets about academic papers, and sentiment) reuse guidelines and human labels from published studies and count as supplementary evidence. Seven models from five providers do the labeling, four closed and three open-weight, and five more are added as a robustness check. Agreement is measured with Cohen's Kappa, with 0.5 as the target, above the conventional 0.4 for moderate agreement.

## Measurement error comes first

Xiang Cheng, João Sedoc, and Raveesh Mayya argue that reproducibility cannot be judged until measurement error is under control. When labels are far from the truth, two models can be wrong in different ways. A gap between a retired model and its replacement then mixes the models' differences with muddled guidelines, an unreliable human baseline, or a weak prompt. The problem is larger with LLMs. A human annotator who is unsure can ask around and infer what the researcher meant, whereas a model has only the text of its instructions.

Because the truth is never observed, models are judged by how often they match human reference labels. Under a standard model of how human labelers err, the authors prove that this agreement goes up both when the model gets closer to the truth and when the model and the humans err on the same items, the second effect being what they call co-labeling covariance. When it is large, the model with the highest agreement may simply share the humans' errors.

## The research questions and how they are answered

The main question João Sedoc, Raveesh Mayya, and Xiang Cheng ask is, how can researchers achieve and evaluate robust reproducibility in LLM-based text annotation? Their workflow, SILICON (Systematic Inference with LLMs for Information Classification and Notation), first targets each source of error. Three research assistants label a small sample independently, meet over Zoom to resolve disagreements, and revise the guidelines until they clear the agreement target on the first pass of a fresh sample, a process that took their agreement on dialog intent from a Kappa of 0.128 to 0.61. These task-level annotation experts then label the baseline. Guidelines go into the system role, the channel that sets a model's behavior before the conversation starts, and candidate models are compared on identical guidelines, baselines, and prompts.

With error controlled, the team treats results as reproducible on a target model when the two show no statistically detectable difference in accuracy. The first target is a backup. Open-weight models can be downloaded and kept, so no provider can retire them, and a logistic regression of item-level matches with the expert labels, with standard errors clustered by item, tests each one against the focal model, here the best model for the task. The second target is an upper bound. The focal model labels each item five times, and items where its answers split, measured by a low First-Second Distance (the gap between the shares of its two most common answers), go to a majority vote with the next two best models. Moving the cutoff from no items to all items traces a routing curve that shows whether extra models help.

## What the study finds

Raveesh Mayya, Xiang Cheng, and João Sedoc find that each intervention reduces error. Iteratively refined guidelines raise the agreement between model labels and the expert baseline by 0.1 to 0.5 Kappa points over one-shot guidelines in all six primary tasks. Annotation experts agree with each other 0.1 to 0.4 points more than research assistants who got the final guidelines without helping write them, the paper's stand-in for crowd workers. On dialog intent, the two groups reach 0.61 and 0.23. Placing guidelines in the system role gives the best prompt for all four models tested, although the gain is not statistically significant.

The baseline also changes which model looks best. On dialog intent, the hardest task for the models, most models agree more with the crowd baseline than with the experts, consistent with co-labeling covariance, while among model and task pairs where agreement with both baselines exceeds 0.5, almost all align at least as closely with the experts. Estimated directly on items where all three experts agree, co-labeling covariance for the best model is at most about 0.01 in four of the six tasks and larger in the two multi-label tasks.

No model leads everywhere. The top model changes from task to task, and an open-weight model leads on three of the nine. Binary tasks are the easy cases, with Kappa above 0.5 for almost every model. Multi-label tasks, where an item can carry several labels, are hard, with Kappa around 0.2 to 0.4, and the authors suggest leaving them to human annotators or to designs that pair humans with LLMs.

Every task whose best model is closed has at least one open-weight model with no statistically detectable difference in accuracy, and on dialog breakdown the best model is open-weight already. The routing curves differ by task. On dialog breakdown, agreement rises steadily as more items go to the vote, while on dialog intent it falls, consistent with the two auxiliary models sharing mistakes that the focal model avoids. Business proposals and review attributes peak at an interior cutoff. Connectedness presence stays flat, so extra models there add cost without adding accuracy.

## What the simulation shows

To check whether lower measurement error changes the conclusions researchers draw, Xiang Cheng, Raveesh Mayya, and João Sedoc run a Monte Carlo simulation of the SILICON sequence in which no LLM is called. Each of 1,000 replicates draws balanced binary true labels for 1,000 validation items and 300 test items and creates human reference labels that flip the truth at a set error rate. It then generates ten candidate LLM configurations, each with its own accuracy and its own coupling rate, the probability that it copies the human label, which stands in for co-labeling covariance. The simulated researcher picks the candidate that agrees most with the human labels on the validation items, uses it to label the test items, and regresses an outcome generated from the true labels, with a true effect of 1.0, on the LLM labels. The conventional regime has a human error rate of 15 percent and candidates with 65 to 85 percent accuracy, and the SILICON regime has 2 percent and 75 to 95 percent, with the human error rates calibrated from the empirical results and the same coupling range of 20 to 50 percent in both.

Under the conventional regime, the estimated effect averages 0.696, about 30 percent below the truth, and the 95 percent confidence interval contains the true effect in only 31.7 percent of replicates. Under the SILICON regime, the estimate averages about 0.93, which cuts the shortfall by 75 percent, coverage rises to 89.6 percent, and choosing by agreement picks the truly best candidate in 98.1 percent of replicates, up from 79.7 percent. When the two candidate pools nearly overlap, the bias still falls by 57 percent and coverage rises from 31.7 to 80.5 percent, and with very low coupling in both regimes it falls by 68 percent.

## What it means

João Sedoc, Xiang Cheng, and Raveesh Mayya turn the results into steps for researchers. A researcher who labels data with a closed model, whether the best one or a cheaper one, should control the four error sources on a validation sample and then test open-weight models against it before labeling at scale. An open-weight model with no detectable difference gives the study a backup that no provider can retire. The routing curve then shows whether paying for more models is worth it. Firms that classify support tickets, reviews, or employee feedback with LLMs face the same risk, and an open-weight backup also protects them from lock-in to a single vendor.

Two caveats. The workflow treats high agreement among annotators as the goal, which does not suit studies that set out to measure how differently people read the same text. And the validation covers classification tasks only.

## Where this sits in the broader agenda

The paper belongs to Raveesh Mayya's work on how generative AI changes knowledge work, including research itself. It connects to his study with Doron Yeverechyahu and Gal Oestreicher-Singer on [GitHub Copilot and open-source innovation](/papers/llms-open-source-innovation-github-copilot/), which used an LLM to label commit messages, and to his study with Badr-Eddine Lahsini on [Moroccan Darija](/papers/llms-low-resource-languages-moroccan-darija/), which shares its focus on when LLM output can be trusted.

The team is now measuring what each additional model call costs against the accuracy it adds and extending the routing procedure to choose among more models. An open-source toolkit implementing SILICON will accompany the published paper.

**Full citation:** Cheng, X., Mayya, R., and Sedoc, J. "To Err Is Human; To Annotate, SILICON? Toward Robust Reproducibility in LLM Annotation." Working paper (R&R). arXiv:2412.14461.
