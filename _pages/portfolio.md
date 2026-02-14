---
layout: single
title: "Portfolio"
permalink: /portfolio/
author_profile: true
---

Hier finden Sie eine Übersicht meiner bisherigen Projekte.

{% assign projects = site.projects | where: "lang", "de" %}
{% for project in projects %}
  <article class="archive__item" itemscope itemtype="https://schema.org/CreativeWork">
    <h2 class="archive__item-title" itemprop="headline">
      <a href="{{ project.url | relative_url }}" rel="permalink">{{ project.title }}</a>
    </h2>
    <p class="page__meta">
      {% if project.role_context %}
        <i class="fas fa-briefcase" aria-hidden="true"></i> {{ project.role_context }} &nbsp;
      {% endif %}
      {% if project.tags %}
        <i class="fas fa-tags" aria-hidden="true"></i> {{ project.tags | join: ', ' }}
      {% endif %}
    </p>
    {% if project.excerpt %}<p class="archive__item-excerpt" itemprop="description">{{ project.excerpt | markdownify | strip_html | truncate: 160 }}</p>{% endif %}
  </article>
{% endfor %}
