---
layout: single
permalink: /
author_profile: true
toc: true
toc_label: "Inhalt"
toc_icon: "cog"
title: "Jan Kühnemund"
excerpt: "Site Reliability Engineer (DFS) | DevOps & Network Automation"
header:
  overlay_color: "#333"
  actions:
    - label: "Portfolio ansehen"
      url: "/portfolio/"
    - label: "Lebenslauf (CV)"
      url: "/cv/"
---

**Site Reliability Engineer (DFS) | DevOps & Network Automation**

Spezialisiert auf Reliability Engineering, Automatisierung und komplexe Netzwerkinfrastrukturen. Fokus auf skalierbare Lösungen und effiziente Operations durch Code.

[Portfolio](#projekte){: .btn .btn--primary}
[Lebenslauf](#erfahrung){: .btn .btn--primary}
[Kontakt](#kontakt){: .btn .btn--primary}
[LinkedIn](https://www.linkedin.com/in/jkuehnemund/){: .btn .btn--info}
[GitHub](https://github.com/jahknem){: .btn .btn--info}

## Projekte {#projekte}

{% assign featured_projects = site.projects | where: "lang", "de" | where: "featured", true %}
{% if featured_projects and featured_projects.size > 0 %}

{% for project in featured_projects %}
<article class="archive__item" itemscope itemtype="https://schema.org/CreativeWork">
  <h3 class="archive__item-title" itemprop="headline">
    <a href="{{ project.url | relative_url }}" rel="permalink">{{ project.title }}</a>
  </h3>

  {% if project.role_context %}
  <p class="page__meta">
    <i class="fas fa-briefcase" aria-hidden="true"></i> {{ project.role_context }}
  </p>
  {% endif %}

  {% if project.excerpt %}
  <p class="archive__item-excerpt" itemprop="description">
    {{ project.excerpt | markdownify | strip_html | truncate: 160 }}
  </p>
  {% endif %}
</article>
{% endfor %}

[Alle Projekte ansehen](/portfolio/){: .btn .btn--primary}

{% else %}

{% for project in site.data.projects %}
<div class="feature__item">
  <div class="archive__item-body">
    <h3 class="archive__item-title">{{ project.title }}</h3>
    <p><strong>Rolle:</strong> {{ project.role }} | <strong>Tech Stack:</strong> {{ project.stack }}</p>
    <div class="archive__item-excerpt">
      <p>{{ project.description_de }}</p>
    </div>
  </div>
</div>
{% endfor %}

{% endif %}

## Kompetenzen

* **Reliability:** Kubernetes, Prometheus, Grafana
* **Automation:** Ansible, AWX, Python, CI/CD
* **Network:** Cisco, Nokia, FreeRADIUS, TR-069
* **Virtualization:** Proxmox, Linux

## Erfahrung {#erfahrung}

* **Site Reliability Engineer** @ DFS Deutsche Flugsicherung GmbH  
  *Langen (Hessen) | Dez 2025 – heute*
* **DevOps-/Network Engineer** @ blue networks GmbH & Co. KG  
  *Okt 2021 – Nov 2025*  
  Cluster-Automatisierungslösungen zur Optimierung von Netzwerkkonfigurationsprozessen.
* **Admin & Android Developer Roles** @ RoNikJa GmbH  
  *Jan 2020 – Nov 2021*  
  Interner Server-/Netzwerkbetrieb, Mikrocontroller-Code für ein digitales Mikroskop sowie Android-App-Entwicklung.
* **Praktikum** @ blue networks  
  *Okt 2020 – Mär 2021*  
  Implementierung einer AAA-Lösung mittels FreeRADIUS; Initialisierung einer ACS-Lösung basierend auf CWMP/TR-069.

## Ausbildung

* **M.Sc Informatik** @ TU Darmstadt *(Erwartet Mär 2026)*  
  *Apr 2023 – heute*
* **Auslandssemester** @ ISEP  
  *Jan – Jul 2025*
* **B.Eng Technische Informatik**  
  *Sep 2017 – Sep 2022*

## Zertifizierungen & Sprachen

* **Zertifizierungen:** CCNA (ENSA), CCNA (SRWE), Cambridge English: First (FCE)
* **Sprachen:** Deutsch (Muttersprache), Englisch (Verhandlungssicher), Französisch (Grundkenntnisse)

## Kontakt {#kontakt}

Ich freue mich auf den Austausch.

📧 [jan@kuehnemund.io](mailto:jan@kuehnemund.io)
