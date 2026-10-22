---
title: "Growing Platforms by Adding Complementors without a Contract"
url: /papers/growing-platforms-without-contract/
summary: "Extended narrative summary of the paper by Raveesh Mayya and Allen Li (2025, Information Systems Research): what happens when a food delivery platform lists restaurants without a contract, and what happens when a regulator forces it to stop."
description: "Extended summary of the Information Systems Research paper on Grubhub's non-partnered restaurant strategy, by Raveesh Mayya (NYU Stern) and Zhuoxin (Allen) Li (Wisconsin)."
searchHidden: true
ShowBreadCrumbs: false
---

**Paper:** Growing Platforms by Adding Complementors without a Contract

**Authors:** Raveesh Mayya (New York University, Stern School of Business) and Zhuoxin (Allen) Li (Wisconsin School of Business)

**Journal:** Information Systems Research, 36(6), 1670-1690, 2025

**Finding in one line:** Raveesh Mayya and Allen Li show that when Grubhub listed over 150,000 restaurants without contracts, both the listed restaurants and the platform's contracted restaurants gained takeout revenue; California's ban on the practice reversed the gains and hurt the independent restaurants it was meant to protect.

*This is an extended narrative summary written for readers who want more detail than an abstract offers without reading the full paper.*

## Why this question matters

Digital marketplaces grow by attracting participants on one side and hoping the other side follows. The standard way to build the supply side is a formal contract: the restaurant signs up, pays a commission on each order, and in return controls its menu, its prices, and its presence on the app. Two decades of platform economics built its playbook on that arrangement. The models assume the participants a platform attracts are active. They sign contracts. They curate listings, set prices, run promotions. Why would a platform bother adding participants who do none of this?

It turns out a platform might not need them to be active. Think of financial markets. A contract market involves binding agreements with defined terms; a spot market involves immediate transactions with no prior commitment. The first generation of platform research implicitly modeled a contract market on the supply side. A platform that lists suppliers who never signed anything, and uses a third side of the market to make those listings functional, is running something closer to a spot market for suppliers. Whether cross-side network effects survive when one side is populated by passive participants was an open question.

Around 2019, Grubhub ran exactly this experiment. It listed restaurants that had never agreed to appear and used third-party couriers to bridge the gap. The courier places the order through the restaurant's ordinary channels, pays with a platform-issued card, and delivers the food. The restaurant pays no commission and often has no idea it is on the app. In the last quarter of 2019 Grubhub added over 150,000 such "non-partnered" restaurants, on a platform that had listed about 105,000 restaurants in all of 2018. Restaurants complained. Some sued. In September 2020 California passed the Fair Food Delivery Act, the first US law requiring delivery platforms to obtain a formal agreement before listing a restaurant.

Raveesh Mayya, a faculty at NYU Stern, and Zhuoxin (Allen) Li, a faculty at the Wisconsin School of Business, turn these two events into a pair of natural experiments, one that switches the strategy on and one that switches it off. Does being listed without consent hurt or help the listed businesses? What does the arrival of thousands of passive competitors do to the partnered restaurants already paying commissions? When the regulator forces removal, who bears the cost? Nobody had answered these questions with data.

## Setting and data

Raveesh Mayya and Allen Li assemble a monthly panel of 115,889 restaurants across California, Oregon, and Washington: 36,749 partnered with Grubhub, 27,966 non-partnered, and 51,174 never on the platform, from September 2019 through March 2021. Three data sources are triangulated. Foot traffic comes from SafeGraph, with a takeout visit defined as one lasting under ten minutes, since diners and couriers picking up food rarely linger longer. Partnership records come from Grubhub itself, with exact dates of addition and removal. Revenue comes from anonymized, aggregated Visa card transactions observed monthly per restaurant. Table 1 of the paper defines the variables and Table 2 reports summary statistics; Figure 1 diagrams how an order flows through a non-partnered restaurant, with the courier standing in for the missing contract.

How Grubhub assigned treatment matters for identification. Its selection rule was crude by design, any restaurant with a menu available online was a candidate, and the delisting came from a state law rather than from the restaurants themselves. Both events approximate the random assignment that causal inference needs. Appendix Figure A1 shows similar pre-event foot traffic across partnered, non-partnered, and never-listed restaurants, consistent with mass inclusion rather than cherry-picking. Before the regulation took effect, roughly 40 percent of Grubhub's California listings were non-partnered.

## The research questions and how they are answered

The main causal question Raveesh Mayya and Allen Li ask is, what happens to a restaurant when Grubhub lists it without a partnership, and what happens to nearby partnered restaurants when it does? The core design is difference-in-differences. Because Grubhub added restaurants in waves, the listing analysis uses a staggered treatment design: each month, newly listed non-partnered restaurants were matched one-to-one to never-listed controls in the same zip code and restaurant category with similar pre-treatment visit patterns, yielding 7,000 treated restaurants and 7,000 matched controls analyzed with two-way fixed effects. Staggered designs have known econometric pitfalls, so the paper also runs a matrix completion estimator (Figure 2 plots it beside the event study), the newer staggered-DiD estimators of Callaway and Sant'Anna and of Sun and Abraham (Appendix Figure A3), a Goodman-Bacon decomposition (Appendix Figure A4), and a 500-draw placebo test whose estimates center on zero while the true effect sits far in the tail (Figure 3).

The spillover analysis asks what happens to a partnered restaurant when the first non-partnered restaurant appears in its zip code. To keep demand from leaking between treated and control units, matched pairs are at least about one mile apart, constructed with Uber's H3 hexagonal grid, while still sharing a zip code so both face the same local rules. The delisting analysis is a conventional difference-in-differences around September 24, 2020, when California's law was signed and non-partnered restaurants in the state were removed.

## What the study finds

Being listed without a contract helps the listed restaurants. Raveesh Mayya and Allen Li find that non-partnered restaurants gained about 41 additional normalized takeout visits per month after inclusion (Table 3, Panel A). At the industry's average delivery order of $34.37, that is roughly $1,410 in extra monthly revenue, earned without paying any commission; a log specification puts the increase at about 4 percent of takeout volume. Independents drive the result; chains show insignificant changes. A mechanism analysis in Table 4 shows that restaurants in the top quartile of pre-period takeout volume gained the most, about $3,923 per month more than bottom-quartile restaurants, and about $6,239 among independents. The listing worked like free advertising. Restaurants that had invested in takeout operations but stayed off the platform, perhaps deterred by commission fees, converted the new visibility into orders.

The second finding runs against the intuition that new listings steal demand from old ones: partnered restaurants benefited too. When non-partnered restaurants appeared in a partnered restaurant's zip code, its takeout visits rose by about 71 normalized visits per month, roughly $2,430 in revenue (Table 5, Figure 4). A thicker marketplace attracted more diners, and their orders spilled over onto the restaurants already there. Again the benefit concentrated among independents, and Appendix Table A9 shows the spillover holds whether the nearby non-partnered restaurants were chains or independents.

The delisting results complete the argument. When California forced Grubhub to remove non-partnered restaurants, those restaurants lost about 14 normalized takeout visits per month, roughly $492 in revenue (Table 6, Figure 5). The loss fell on independent restaurants; chains showed no significant decline. Partnered restaurants in California saw negative but mostly insignificant visit effects, with a significant revenue decline in Appendix Table A11. The delisting loss is smaller than the listing gain, an asymmetry Mayya and Li attribute to customer relationships formed during the listing period that partially survived the removal.

## What it means

For platforms, the study shows that inorganic supply growth can be incentive-compatible. The platform gains selection, couriers gain work, consumers gain variety, and the unwitting suppliers gain orders. Same-side competition did not bite because the listing wave changed what the platform was for its users; a diner who finds nearly every neighborhood restaurant on the app treats it as the default way to order food, which generates orders for partnered and non-partnered restaurants alike. The spot-market analogy holds here too: in financial markets, spot liquidity strengthens the contract market by signaling a thick, active marketplace, and the non-partnered listings played that role for Grubhub's contracted supply.

For regulators, the lesson is about choice. California's Fair Food Delivery Act prohibited platforms from listing restaurants without consent, and the principle is sound. But the ban removed the choice along with the harm. The small, independent restaurants the law aimed to protect lost a free channel to reach consumers, and partnered independents nearby lost orders as the thinner supply side made the platform less compelling for diners. Perhaps the right response is not a ban but a framework: require restaurant consent, ensure pricing transparency, establish liability guidelines, and let restaurants decide what arrangement works for them. The design space for platform growth is larger than the literature acknowledged, and so is the space for getting regulation right.

Two caveats. The strategy works where a courier can order through a restaurant's ordinary channels and physically pick up the product; platforms whose complementors sell digital goods or need technical integration cannot copy it. And the outcomes measure takeout revenue, not full profit and loss, so reputational costs from outdated menus or cold food remain unpriced.

## Where this sits in the broader agenda

The paper belongs to Raveesh Mayya's research stream on platform policy changes and their consequences, which examines how platforms adjust the rules of participation in two-sided markets and how suppliers absorb those adjustments. It pairs a platform-initiated policy with its regulatory reversal in a single setting, a combination that rarely appears in the literature.

**Full citation:** Mayya, R., and Li, Z. (2025). Growing Platforms by Adding Complementors without a Contract. *Information Systems Research*, 36(6), 1670-1690. Published February 20, 2025. An open-access version is available from the journal.
