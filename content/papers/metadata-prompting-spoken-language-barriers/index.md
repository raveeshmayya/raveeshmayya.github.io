---
title: "Mitigating Spoken Language Barriers in AI-Assisted Programming: Evidence from a Field Experiment"
url: /papers/metadata-prompting-spoken-language-barriers/
date: 2026-10-24T00:39:01-04:00
paper:
  authors:
    - name: "Rohit Aggarwal"
      affiliation: "UC Riverside"
    - name: "Raveesh Mayya"
      self: true
      affiliation: "New York University, Stern School of Business"
    - name: "Harpreet Singh"
      affiliation: "University of Texas at Dallas, Naveen Jindal School of Management"
  year: 2026
  status: "Working paper"
summary: "Extended narrative summary of the working paper by Rohit Aggarwal, Raveesh Mayya, and Harpreet Singh: in a field experiment inside a real hiring process in India, developers with weaker English abandoned more, worked slower, and scored lower when prompting an LLM in English prose, and a JSON-based format called Metadata Prompting closed those gaps."
description: "Extended summary of the working paper on Metadata Prompting and spoken-language barriers in AI-assisted programming, by Raveesh Mayya (NYU Stern), Rohit Aggarwal (UC Riverside), and Harpreet Singh (UT Dallas Jindal)."
searchHidden: true
ShowBreadCrumbs: false
---

**Paper:** Mitigating Spoken Language Barriers in AI-Assisted Programming: Evidence from a Field Experiment

**Authors:** Rohit Aggarwal (UC Riverside), Raveesh Mayya (New York University, Stern School of Business), and Harpreet Singh (University of Texas at Dallas, Naveen Jindal School of Management), listed alphabetically in the paper

**Status:** Working paper (R&R), draft dated May 5, 2026

**Findings in three sentences:** In AI-assisted programming, where developers describe what they want to an LLM in English prose, Raveesh Mayya, Rohit Aggarwal, and Harpreet Singh first document a spoken-language barrier inside a real hiring process in India, with developers of low English proficiency, compared with those of high proficiency, about 80 percent more likely to abandon a task, about 22 percent slower to finish, and about 14 percent lower on accuracy. Their fix, Metadata Prompting, replaces prose with a JSON-based intermediate representation that separates what the program should do from how to say it in English, which improves performance at every proficiency level and makes the proficiency gaps statistically insignificant on all three outcomes. Using a format conversion analysis, in which GPT-4o rewrites every prompt into other common formats (including XML), the authors attribute about 87 percent of the accuracy advantage to developers writing fuller specifications and only about 13 percent to the model parsing structured input more easily.

**Method contribution:** A JSON-based intermediate representation for writing software requirements, developed in the design science tradition from three design principles (separation of concerns, symbolic externalization, and deferred definition) drawn from compiler design, cognitive load theory, and speech production research. It is tested in a 2×2 crossover field experiment with 965 job candidates, each of whom is given two coding tasks, one under each prompting format, with the order of formats and tasks randomly assigned. A developer who completes both tasks serves as their own control, so stable traits such as ability and motivation drop out of the comparison. Because the tasks counted toward hiring, candidates had real stakes. A format conversion analysis then separates what the human writes better from what the model reads better.

*This is an extended narrative summary written for readers who want more detail than an abstract offers without reading the full paper.*

## Why this question matters

AI coding assistants work by letting a developer describe in words what the code should do. Older programming tools mostly took structured input, such as menu choices and command-line flags, and seldom required fluent English, whereas a chat assistant makes the developer write the request in sentences. Millions of developers write English as a second language. For them, the newer and more capable tool can be the harder one to use.

Writing the prompt in a native language that is low-resource, such as Hindi, Swahili, or Yoruba, has costs of its own. Models have little digital text to learn from. They also split words in these languages into more tokens, the small pieces of text a model processes, which raises cost and lowers quality.

LLMs read structured formats such as JSON about as well as they read prose. A request to a model can therefore be written in whatever form is easiest for the person writing it. A research team comprising Raveesh Mayya (NYU Stern), Rohit Aggarwal (UC Riverside), and Harpreet Singh (UT Dallas Jindal) asks whether English proficiency affects how well developers use AI to program, whether a structured intermediate representation can shrink the gap, and how proficiency shapes which style of prompting developers prefer.

## Setting and data

Raveesh Mayya, Rohit Aggarwal, and Harpreet Singh partnered with a medium-sized technology firm in India that builds custom full-stack software for clients in several industries. In the last quarter of 2023 the firm was hiring full-stack engineers who work with the MERN stack (MongoDB, Express, React, and Node.js), and the study ran inside that hiring process. Task performance fed into hiring decisions, so candidates had a real reason to try.

The sample is 965 candidates, all native Hindi speakers, with under a year of programming experience on average. Each passed through three stages. A 90-minute test of building a MERN application without AI measured baseline coding skill. A 60-minute GRE-style test measured English proficiency, scaled from 0 to 1. In the third stage, each candidate was given two 85-minute coding tasks to do with an AI assistant, one with prose prompts and one with Metadata Prompting. Task requirements came as videos in Hindi, so a candidate's English did not limit how well they understood the task.

The outcomes are whether a candidate abandoned the task, total time (in minutes) a task took, and accuracy, the share of unit tests passed by code that the LLM generated from the candidate's prompt, averaged over two runs.

## Metadata Prompting and why it should work

The authors start from what they call the articulation burden, the mental cost of turning a technical idea into English prose. They divide it into composing grammatical sentences that carry the task logic, holding requirements and half-finished clauses in working memory, and deciding what to say while also deciding how to say it. Each part weighs most on someone writing in a second language.

Each part maps to a design principle and a prediction. Separation of concerns, from compiler design, keeps what to convey apart from how to express it, which should cut abandonment, the most extreme response to overload. Symbolic externalization, from cognitive load theory, moves definitions into named fields the developer can look at, which should mainly shorten completion time. Deferred definition, from Levelt's model of speech production, lets a developer name an entity first and define it later, which should produce fuller specifications and more accurate code. Each principle should help developers with low proficiency most.

Metadata Prompting builds all three into JSON, a common format of named fields and values. In the paper's worked example, a request for a Node.js function that sends inventory alerts becomes a task, a reason, the inputs, and a list of rules. Earlier structured methods, such as formal specification languages, were built so that an engineer or a compiler could read requirements precisely. Metadata Prompting is built to make requirements easier to write. The authors expect it to work where domain expertise exists apart from English, the format is already familiar, and the output is code read by a model that handles structured input as well as prose, which describes MERN developers working in JSON.

## The research questions and how they are answered

The main question Raveesh Mayya, Rohit Aggarwal, and Harpreet Singh ask is, do developers with weaker English get less out of an AI coding assistant, and can a different way of writing the request remove the gap? The experiment is a 2×2 crossover. Each candidate does one task with prose prompting and the other with Metadata Prompting, and candidates are randomly assigned to four groups of about 241 that differ in which format and which task come first.

Comparing each candidate with themselves removes stable traits, such as ability and motivation, that might be correlated with English proficiency. Because everyone uses both formats, the authors also test whether the benefit of Metadata Prompting depends on proficiency. The four groups are balanced. They do not differ significantly on seven candidate traits, such as English proficiency and coding ability (p-values from 0.24 to 1.00).

Of the 965 candidates, 691 completed the first task and 656 of those also completed the second. Randomization is fully intact only for the first task, so the abandonment analysis uses whether each of the 965 candidates abandoned it, while completion time and accuracy pool both tasks (1,347 observations).

## What the study finds

Raveesh Mayya, Rohit Aggarwal, and Harpreet Singh first establish the barrier. Under prose prompting, the authors estimate that developers with low English proficiency, compared with those with high proficiency, are about 80 percent more likely to abandon a task, take about 22 percent longer, and score about 14 percent lower on accuracy. In the raw data under prose prompting, the bottom tercile (the third of candidates with the lowest English scores) takes about 10 more minutes than the top tercile and scores under 60 percent on accuracy against close to 70 percent.

Metadata Prompting closes these gaps. Holding proficiency constant, it cuts completion time by about 20 minutes, raises accuracy by about 19 percentage points, and lowers the odds of abandoning a task. Under Metadata Prompting every tercile finishes in roughly 35 minutes and scores above 80 percent on accuracy, and the proficiency gap is no longer statistically significant on any outcome (p = 0.31 for abandonment, 0.49 for completion time, and 0.14 for accuracy). Developers at every proficiency level gain, and the gains are largest for those with the lowest proficiency.

One alternative reading is that English proficiency stands in for general ability. If it did, the gaps would persist under any format, and they do not. In models of completion time and accuracy with participant fixed effects, which compare each candidate only with themselves and so absorb every stable trait, the narrowing of the proficiency gap under Metadata Prompting remains significant at the 1 percent level. The results also hold with other accuracy measures, other statistical models, and a test for learning across rounds.

## Why Metadata Prompting works

Part of the accuracy gain could come from the model, if LLMs simply parse JSON more easily. The authors' account puts it on the human side, where the structure helps developers write more complete requirements. To tell the two apart, they run a format conversion analysis, in which GPT-4o rewrites all 1,347 prompts into other formats with the content held fixed (including XML, which neither group used) and the same LLM generates code that is scored against the original unit tests. If format drove the advantage, equalizing it would close the 18.4-point accuracy gap between English-written and JSON-written prompts. Conversion closes only 11.4 to 14.1 percent of it, about 13 percent on average, and when both groups' prompts are converted to XML, 15.8 points remain. The authors attribute the remaining 87 percent or so to the gains coming from developers writing better.

The authors also surveyed 656 participants after the tasks. On three five-point items (future use, confidence, and expected effectiveness), where 5 strongly favors Metadata Prompting, every tercile favors it, with average scores of 4.26 to 4.32 in the bottom tercile and 3.58 to 3.67 in the top, a statistically significant difference.

## What it means

Raveesh Mayya, Rohit Aggarwal, and Harpreet Singh place the result within research on the "AI divide," the uneven spread of AI's benefits, and argue that interface design can narrow it. In their reading, a firm can get the gains without English training for its developers and without a model built for their language. Accepting structured prompts requires no fine-tuning. The authors suggest that AI platforms accept structured prompts alongside ordinary chat and offer templates and validators that help users build them.

The authors expect the design principles to carry to other tasks whose output is code or another formal language, and they suggest tests in Stata or R programming and database queries, with XML or YAML in place of JSON.

Two caveats. The evidence comes from one firm's hiring process, Hindi-speaking candidates, and MERN-stack tasks where JSON is already familiar, a setting that meets all three of the authors' conditions. And the setting does not record why candidates abandoned a task or how hard they found prompt writing, and English proficiency comes from a general GRE-style test. The role of articulation difficulty is therefore the authors' inference.

## Where this sits in the broader agenda

This paper by Raveesh Mayya, Rohit Aggarwal, and Harpreet Singh belongs to Raveesh Mayya's work on bringing the benefits of generative AI to speakers of low-resource languages. A companion study with Badr-Eddine Lahsini (UM6P Africa Business School) on [Moroccan Darija](/papers/llms-low-resource-languages-moroccan-darija/) applies the same logic of working in the form one handles best before converting for the reader, with the model as the writer, drafting in the script it writes best. The paper also connects to his work with Doron Yeverechyahu and Gal Oestreicher-Singer on [GitHub Copilot and open-source innovation](/papers/llms-open-source-innovation-github-copilot/), which asks what happens when programmers get AI assistance. This paper asks who can use it well.

**Full citation:** Aggarwal, R., Mayya, R., and Singh, H. "Mitigating Spoken Language Barriers in AI-Assisted Programming: Evidence from a Field Experiment." Working paper (R&R), May 2026.
