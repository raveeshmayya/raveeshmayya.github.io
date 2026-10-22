---
title: "Token Tradability as a Form of Platform Deregulation: Intended and Unintended Consequences of a Policy Change"
url: /papers/token-tradability-platform-deregulation/
summary: "Extended narrative summary of the paper by Yuxin Geng, Raveesh Mayya, and Chenshuo Sun (Information Systems Research, conditionally accepted): when a US auction platform let users trade its tokens at a market-determined rate, the token's real value became visible, and supply-side participation fell even as the platform's intended goal was met."
description: "Extended summary of the ISR paper on token tradability and platform deregulation, by Raveesh Mayya (NYU Stern) and coauthors."
searchHidden: true
ShowBreadCrumbs: false
---

**Paper:** Token Tradability as a Form of Platform Deregulation: Intended and Unintended Consequences of a Policy Change

**Authors:** Yuxin Geng (University of Minnesota, Carlson School of Management), Raveesh Mayya (New York University, Stern School of Business), and Chenshuo Sun (Zhongguancun Academy)

**Journal:** Information Systems Research, conditionally accepted

**Finding in one line:** Raveesh Mayya and his coauthors show that when a US peer-to-peer auction platform deregulated its token's exchange rate and let users trade tokens at a market-determined price, the intended goal (curbing excessive bidding) was achieved, but sales fell 14.6 percent and product variety fell 9 percent because the visible market rate shocked users anchored on the token's old nominal value.

**Method contribution:** The paper combines three quasi-experimental designs (regression discontinuity in time, fixed effects, and Temporal Causal Inference) with two controlled experiments: a 300-participant Prolific study and a 640-agent simulation in MIT Professor John Horton's Expected Parrot EDSL framework, run under the methodological safeguards that Gao et al. (PNAS 2025) prescribe for using LLMs as human surrogates.

*This is an extended narrative summary written for readers who want more detail than an abstract offers without reading the full paper.*

## Why this question matters

Digital platforms act as private regulators of their internal economies. They set access rules, fee schedules, and, in many cases, the exchange rate of a platform-specific token: Facebook Credits, Microsoft Points, Amazon Coins, Tencent Q-coins, the Linden Dollar. Platforms have traditionally administered both the token supply and the token-dollar rate, selling tokens at a fixed price and restricting users from cashing out, a design meant to lock users in. The design has a known cost. With uncapped supply and limited burning, tokens accumulate and the platform's internal economy inflates.

An increasingly visible response is deregulation: the platform stops setting the exchange rate and lets a peer-to-peer secondary market discover it. This hands users a bundle of decision rights they never had, including how to monetize accumulated tokens, what price to ask, when and how much to dispose of, and which valuation benchmark to reference. Theory pulls in two directions. Liquidity and autonomy should encourage participation and relieve the pressure that makes users dump tokens through overbidding. But the market-determined rate also makes the token's real value visible. Many users in token economies exhibit money illusion: they organize decisions around the fixed nominal rate rather than actual purchasing power. For them, a visible market rate is a salience shock. They suddenly recognize how much less their balances are worth, even though the balances themselves have not changed. Whether deregulation helps or hurts the platform, and under what conditions, had not been examined empirically before this paper.

## Setting and data

The setting is a US peer-to-peer auction platform, launched in 2009, where users trade used goods (books, collectibles, DVDs, electronics, sporting goods, video games) in auctions settled with platform tokens called credits. Users earned credits by selling items, completing activities like surveys, or buying them from the platform at a fixed rate of 1,000 credits per dollar. There was no way to convert credits back into dollars.

On December 14, 2015, with no advance notice, the platform opened a token exchange where users could sell eligible credits to each other at whatever price they set, with the platform taking a 20 percent fee and displaying the running market rate on the selling page. The platform had two stated objectives: control the inflation endemic to its token economy, and encourage sellers to list more by giving them a way to monetize earnings. The sudden announcement makes the change an exogenous shock to users.

What happened to the exchange rate is visible in the raw data. The nominal rate jumped from 1,000 to over 5,000 credits per dollar and kept depreciating. Notably, the token's real purchasing power had been eroding well before the policy, which shows up in the winning bid prices of Amazon gift cards the platform auctioned: users were already paying far more than 1,000 credits per dollar of face value. The fixed nominal rate had simply been masking the decline. The data cover over 2 million product listings from February 2015 to September 2016, 45 weeks before the policy and 40 weeks after, aggregated to a seller-week panel of 757,945 observations from 8,917 sellers.

## The research questions and how they are answered

The main causal question Raveesh Mayya and his coauthors ask is, what happens to user participation when an administered token rate becomes market-determined? The identification challenge is that the policy hit every user at once, so there is no untreated group. The paper attacks the problem from three angles. A regression discontinuity in time design estimates the short-run jump within a narrow window around the policy date. A fixed-effects model with user and calendar-month fixed effects estimates effects over the full 85-week horizon. And Temporal Causal Inference, built for exactly this no-control-group scenario, matches each user cohort to similar users who joined the platform a few weeks earlier, whose aligned comparison periods fall entirely before the policy date and are therefore uncontaminated.

## What the study finds

The response splits across the two sides of the market, and the split is the paper's core finding. On the buyer side, the number of bids per auction falls 17.4 percent in the short run and 13.4 percent over the longer horizon. This is what the platform wanted. Users who had been overbidding on items just to burn down oversized token balances could now liquidate directly instead. On the seller side, the platform got the opposite of what it wanted: weekly sales fall 14.6 percent and the variety of product categories listed falls 9 percent, with all three estimation strategies agreeing. A platform that lives on transaction volume set out to stimulate listings and instead suppressed them.

The category detail sharpens the picture. Ten of thirteen major categories decline, led by toys, health and beauty, and electronics, which are experience goods with uncertain resale values. The three categories that hold steady (movies and music, video games, home and garden) are search goods that are easy to value, and largely digitally deliverable. Sellers did not leave at random. They retreated toward products whose remaining uncertainty was easiest to price, a risk-mitigation strategy in a marketplace where token-value uncertainty now compounded the auction uncertainty they already faced.

## The salience mechanism

Why would sellers pull back when they gained a new right? The paper's answer is a salience shock, and it tests the idea from several directions.

First, users who already knew the token's real value should not be shocked. The paper identifies well-informed users through their pre-policy gift card purchases, since gift cards have a printed dollar face value that reveals what a credit actually buys. These users are not significantly affected by the policy. Second, a placebo. In late 2014, the platform reinstated gift card trading without touching the exchange rate. Nothing happened to participation, which says tradability by itself is not what moved behavior; the visible market rate is. Third, the shock should scale with exposure. It does: users holding the largest pre-policy token balances, for whom the gap between nominal and real wealth was widest, cut their sales and variety the most. Fourth, the paper traces an amplification loop. Impatient users who had previously overbid on gift cards to dispose of credits reduce participation the most sharply after the policy, consistent with these users liquidating tokens at discounted prices, which deepened the visible depreciation and kept the shock salient for everyone else.

## The two controlled experiments

The field evidence cannot fully separate salience from everything else that moved after the policy, so the paper runs two experiments that manipulate salience directly. In a 300-participant Prolific study, subjects see one of three transaction histories before a selling task: items priced in credits only, items plus gift cards showing both dollar and credit prices, or items plus explicit credit-for-cash trades. Participants who saw credits only stayed anchored on the nominal 1,000-per-dollar rate and listed their item at less than half the price of the informed groups. When the real rate was then revealed, 86 percent of them reported being surprised, against roughly half in the informed groups, and their willingness to keep using the platform dropped.

Because human subjects can absorb only so much policy context, the paper complements this with 640 simulated economic agents built under John Horton's homo silicus paradigm in the Expected Parrot EDSL framework. Uninformed agents, anchored to the nominal rate through their assigned purchase histories, receive the same salience shock the field users did and face an incentive-compatible choice between listing an item and a guaranteed outside option. Uninformed agents refuse to list at far higher rates than informed agents: 89.4 versus 13.1 percent under GPT-4o, 22.5 versus 0.6 percent under DeepSeek Reasoner, an architecturally distinct model. The design follows the methodological safeguards of Gao, Lee, Burtch, and Fazelpour's PNAS paper on LLMs as human surrogates, covering documentation, model stability, data leakage, prompt robustness, and self-explanations.

## What it means

For platform managers, the lesson is not that deregulation fails. It is that deregulating an administered token rate without stabilization safeguards lets the salience shock reach users at full force. The paper scopes this with four boundary conditions: an administered rate with an accumulated gap between nominal and real value, a meaningful share of nominally anchored users, demand-discovery pricing that prevents sellers from absorbing the shock through repricing, and the absence of strong stabilization tools. Where any of these fails, the prediction changes. A posted-price marketplace, for instance, would let sellers reprice instead of withdraw. The paper recommends concrete levers: phased rollout starting with users already exposed to the real rate, trading guardrails such as price bands and progressive limits (Second Life's LindeX exchange is a working precedent), market-maker and supply management, seller-side support in high-uncertainty categories, and pre-transition transparency that displays dollar equivalents alongside token prices before deregulating.

Two caveats. Privacy restrictions kept the secondary exchange's transaction-level data out of reach, so the impatient-seller cascade is inferred from aggregate patterns rather than traced trade by trade. And the setting is a platform that deregulated after years of token accumulation; a token tradable from inception, with no anchor to disrupt, might behave differently.

## Where this sits in the broader agenda

The paper extends Raveesh Mayya's research stream on platform policy changes and their unintended consequences, and continues the multi-method approach of his virtual gifting work, which likewise pairs quasi-experimental field evidence with LLM agent experiments under the homo silicus paradigm. This paper is also personally meaningful for him: he is the senior-most author, Yuxin Geng was a sophomore at Tsinghua University when the research started, and he is now a PhD student at the University of Minnesota Carlson School of Management.

**Full citation:** Geng, Y., Mayya, R., and Sun, C. "Token Tradability as a Form of Platform Deregulation: Intended and Unintended Consequences of a Policy Change." Information Systems Research, conditionally accepted. https://papers.ssrn.com/abstract=4766534
