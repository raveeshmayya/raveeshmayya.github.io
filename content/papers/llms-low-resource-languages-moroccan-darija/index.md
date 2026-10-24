---
title: "Enhancing LLM Performance in Low-Resource Language Settings: Evidence from Moroccan Darija"
url: /papers/llms-low-resource-languages-moroccan-darija/
summary: "Extended narrative summary of the working paper by Badr-Eddine Lahsini and Raveesh Mayya: a frontier LLM writes acceptable Moroccan Darija 91.6 percent of the time in Arabic script but only 14.6 percent in Latin script, and drafting in Arabic script before transliterating lifts Latin-script acceptability to 89 percent."
description: "Extended summary of the working paper on LLM performance in Moroccan Darija, a low-resource language written in Arabic and Latin script, by Raveesh Mayya (NYU Stern) and Badr-Eddine Lahsini (UM6P Africa Business School)."
searchHidden: true
ShowBreadCrumbs: false
---

**Paper:** Enhancing LLM Performance in Low-Resource Language Settings: Evidence from Moroccan Darija

**Authors:** Badr-Eddine Lahsini (Mohammed VI Polytechnic University, Africa Business School, Morocco) and Raveesh Mayya (New York University, Stern School of Business)

**Status:** Working paper (draft dated September 8, 2026)

**Findings in three sentences:** In low-resource language settings where a language is natively written in two scripts, Raveesh Mayya and Badr-Eddine Lahsini first document a generation disparity, with a frontier LLM writing acceptable Moroccan Darija 91.6 percent of the time in Arabic script but only 14.6 percent of the time in Latin script. Their fix, staged generation, drafts the reply in Arabic script and then transliterates it into Latin script in a single call, which raises Latin-script acceptability to 89 percent. A crossover-design field experiment with 108 native Darija speakers confirms the gain, as raters accept 81.0 percent of staged Latin-script replies against 15.3 percent of directly generated ones.

**Method contribution:** A staged generation pipeline, run on a commercial LLM with no fine-tuning, that drafts the reply in Arabic script, transliterates it into Latin script in a single call, and screens the result against a hand-built lexicon of known wrong word forms. A reverse control that drafts in Latin script and transliterates into Arabic lowers Arabic-script acceptability. This confirms that the disparity arises in generation, since the gain exists only when the draft is written in the script the model writes reliably. Token-level confidence traces show the model is least confident when composing in Latin script. The field test is a crossover experiment in which each of the 108 native Darija raters judges all four conditions and serves as their own control, and four rotating lists put every comment under every condition, so differences between raters and between comments drop out of the comparison.

*This is an extended narrative summary written for readers who want more detail than an abstract offers without reading the full paper.*

## Why this question matters

Firms increasingly hand frontline customer work to large language models, and replying to online reviews is a natural fit. Reviews are short and plentiful, and later customers read the replies too. A usable reply must be in the customer's own language, spelled so a native speaker accepts it, and grammatical. English and Mandarin clear that bar easily. Low-resource languages, those with little digitized text for training models, often do not. The model drifts into English or French mid-sentence (code-switching), mixes one script with another (script mixing), or spells words in ways no native speaker would. For most businesses, these blemishes mean the tool never gets a chance.

Raveesh Mayya and Badr-Eddine Lahsini ask whether this means the model does not understand the language. Earlier research finds that LLMs read better than they write, and that the gap is widest in low-resource languages. Children, too, understand words months before they can say them. If the same comprehension-production asymmetry is at work here, a bad reply may come from a model that knows what to say and fails at writing it out. But a finished reply fuses what the model knew with how it wrote, so the two failures look alike.

The authors separate the two with languages that are natively written in more than one script, a situation called digraphia. Serbian, for example, uses Latin and Cyrillic. The words, grammar, and meaning are the same in both scripts, so the authors attribute any gap between the two scripts to writing. They study Moroccan Darija, the Moroccan Arabic dialect spoken by about 40 million people and written in both Arabic and Latin script. Customers use Latin script as often as Arabic script, so a business has to answer in both. Darija also has no codified spelling in either script, so "how are you" appears as "kidayr," "ki dayr," or "kidayer."

## Setting and data

Raveesh Mayya (NYU Stern) and Badr-Eddine Lahsini (UM6P Africa Business School) work with 500 customer comments on restaurants, curated by hand from public social media posts. Each comment exists in both scripts with the same words in the same order. Three models at the frontier in December 2025 (GPT-5.2, Claude Opus 4.5, and DeepSeek-V3.2) reply as the restaurant's manager and write directly in the script of the comment (direct generation). A Moroccan postgraduate who is a native Darija speaker codes every reply as acceptable or not under a fixed rubric. A reply is rejected for mixing scripts, not being recognizably Darija, containing ill-formed words, breaking agreement, or leaking prompt text. Unconventional spelling alone never counts against a reply, since Darija has no standard spelling.

## The research questions and how they are answered

The main question Raveesh Mayya and Badr-Eddine Lahsini ask is, how well can an LLM write Darija in each script, and can the gap be closed without retraining the model? Their answer, staged generation, has the model compose the reply in the script it writes best and then transliterate it, that is, rewrite the same words in the letters of the customer's script.

Instructions come first because, for a business using a commercial LLM, the prompt is the main lever. The authors try three strategies, and each one adds to the last. Word examples pair Darija words with their conventional Latin spellings. Letter rules add a complete table mapping Arabic letters to Latin ones. Wrong-word screening checks each reply against a hand-built lexicon of attested wrong forms (6,289 Latin and 827 Arabic) and returns the flagged words to the model in a correction loop of up to ten rounds.

The last step is a crossover field experiment on Prolific. Native Darija speakers judge replies to 16 comments about restaurants and telecommunications providers under four conditions, Arabic or Latin script, each written directly or through staged generation. Every rater sees every condition, and the analysis uses rater and comment fixed effects.

## The staged generation pipeline

Raveesh Mayya and Badr-Eddine Lahsini run staged generation in one call. The model writes the reply in Arabic script and then transliterates its own draft into Latin script. The Latin text goes through the same wrong-word screening, and the correction loop regenerates only the transliteration, so the Arabic draft stays fixed. A loanword override keeps French and English words that Latin-script Darija writes in their source spelling, such as "client," from being transliterated letter by letter.

Staged generation has a built-in check, the reverse control. For Arabic-script comments, the model drafts in Latin script and transliterates into Arabic, with everything else unchanged. If the gain came from splitting the work into steps or from the correction loop, the reverse control should help Arabic-script replies too. If it comes from composing in the stronger script, the reverse control should hurt them.

## What the study finds

Raveesh Mayya and Badr-Eddine Lahsini find that Latin script is the weak side for every model, although Latin is the best-represented script in every frontier model's training data. In Arabic script, 79.8 percent of GPT-5.2's replies are acceptable, 75.2 percent of Claude's, and 12.2 percent of DeepSeek's. In Latin script the figures are 10.2, 11, and 0 percent. Of GPT-5.2's direct Latin-script replies, 83 percent contain Arabic characters and 38 percent switch script inside a single word. In the authors' reading, the model picks the right word and then loses the script partway through it. Latin Darija also costs more tokens, the text pieces a model predicts one at a time, at 2.56 per word against 2.26 in Arabic script. The authors suggest that English and French, which share those Latin pieces, compete for each next token.

Word examples (9.8 percent) and letter rules (10.2 percent) do not improve on GPT-5.2's 10.2 percent baseline, and wrong-word screening reaches 29.4 percent. With the same lexicon and correction loop, staged generation reaches 69 percent. Without the correction loop it reaches 38.4 percent, so drafting in Arabic supplies 28.2 points of the 59-point gain over direct generation and the correction loop 30.6, and neither is enough alone.

The reverse control lowers Arabic-script acceptability from 79.8 to 18.8 percent on GPT-5.2, so the authors conclude that the gain comes from composing in the script the model writes reliably. Token-level confidence, the average probability GPT-5.2 gives each token as it writes, is 66 percent when composing in Latin script, 76 percent in Arabic script, and 87 percent when transliterating its own draft.

On OpenAI's newer GPT-5.5, staged generation raises Latin-script acceptability from 14.6 to 89 percent, within three points of the model's 91.6 percent in Arabic script, and its gain over direct generation widens from 59 to 74 points. The reverse control again lowers Arabic-script acceptability, from 91.6 to 47 percent.

The field experiment, run on GPT-5.5 with 108 Moroccan raters and 1,728 rated responses, reproduces the pattern. Raters accept 15.3 percent of directly generated Latin-script replies and 81.0 percent of staged ones, against 96.8 percent for direct Arabic script. Staged generation raises Latin-script acceptance by 65.4 points, and the reverse control lowers Arabic-script acceptance by 12.4 points, a script-by-method interaction of 78 percentage points (p < 0.001). The interaction holds under alternative clustering, an exact wild cluster bootstrap, logit and ordered-logit models, and a check for learning effects. Script habit, the script a rater uses to write Darija, does not change acceptance and mainly affects how harshly raters judge tone. Every subgroup accepts staged Latin-script replies at 78 to 87 percent.

## What it means

Raveesh Mayya and Badr-Eddine Lahsini read the results as a change of diagnosis. The obstacle in Darija is a script the model writes badly, which they call a smaller and more tractable problem than a language it does not know. Staged generation needs no fine-tuning and runs on a commercial API as is. Leaderboards report one number per language, so a model can rank well in Arabic and still fail in one of its two scripts.

The authors suggest the logic carries to other languages with a stronger script and a reliable rendering step. Replications in Serbian and Punjabi could separate three causes of the Latin-script deficit, namely scarce Latin-script text in training data, interference from French and English, and the lack of a codified spelling.

Two caveats. Staged Latin-script replies are still accepted 15.7 points less often than direct Arabic-script ones, and they read more formal than the Latin-script Darija that native speakers type. And wrong-word screening catches only the wrong words its lexicon lists, so adopters should keep a human path for the replies it misses.

## Where this sits in the broader agenda

The paper belongs to Raveesh Mayya's work on bringing generative AI to speakers of low-resource languages. It connects to his paper with Rohit Aggarwal and Harpreet Singh on spoken-language barriers in AI-assisted programming, which applies to human writers the logic of working in the form one handles best before converting for the reader. Raveesh Mayya and Badr-Eddine Lahsini apply it to the machine writer, which drafts in the script it writes best. The paper grew out of Badr-Eddine Lahsini's Fulbright visit to NYU Stern from UM6P Africa Business School in Morocco. Raveesh Mayya was his host.

**Full citation:** Lahsini, B.-E., and Mayya, R. "Enhancing LLM Performance in Low-Resource Language Settings: Evidence from Moroccan Darija." Working paper, September 2026.
