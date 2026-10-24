---
title: "Do Nonmonetary Virtual Gifts Enhance or Diminish Voluntary Paid Gifts? Evidence from a Video Game Live-Streaming Platform"
url: /papers/virtual-gifts-live-streaming/
date: 2026-08-25T23:40:39+05:30
paper:
  authors:
    - name: "Peiyan Yu"
      affiliation: "University of Georgia, Terry College of Business"
    - name: "Raveesh Mayya"
      self: true
      affiliation: "New York University, Stern School of Business"
    - name: "Anindya Ghose"
      affiliation: "New York University, Stern School of Business"
  venue: "Information Systems Research"
  year: 2026
  doi: "10.1287/isre.2024.0902"
  status: "Articles in Advance"
summary: "Extended narrative summary of the paper by Peiyan Yu, Raveesh Mayya, and Anindya Ghose (Information Systems Research, Articles in Advance): when a live-streaming platform gave viewers free gifts, paid gifting went up, not down, because the free tier diluted the signaling value of the cheapest paid gift."
description: "Extended summary of the ISR paper on virtual gifting in live-streaming, by Raveesh Mayya (NYU Stern) and coauthors."
searchHidden: true
ShowBreadCrumbs: false
---

**Paper:** Do Nonmonetary Virtual Gifts Enhance or Diminish Voluntary Paid Gifts? Evidence from a Video Game Live-Streaming Platform

**Authors:** Peiyan Yu (University of Georgia, Terry College of Business), Raveesh Mayya (New York University, Stern School of Business), and Anindya Ghose (New York University, Stern School of Business)

**Journal:** Information Systems Research, Articles in Advance

**Finding in one line:** Raveesh Mayya and his coauthors show that when a major live-streaming platform gave viewers free virtual gifts, paid gifting rose rather than fell, adding roughly $2.42 per viewer-streamer pair per week, because free gifts diluted the signaling value of the cheapest paid tier and pushed gifters up to costlier options.

**Method contribution:** Alongside a battery of modern staggered-adoption estimators and Temporal Causal Inference, the paper runs a controlled experiment on 1,440 LLM agents in MIT Professor John Horton's Expected Parrot EDSL framework, implementing all five methodological safeguards that Gao et al. (PNAS 2025) prescribe for using LLMs as human surrogates.

*This is an extended narrative summary written for readers who want more detail than an abstract offers without reading the full paper.*

## Why this question matters

The creator economy keeps growing, but live-streaming occupies an odd corner of it. While a pre-recorded video on YouTube earns for years, a live stream earns almost nothing once it ends. Whatever a streamer captures, they capture during the broadcast itself, while simultaneously delivering skilled gameplay and holding an audience in real time. That leaves little room for conventional monetization like mid-stream ads, and it is why voluntary paid gifts from viewers dominate streamer revenue in video-game live-streaming, an industry projected to grow from $8.4 billion in 2025 to $13.85 billion by 2030. Platforms have to balance that monetization pressure against keeping sessions lively, and they have been experimenting with ways to encourage participation. Surprisingly, one increasingly popular experiment is giving viewers non-monetary gifts to send, free of charge. Twitch, TikTok LIVE, and Instagram Live all run some version of this.

It is not obvious that the two channels can coexist per economics literature. If a viewer can express appreciation for free, why keep paying? The standard intuition says free gifts should cannibalize paid ones. Signaling theory allows the opposite. If gifts are how viewers signal appreciation publicly, and a free gift earns the same visible recognition as the cheapest paid gift, then the cheapest paid gift stops distinguishing its sender. Viewers who want to stand out must climb to costlier tiers. Free gifts might not replace paid gifts; they might raise the floor everyone signals above. Which force wins is an empirical question, and before this paper there was no causal evidence either way.

A team including Peiyan Yu (UGA Terry), Raveesh Mayya (NYU Stern), and Anindya Ghose (NYU Stern) identifies the platform design conditions under which the second force can win: gifts must be publicly visible in real time, gift tiers must carry different values, and interaction must be synchronous. When those hold, free gifts can complement paid gifts through what the paper calls costly signaling with norm elevation. The boundary condition matters as much as the result. Where these design features are absent, say gifts are private, undifferentiated, or asynchronous, nothing stops cannibalization from dominating, and the paper does not claim otherwise.

## Setting and data

The setting is the video-game live-streaming section of one of Asia's largest streaming platforms. Viewers watch gameplay, chat in real time, and send stickers to streamers. Paid stickers cost real money, and the streamer receives the money minus a platform commission. Every sticker also carries reputation points that accumulate during a session and determine the stream's ranking on the platform homepage: a 10-cent sticker earns 10 points, a 100-cent sticker 100 points, and so on up the tiers.

On November 15, 2019, the platform changed its coin policy. Coins, previously handed out only in rare promotions, began accruing to all viewers automatically as they watched, and coins convert into free stickers. A free sticker transfers no money to the streamer but earns the same 10 reputation points as the cheapest paid sticker. Free-sticker volume exploded from roughly 30 to 40 per viewer-streamer pair per week to over 800. The cheapest paid tier lost its distinctiveness overnight, which is precisely the signaling-dilution condition the theory needs.

The data cover every viewer who sent at least one sticker and every streamer who received one from May 10 to December 10, 2019, about 27 weeks before the policy and 4 weeks after, merged with session metadata, viewer demographics, streamer characteristics, and city-level census controls, and aggregated to a viewer-streamer-week panel.

## The research questions and how they are answered

The main causal question Raveesh Mayya and his coauthors ask is, what happens to a viewer's paid gifting to a streamer once free gifts flood into that relationship? Two identification problems stand in the way. The policy hit the whole platform at once, so no group is untreated. And although the policy has a single date, viewer-streamer pairs experienced the surge in free stickers at different times, a staggered pattern.

The primary design uses that staggering: pairs that have already experienced their free-sticker increase are compared against pairs that will experience theirs later, with propensity score matching on viewer, streamer, and stream characteristics, and viewer-streamer-pair fixed effects. Because staggered designs with two-way fixed effects can go wrong, the paper re-estimates the effect with the Callaway-Sant'Anna estimator, the Borusyak-Jaravel-Spiess imputation estimator, matrix completion, and synthetic difference-in-differences, and runs a Goodman-Bacon decomposition to confirm negative weights are not distorting the baseline.

The complementary design, Temporal Causal Inference, tackles the no-control-group problem directly. Viewers who formed a relationship with a streamer later in the sample are matched to similar pairs from earlier cohorts, whose aligned post periods fall before the policy date in calendar time and are therefore uncontaminated. A machine-learning variant, Temporal Causal Forest, checks that the matching method is not driving the result.

## What the study finds

Free gifts raise paid gifting. In the primary specification, a pair's paid gifting rises by about 1,752 cents of local currency, roughly $2.42 per week, after its free-sticker increase, which aggregates to about $1.13 million per year across the matched sample. The modern staggered-adoption estimators land between 694 and 2,799 cents depending on specification, all significant. The TCI estimates, which capture the average effect across all pairs rather than only those that took up free gifting, are positive and significant as well. Effects hold across viewer tenure, spending history, streamer popularity, streamer gender, and game genre, and do not disproportionately favor already-popular streamers.

The distributional evidence pins down why. Once free stickers carried the same reputation points as the 10-cent sticker, the 10-cent tier collapsed, falling from 46.5 percent to 23.4 percent of paid stickers per session, while the 100-cent tier tripled from 9.2 percent to 33.4 percent. Sessions where the 10-cent sticker was the most common gift dropped from 58 percent to 29 percent; sessions where the 100-cent sticker was most common rose from 7 percent to 36 percent. The whole density of gift values shifted right, not just the tail. A proportional rise across all tiers would suggest viewers simply spending more; the tier-specific substitution, cheapest tier down and higher tier up simultaneously, is the signature of signaling escalation.

There is also early evidence of habit formation. Among viewers who had never sent a paid sticker, the free-sticker experience raised both the probability of starting to pay and the amount paid, consistent with free gifts lowering the barrier into a gifting habit that then sustains itself within the viewer-streamer relationship.

## The LLM agent experiment

One question observational data cannot settle is what an individual viewer would do under controlled variation in what they observe others doing. Randomizing exposure to other viewers' gifting in a live session is infeasible. So, following MIT Professor John Horton's homo silicus approach of using LLMs as simulated economic agents, the authors built a controlled experiment in Horton's Expected Parrot Domain-Specific Language (EDSL) framework: 480 agents spanning four cultural and gender contexts, assigned pre-policy histories as non-gifters, low-tier gifters, or high-tier gifters, facing a within-subject policy change that introduces a free gift, across three conditions that progressively reveal how other viewers are escalating, 1,440 agent sessions in all.

The results track the field data closely. Not a single baseline paid gifter substituted down to the free gift, in any condition, under either GPT-4o or a full replication on GPT-4.1. Instead, 17.5 to 19.4 percent of gifters escalated to higher paid tiers, and escalation rose monotonically as the visibility of others' escalation increased. The agents' own written rationales describe the mechanism unprompted: a single Rose would get lost in the flood of free Glow Sticks, so they upgraded to a Heart to stand out.

LLM surrogacy is easy to do badly, and the authors treat that risk seriously. The design follows the five safeguards that Gao, Lee, Burtch, and Fazelpour lay out in their PNAS paper on the pitfalls of LLMs as human surrogates. Documentation: pinned model versions, temperature, prompts, notebooks, and raw responses all released in the online supplement. Model stability: a fixed seed, deterministic caching, and a full replication on a second model with a different architecture and training pipeline. Data leakage: a fictitious gift economy with invented tier names and point systems that no training corpus contains. Prompt robustness: three visibility conditions, four cultural contexts, and behavioral histories assigned through transaction records rather than persona labels. Self-explanations: agent rationales reported as illustration, never as primary evidence. The paper positions the experiment as one element in a broader evidentiary strategy, not standalone proof, which is exactly the posture Gao and coauthors recommend.

## What it means

For platforms, the finding reverses a natural fear. A free gifting channel, introduced under the right design conditions, is not a leak in the revenue pipeline but a lever that lifts it: the free tier resets the signaling floor, and viewers who care about standing out pay more, not less. The design conditions do the work, though. Real-time public visibility, value-differentiated tiers, and synchronous interaction are what let a free gift dilute a paid signal in the first place. A platform lacking those features should not expect the same complementarity, and the authors are careful to scope the claim accordingly.

Two caveats. The post-policy window is four weeks, so the habit-formation evidence captures initial conversion rather than long-run automaticity, and the authors label it early evidence for that reason. And the study covers one large platform in Asia; the design conditions travel, but the magnitudes may not.

## Where this sits in the broader agenda

The paper extends Raveesh Mayya's research stream on platform policy changes and their consequences, this time on the demand side of creator monetization rather than the supply side of participation rules. It also connects to his generative AI stream: the LLM agent experiment operationalizes the kind of disciplined, reproducible LLM methodology his SILICON work with Cheng and Sedoc argues for, applied here as evidence rather than annotation.

**Full citation:** Yu, P., Mayya, R., and Ghose, A. "Do Nonmonetary Virtual Gifts Enhance or Diminish Voluntary Paid Gifts? Evidence from a Video Game Live-Streaming Platform." Information Systems Research (Articles in Advance). https://pubsonline.informs.org/doi/10.1287/isre.2024.0902
