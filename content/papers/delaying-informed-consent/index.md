---
title: "Delaying Informed Consent: An Empirical Investigation of Mobile Apps' Upgrade Decisions"
url: /papers/delaying-informed-consent/
date: 2026-08-25T23:40:39+05:30
paper:
  authors:
    - name: "Raveesh Mayya"
      self: true
      affiliation: "New York University, Stern School of Business"
    - name: "Siva Viswanathan"
      affiliation: "University of Maryland, Smith School of Business"
  venue: "Management Science"
  year: 2025
  volume: 71
  issue: 8
  pages: "7113-7135"
  doi: "10.1287/mnsc.2022.00334"
  status: "Published"
summary: "Extended narrative summary of the paper by Raveesh Mayya and Siva Viswanathan (2025, Management Science): what happens when apps delay adopting a privacy policy, and a reusable method for estimating app downloads from public Play Store data."
description: "Extended summary of the Management Science paper on delayed privacy policy adoption in the Android ecosystem, by Raveesh Mayya (NYU Stern) and Siva Viswanathan (UMD Smith), including the download estimation method."
searchHidden: true
ShowBreadCrumbs: false
---

**Paper:** Delaying Informed Consent: An Empirical Investigation of Mobile Apps' Upgrade Decisions

**Authors:** Raveesh Mayya (New York University, Stern School of Business) and Siva Viswanathan (University of Maryland, Smith School of Business)

**Journal:** Management Science, 71(8), 7113-7135, 2025

**Finding in one line:** Raveesh Mayya and Siva Viswanathan show that apps overreaching for permissions, mostly to serve targeted ads, exploit the time flexibility platforms grant for adopting privacy policies; studying this in the context of Android's switch from download-time to runtime permissions, they estimate that apps delaying adoption face marketplace consequences of roughly 350,000 lost downloads and 2,744 lost rating stars.

**Method contribution:** A validated technique for estimating an app's actual downloads from publicly visible Play Store data, using download-bucket jumps and rating counts, accurate to about 1 percent against proprietary download records.

*This is an extended narrative summary written for readers who want more detail than an abstract offers without reading the full paper.*

## Why this question matters

Consumers have grown increasingly vocal about who gets access to their personal data, when, and on what terms. Every data breach and tracking scandal has sharpened the demand. People no longer accept that using a digital product means surrendering their information wholesale. Regulators responded with laws like GDPR and CCPA, which mandate uniform, time-bound compliance. Platforms responded too, rewriting their own rules around the principle of informed consent, the requirement that an app ask before it collects, with Apple's App Tracking Transparency and Android's permission overhauls as the prominent examples.

Where a regulation sets a deadline, a platform typically grants its developers a window. Android 6.0, released in late 2015, is a clean example. Before Android 6.0, a user granted an app every permission it listed in one take-it-or-leave-it screen at install; after it, permissions became runtime choices, requested individually while the app runs, and refusable one by one. Figure 1 of the paper illustrates the shift. Apps got roughly a three-year grace period to adopt the new model, during which non-upgraded apps kept running normally.

That flexibility is well-intentioned. Forcing overnight compliance can hurt developers' revenue and innovation. But flexibility hands complementors a choice, and choices invite strategy. An app that delays the upgrade keeps collecting data under the old all-or-nothing consent for years. Nobody had measured what that delay costs the app, or asked what kind of app finds the delay worthwhile.

Raveesh Mayya, a faculty at NYU Stern, and Siva Viswanathan, a faculty at UMD Smith, answer both questions. Along the way they solve a measurement problem that had limited app-economy research for years: the Play Store does not publish download counts.

## Setting and data

The dataset was hand-built rather than purchased, in the tradition of empirical IO work that constructs its own panel. Raveesh Mayya and Siva Viswanathan installed 16,705 popular free Android apps on emulators mimicking a Samsung Galaxy Tab 3 and re-scanned them monthly from April 2016 to March 2018, using a custom-built Android app that reads the emulator's database to record each app's upgrade status and full permission list. The main panel covers 13,691 apps present on the Play Store for at least 14 of the 24 months. Monthly snapshots add download buckets, ratings, comment counts, categories, descriptions, and revenue models. Appendix B details how the sample tracks the global app population.

The downloading of apps was important because upgrade timing is invisible in public metadata. Only by holding the app on a device and watching it can you date when a developer actually upgraded the app by "targeting" the latest Android version. When an app targeted Android 6.0 or above, they had to adopt runtime permissions.

## Estimating downloads from public data

The Play Store shows download buckets, not numbers. An app displays "500,000+" until it crosses the next threshold and displays "1,000,000+". Prior work established that rating counts track downloads closely. The paper combines the two facts into an estimator, described in Section 3.1 and Appendix C.

The logic runs as follows. Watch the store monthly. When an app jumps from one bucket to the next, you know its cumulative downloads at that month almost exactly: the lower bound of the new bucket. An app moving from 100,000+ to 500,000+ in June 2016 had very close to 500,000 downloads at that jump. At that month, divide downloads by the app's rating count to get a download-per-rating ratio. If the app jumps again later, compute the ratio again; for the months in between, interpolate the ratio. Multiplying the interpolated ratio by the observed rating count in any month yields that month's download estimate. Table C1 walks through a worked example.

In the panel, 62.43 percent of apps (8,730) jumped a bucket at least once, so the method applies to them directly. For apps that never jumped, the paper borrows the average download-per-rating ratio of the app's category and bucket, estimated from bucket jumps in a global database of over two million apps, and all models are rerun with and without these apps.

Authors use thorough accuracy checks. Within the panel, 96.96 percent of the monthly estimates fall inside the app's actual displayed bucket, and the rest miss by about 3.6 percent. Against ground truth, actual download records purchased from a business intelligence firm, the estimates deviate by about 1.049 percent (Appendix C2). Any researcher observing the Play Store at regular intervals can reproduce the pipeline with public data.

## The research questions and how they are answered

The main causal question Raveesh Mayya and Siva Viswanathan ask is, what happens to an app's marketplace outcomes when it delays the upgrade? Apps that upgraded during the panel are the treated group; propensity score matching pairs each with a control app that had not upgraded by the panel's end, with exact matching on download bucket and category, yielding 2,504 matched pairs. Figure 2 shows the parallel pre-trends. A difference-in-differences model estimates the effect of upgrading, and a three-way interaction with a Late Upgrader dummy separates apps that adopted promptly from those that dragged (Table 3). Robustness checks include synthetic DiD (Table A5), simultaneous estimation (Table A7), and a self-selection correction (Table A8).

The second question they ask is, who delays and why? Following methods from the computer security literature, the authors group apps by functionality and flag permissions that most apps in a group request as essential, and rarely requested ones as potential overreach (Figure 3). A Cox proportional hazards model then tests whether overreaching apps postpone upgrading (Table 5), with text mining of app descriptions used to trace the motive (Appendix F).

## What the study finds

Upgrading promptly pays and delaying costs. Timely upgraders gained both downloads and ratings. Late upgraders lost roughly 350,000 downloads, which translates to an annual revenue loss between $0.25 million and $1.25 million for an average app, and about 2,744 rating stars (Table 3).

Part of the cost comes from Android's search algorithm, which penalizes poorly maintained apps. Rebuilding each app's monthly position in the Play Store's similar-apps network with a PageRank-style centrality measure, the authors find delaying reduces app popularity by 13.76 percent (Table 4, Panel A). Users notice too. Apps that deny them the option to refuse individual permissions pay for it in ratings. Frequent maintenance softens the blow without eliminating it, since well-maintained late upgraders still lose about 3.43 percent of downloads (Table 4, Panel B).

The authors study if this delay is strategic in nature. First they need to know which apps overreach, meaning which apps seek permissions that are not necessary for their core functionality. Following the security literature, they group apps into peers with similar functionality using the granular IAB advertising taxonomy, and code a permission as essential only if at least 80 percent of an app's peers request it; anything below that threshold is nonessential. A navigation app asking for GPS is essential. A navigation app asking for call logs is not. Each nonessential permission an app requests lowers its monthly likelihood of upgrading by 2.7 percent, and Kaplan-Meier estimates show overreaching apps delay about four months longer than their peers (Figure 4). Text mining points to targeted in-app advertising as the motive behind the overreach (Table 6). Operational explanations fall flat: apps with ample resources to upgrade delayed anyway, and a falsification test shows the same apps happily adopted a version upgrade that carried no permission restrictions (Table A13).

## What it means

For platform designers, the finding cuts both ways on flexibility. Too little time hurts legitimate developers. Too much invites strategic delay, since ample time does not by itself persuade a data-hungry app to comply. The paper's answer is to pair time flexibility with algorithmic penalties, and to make sure developers know the penalties exist. An app weighing four more months of unrestricted data collection against a six-figure revenue loss can only make that trade sensibly if the cost is visible.

Developers get hard numbers on a tradeoff that had been folklore. Delaying compliance keeps an app collecting data under the old all-or-nothing consent, and Raveesh Mayya and Siva Viswanathan measure what that costs in downloads, revenue, and reputation.

For researchers, the download estimator is the durable tool. Downloads are the central outcome variable of the app economy, and the paper shows how to recover them from public data with about 1 percent error, no proprietary feed required.

Two caveats. The setting is free apps on Android, whose reliance on data monetization makes them the sharpest case. Paid apps face a different calculus. And the panel covers one policy transition on one platform, so the size of the penalties may differ for other policy changes, even if the strategic logic carries over.

## Where this sits in the broader agenda

The paper belongs to Raveesh Mayya's research stream on platform policy changes and their consequences, which examines how platforms adjust the rules of participation and how complementors respond. Here the response is about timing. Given flexibility on when to comply, complementors sort themselves by their appetite for user data, and the ones that delay are the ones the policy was aimed at.

**Full citation:** Mayya, R., and Viswanathan, S. (2025). Delaying Informed Consent: An Empirical Investigation of Mobile Apps' Upgrade Decisions. *Management Science*, 71(8), 7113-7135.
