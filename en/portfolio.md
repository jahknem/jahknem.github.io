---
layout: single
title: "Portfolio"
permalink: /en/portfolio/
author_profile: true
---

Here is an overview of my previous projects.

<div class="pillars-grid">
{% assign projects = site.projects | where: "lang", "en" %}
{% for project in projects %}
  <div class="project-card">
    <h3><a href="{{ project.url | relative_url }}">{{ project.title }}</a></h3>
    <div class="project-meta">
      {% if project.role_context %}
        <i class="fas fa-briefcase" aria-hidden="true"></i> {{ project.role_context }}
      {% endif %}
    </div>
    <div class="project-excerpt">
      {{ project.excerpt | markdownify | strip_html | truncate: 160 }}
    </div>
    {% if project.tags %}
    <div class="project-meta" style="margin-top: 1rem;">
       <i class="fas fa-tags" aria-hidden="true"></i> {{ project.tags | join: ', ' }}
    </div>
    {% endif %}
  </div>
{% endfor %}
</div>
