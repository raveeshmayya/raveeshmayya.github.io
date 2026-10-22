---
title: "Research"
url: /research/
summary: "Research by Raveesh Mayya"
---

## Recent Research Award Nominations/Wins

- **[The 2026 Platform Leaders Academic Prize](https://platformleaders.com/insights/the-2026-platform-leaders-academic-prize-meet-the-three-finalists/)** (London) — Finalist (Top 3)
- **AI in Management (AIM) 2026** (Los Angeles) — Best Paper Finalist
- **AI in Management (AIM) 2025** (Los Angeles) — Best Paper Finalist
- **Int. Conf. of Smart Finance 2025** (Shanghai) — Best Track Paper Award
- **CIST 2024** (Seattle) — Best Student Paper Runner Up
- **ICIS 2023** (Hyderabad) — Best Paper Nominee
- **WHICEB 2023** (Wuhan) — Best Paper Runner Up
- **WISE 2022** (Copenhagen) — Best Student Paper Nominee

## Research Agenda

My Ph.D. training at UMD Smith exposed me to a variety of exciting research streams, including the Business Value of IT, where I contributed to a couple of publications through my research assistantship (listed on my <a href="https://raveeshmayya.github.io/longcv/" target="_blank" rel="noopener">CV</a>). Over the years, I've realized that my deep interests lie in two streams, which I am actively building: (a) how digital platforms enhance the choice and control that consumers have in two-sided markets, how suppliers respond to such policies, and how that reshapes marketplace outcomes for those suppliers, and (b) how generative AI transforms knowledge work, with a focus on the supply side of the knowledge economy (programmers, researchers), including how to make its benefits accessible to speakers of low-resource languages.

## Digital Platform Policy and Unintended Consequences

<div class="tag-filter">
  <span class="tag-chip active" data-tag="all">All</span>
  <span class="tag-chip" data-tag="Platform Policy">Platform Policy</span>
  <span class="tag-chip" data-tag="Privacy">Privacy</span>
  <span class="tag-chip" data-tag="Token Policy">Token Policy</span>
  <span class="tag-chip" data-tag="Information Asymmetry">Information Asymmetry</span>
</div>

{{< papers section="platform" >}}

## Generative AI, Knowledge Work, and Collaborative Innovation

This is an emerging research agenda for me, with multiple working papers in progress. Four are below.

<div class="video-grid">
<figure class="talk-video">
<div class="video-frame"><iframe src="https://www.youtube-nocookie.com/embed/PHhXhrF1Kks" title="Talk: Spoken-language barriers in GenAI-assisted software development" loading="lazy" allowfullscreen></iframe></div>
<figcaption>Talk on mitigating spoken language barriers (Wharton GenAI Conference)</figcaption>
</figure>
<figure class="talk-video">
<div class="video-frame"><iframe src="https://www.youtube-nocookie.com/embed/bOgYmunWCtQ?start=1081" title="Talk: The impact of LLMs on open-source innovation (GitHub Copilot)" loading="lazy" allowfullscreen></iframe></div>
<figcaption>Talk on LLMs and open-source innovation (World Bank Conference)</figcaption>
</figure>
</div>

{{< papers section="genai" >}}

<script>
document.addEventListener('DOMContentLoaded', function () {
  var chips = document.querySelectorAll('.tag-chip');
  function applyFilter(tag) {
    chips.forEach(function (c) {
      c.classList.toggle('active', c.dataset.tag === tag);
    });
    document.querySelectorAll('.papers-platform > li').forEach(function (li) {
      var tags = Array.from(li.querySelectorAll('.paper-tag')).map(function (t) { return t.textContent.trim(); });
      li.style.display = (tag === 'all' || tags.indexOf(tag) !== -1) ? '' : 'none';
    });
  }
  chips.forEach(function (c) {
    c.addEventListener('click', function (e) { e.preventDefault(); applyFilter(c.dataset.tag); });
  });
  document.querySelectorAll('.paper-tag').forEach(function (t) {
    t.style.cursor = 'pointer';
    t.addEventListener('click', function () { applyFilter(t.textContent.trim()); });
  });
  var papers = document.querySelectorAll('.paper-list details');
  papers.forEach(function (d) {
    d.addEventListener('toggle', function () {
      if (d.open) {
        papers.forEach(function (o) { if (o !== d) o.open = false; });
      }
    });
  });
});
</script>
