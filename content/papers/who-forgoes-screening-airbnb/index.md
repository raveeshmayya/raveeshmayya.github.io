---
title: "Who Forgoes Screening in Online Markets and Why? Evidence from Airbnb"
url: /papers/who-forgoes-screening-airbnb/
date: 2026-08-25T23:40:39+05:30
paper:
  authors:
    - name: "Raveesh Mayya"
      self: true
      affiliation: "New York University, Stern School of Business"
    - name: "Shun Ye"
      affiliation: "George Mason University, Costello College of Business"
    - name: "Siva Viswanathan"
      affiliation: "University of Maryland, Smith School of Business"
    - name: "Rajshree Agarwal"
      affiliation: "University of Maryland, Smith School of Business"
  venue: "MIS Quarterly"
  year: 2021
  volume: 45
  issue: 4
  pages: "1745-1776"
  doi: "10.25300/misq/2021/15335"
  status: "Published"
summary: "Extended narrative summary of the paper by Raveesh Mayya, Shun Ye, Siva Viswanathan, and Rajshree Agarwal (2021, MIS Quarterly): why Airbnb hosts voluntarily give up their right to screen guests, and what happens when they do."
description: "Extended summary of the MIS Quarterly paper on Airbnb's Instant Book feature and the economics of forgoing screening, by Raveesh Mayya (NYU Stern) and coauthors."
searchHidden: true
ShowBreadCrumbs: false
---

**Paper:** Who Forgoes Screening in Online Markets and Why? Evidence from Airbnb

**Authors:** Raveesh Mayya (New York University, Stern School of Business), Shun Ye (George Mason University, Costello College of Business), Siva Viswanathan (University of Maryland, Smith School of Business), and Rajshree Agarwal (University of Maryland, Smith School of Business)

**Journal:** MIS Quarterly, 45(4), 1745-1776, 2021

**Finding in one line:** Raveesh Mayya and his coauthors show that Airbnb hosts who voluntarily gave up screening their guests through Instant Book gained about 1.79 booked nights and $300 in revenue per month at the cost of slightly lower ratings, with the largest gains going to Black and female hosts.

**Method contribution:** An LSTM classifier trained on 9,925 hand-tagged statements from guest reviews, reaching over 90 percent accuracy, applied to sort positive mentions and six complaint categories across more than 491,000 comments.

*This is an extended narrative summary written for readers who want more detail than an abstract offers without reading the full paper.*

## Why this question matters

In peer-to-peer markets, both sides of a transaction are typically individuals. A guest booking a spare room on Airbnb is trusting a stranger; so is the host accepting the request. The textbook answer to this information asymmetry is screening. Each side inspects the other's profile, history, and reviews, and rejects counterparties who look like poor matches. Screening is treated as a necessity in peer-to-peer market design, the mechanism that keeps adverse selection from unraveling the market.

But screening cuts both ways. Most research on its downsides looks at one direction, hosts screening guests: studies document hosts rejecting guests based on name or clients in labor markets filtering workers by gender. The reverse direction, providers facing bias from the buyers who screen them, has drawn far less attention. A mechanism built to filter bad matches can also filter people, on either side.

Then there is a puzzle the literature had not touched. Some providers voluntarily give up their right to screen. In 2014 Airbnb popularized Instant Book, a setting that lets a host automatically accept every booking request. Car owners on Turo and dog sitters on DogVacay have the same option. A host who enables it accepts more risk of a bad guest and forfeits the protection screening provides. Why would anyone do that? Who does it, and what happens to them afterward?

A research team comprising Raveesh Mayya (NYU Stern), Shun Ye (GMU Costello), Siva Viswanathan (UMD Smith), and Rajshree Agarwal (UMD Smith) takes up both questions. Figure 1 of the paper lays out the framework: first the antecedents, meaning which listings and hosts are likely to forgo screening, then the consequences for occupancy, price, and review ratings. Nobody had studied the voluntary abandonment of screening with data.

## Setting and data

The setting is Airbnb in New York City, the largest Airbnb market in the United States. Under traditional booking, screening runs both ways. The guest screens listings and sends a request; the host screens the guest and accepts or declines. Under Instant Book the host waives the second step while guests keep screening as before. Appendix Figure A1 of the paper shows the two flows side by side.

Raveesh Mayya and his coauthors assemble a panel of all New York City listings from August 2015 through February 2017, combining public Airbnb data with proprietary records from a business intelligence firm. After excluding listings priced above $1,000 a night and listings present for under a year, the sample holds 13,757 listings and 196,155 listing-month observations. The average listing is available 24.5 days a month, charges $167.87 a night, and sits at 54 percent occupancy. About 16 percent of listings use Instant Book, and 96 percent of listings that switch do so at most once, which says the choice is a considered one rather than something hosts toggle month to month. Table 1 defines the variables; Tables A1 and A2 report summary statistics and correlations.

To investigate heterogeienty based on race and gender, the authors code each host's race and gender manually from displayed profiles, then validate a 20 percent random sample against two algorithmic approaches, one based on names and one based on profile photos. Agreement runs 93.75 percent for race and 99.46 percent for gender. In the sample, 55.73 percent of hosts are White and 12.44 percent are Black, with a roughly 53:47 female-to-male ratio, figures in line with prior Airbnb studies (Table 2).

## The research questions and how they are answered

Raveesh Mayya and his coauthors ask two questions: who forgoes screening, and what happens to those who do? The first question, who forgoes screening, is answered with a logit model of the monthly decision to switch to Instant Book (Table 3). The second question needs causal inference, and here the challenge is that hosts self-select into switching. The paper pairs propensity score matching with difference-in-differences. Each switching listing is matched one-to-one, without replacement, to a non-switching listing with a similar propensity score in the month before the switch, and the match must sit within three miles of the treated listing so that neighborhood conditions are comparable. Appendix Table A4 confirms the matched groups are balanced on covariates, and Table 4 shows the race and gender composition of the sample survives the matching.

Outcomes are then estimated with three-stage least squares (3SLS) in a three-equation system covering occupancy, price, and rating, with each equation instrumented against the others using Hausman-type instruments built from the prices and occupancies of a listing's twelve nearest competitors. Robustness checks swap in coarsened exact matching (Appendix Table A8), a collapsed two-period design (Appendix Table A7), look-ahead matching (Appendix Table A9), and alternative covariate sets, all with consistent results. Appendix Figure A2 shows the treated and control groups tracking each other before the switch, and Appendix Table A6 formally fails to reject parallel trends.

## What the study finds

On the antecedents, the pattern is demand-driven. Listings with mid-range occupancy, recent declines in occupancy, or recent price declines are the likeliest to forgo screening (Table 3). Newer hosts, professional hosts, non-Superhosts, and hosts whose local competitors have already enabled Instant Book are also more likely to switch. In short, hosts give up screening when they need bookings. Two demographic patterns sit on top of this. Black hosts are more likely to forgo screening than White hosts, and female hosts more likely than male hosts. The female finding is interesting because screening reads as protection, and female hosts might be expected to hold onto it. One plausible reading is that Instant Book settles expectations upfront: booking is automatic and the host is not part of the transaction, so guests who want a host on hand select themselves out before the stay begins.

On the consequences, Raveesh Mayya and his coauthors find that forgoing screening pays. Occupancy rises by 13.52 percent, about 1.79 additional booked nights per month, with no change in listing price, which works out to roughly $300 in extra monthly revenue (Table 5, Figure 2). The cost shows up in review ratings, which fall by 1.078 points, about 1.2 percent, consistent with letting in some poorly matched guests.

The heterogeneity results carry the paper's second punch. Black hosts gain more from forgoing screening than White hosts, an 18.37 percent occupancy improvement against 14.62 percent, and their ratings fall less, 0.28 percent against 1.56 percent (Table 6, Figure 3). Female hosts match male hosts on occupancy gains, but male hosts cut prices by $4.28 after switching while female hosts do not, so female switchers end up gaining about $56.62 more in monthly revenue than male switchers. Tables 7 and 8 trace the explanation to where switchers sit in their group's quality distribution. Hosts who switch tend to come from the better part of their own group's distribution, and the more selective that sorting, the larger the gains from switching. The review-comment evidence behind this comes from a text mining exercise. The authors hand-tagged 9,925 statements from guest comments as positive mentions or one of six complaint types, trained an LSTM classifier that reaches over 90 percent accuracy, and ran it over more than 491,000 comments; complaint rates stay statistically flat across host groups while positive mentions favor the groups whose switchers gained most (Table 7). Since guests can typically see a host's photo, the authors suggest that guests seem to trade off any taste-based bias for the convenience of instant booking.

The falsification analyses reinforce the story. Listings that suffer larger rating drops after switching are more likely to switch back to traditional booking, while Black hosts are more likely than White hosts to keep Instant Book on (Appendix Table A10). Table 9 collects all the findings in one place.

## What it means

Raveesh Mayya and his coauthors argue that the result revises a default assumption in market design. Screening had been treated as necessary infrastructure for peer-to-peer markets. This study shows that letting participants opt out of screening can be beneficial, because each provider runs their own cost-benefit calculus against their own demand conditions. A host with empty nights values the extra bookings more than the protection; a host with a full calendar keeps the filter. The mechanism works because it is a choice, not a mandate.

The social finding is the sharper one. Airbnb introduced Instant Book partly in response to concerns about how hosts were screening guests. This paper shows the feature also works in the other direction. Black and female hosts are both more likely to adopt instant booking and better rewarded for it, because the feature lets a booking happen before any bias on the guest's side can enter the decision. A design change aimed at one side of the market turned out to be a tool for the other side as well. Platform designers weighing mechanism changes tend to count efficiency effects; this result says the distributional effects across host groups belong in the same ledger.

Two caveats. The sample is New York City over nineteen months, and dynamics could differ in other cities or on platforms where switching is costly or restricted. And the data cover hosts, not guests, so the study cannot observe which guests select into instantly bookable listings or pin down the exact source of the bias in their behavior.

## Where this sits in the broader agenda

The paper belongs to Raveesh Mayya's research stream on platform policy changes and their consequences, which examines how platforms adjust the rules of participation in two-sided markets and how participants respond. Here the policy is a screening option rather than a listing strategy, and the response runs through the supply side's own choices, with distributional consequences the platform likely did not forecast.

**Full citation:** Mayya, R., Ye, S., Viswanathan, S., and Agarwal, R. (2021). Who Forgoes Screening in Online Markets and Why? Evidence from Airbnb. *MIS Quarterly*, 45(4), 1745-1776.
