---
layout: single
permalink: /
author_profile: true
toc: true
toc_label: "Inhalt"
toc_icon: "cog"
title: "Jan Kühnemund - SRE & Cloud Consultant"
excerpt: "Freiberuflicher Consultant für Kubernetes, Virtualisierung und Cloud-Infrastruktur."
header:
  overlay_color: "#333"
---

Ich bin **Jan Kühnemund**, spezialisiert auf **Site Reliability Engineering (SRE)**, **Kubernetes** und **Virtualisierung**. Mit fundiertem Hintergrund in Computer Engineering und jahrelanger praktischer Erfahrung unterstütze ich Projekte bei der Skalierung und Automatisierung ihrer Infrastruktur.

## Über mich

Geboren 1995, verbinde ich akademisches Wissen mit handfester technischer Expertise. Mein Weg führte über eine Ausbildung zum **IT-Systemelektroniker** zum Studium des **Computer Engineering** (Bachelor of Engineering). Diese Kombination ermöglicht mir ein tiefes Verständnis von Hardware bis zur High-Level-Softwarearchitektur.

## Leistungen

Mein Fokus liegt auf robusten, skalierbaren Lösungen:

*   **Kubernetes & Container**: Konzeption und Betrieb von Hochverfügbarkeits-Clustern (z.B. k3s).
*   **Virtualisierung**: Expertenwissen in Proxmox VE (10+ Jahre Erfahrung) und Virtualisierungstechnologien.
*   **Infrastructure as Code (IaC)**: Automatisierung mit Ansible und AWX.
*   **SRE & Entwicklung**: Entwicklung von Python-Anwendungen für den Produktionsbetrieb und Aufbau von Automatisierungspipelines.

## Projekterfahrung

{% assign featured_projects = site.projects | where: "lang", "de" | where: "featured", true %}
{% for project in featured_projects %}
  <article class="archive__item" itemscope itemtype="https://schema.org/CreativeWork">
    <h3 class="archive__item-title" itemprop="headline">
      <a href="{{ project.url | relative_url }}" rel="permalink">{{ project.title }}</a>
    </h3>
    <p class="page__meta">
      {% if project.role_context %}
        <i class="fas fa-briefcase" aria-hidden="true"></i> {{ project.role_context }} &nbsp;
      {% endif %}
    </p>
    {% if project.excerpt %}<p class="archive__item-excerpt" itemprop="description">{{ project.excerpt | markdownify | strip_html | truncate: 160 }}</p>{% endif %}
  </article>
{% endfor %}

[Alle Projekte ansehen](/portfolio/){: .btn .btn--primary}

## Kontakt

Ich stehe für Projekte zur Verfügung. Lassen Sie uns darüber sprechen, wie ich Ihre Infrastruktur optimieren kann.

📧 [jan@kuehnemund.io](mailto:jan@kuehnemund.io)
