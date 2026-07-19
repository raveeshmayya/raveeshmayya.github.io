---
title: "Teaching"
url: /teaching/
summary: "Teaching by Raveesh Mayya"
---

## NYU Stern School of Business

<ul class="paper-list course-list">
<li><details open>
<summary><strong>Foundations of AI Agents (OPMG-GB 3110)</strong><br>
MBA elective · <a href="https://aiagents.stern.nyu.edu" target="_blank" rel="noopener">Course website</a></summary>
<p class="paper-abstract">I co-developed this graduate elective for MBA students. Over six three-hour sessions, students move from the fundamentals of agentic systems (tool calling, system prompts, model trade-offs, managing stochasticity) to multi-agent orchestration, retrieval-augmented enterprise agents, and rigorous evaluation. Agents are best learned by building them: every session pairs concept with lab, culminating in Demo Day, where teams present agents built for real business problems.</p>
</details></li>

<li><details>
<summary><strong>IT in Business and Society (TECH-UB 1)</strong><br>
Undergraduate core</summary>
<p class="paper-abstract">The discussion revolves around how digital technologies are fundamentally different from all other technologies due to three aspects: digital representation, computational power, and modular programmability. Using these three lenses, students examine how digital technologies reshape firms, markets, and society. Students also learn SQL hands-on using SQL Server, querying real datasets to ground the concepts in practice.</p>
</details></li>
</ul>

## UMD Smith School of Business

<ul class="paper-list course-list">
<li><details>
<summary><strong>Database Systems (BMGT 402)</strong><br>
Undergraduate · <strong>Distinguished Teaching Award</strong>, AY 2017-18 (top 10% of all instructors)</summary>
<p class="paper-abstract">A hands-on introduction to designing and querying relational databases. Students learn both DDL and DML sides of SQL, conceptual design with Entity Relationship Diagrams, and normalization for translating business requirements into well-structured schemas. The course emphasizes moving from a messy real-world problem to a clean, queryable database design.</p>
</details></li>
</ul>

<script>
document.addEventListener('DOMContentLoaded', function () {
  var courses = document.querySelectorAll('.course-list details');
  courses.forEach(function (d) {
    d.addEventListener('toggle', function () {
      if (d.open) {
        courses.forEach(function (o) { if (o !== d) o.open = false; });
      }
    });
  });
});
</script>
