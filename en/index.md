---
layout: single
permalink: /en/
author_profile: true
toc: true
toc_label: "Content"
toc_icon: "cog"
title: "Jan Kühnemund"
excerpt: "Site Reliability Engineer (DFS) | DevOps & Network Automation"
header:
  overlay_color: "#333"
  actions:
    - label: "View Portfolio"
      url: "/en/portfolio/"
    - label: "View CV"
      url: "/en/cv/"
---

**Site Reliability Engineer (DFS) | DevOps & Network Automation**

Specializing in Reliability Engineering, Automation, and Networking. Focused on scalable infrastructure and efficient operations.

[Portfolio](#projects){: .btn .btn--primary}
[CV](#experience){: .btn .btn--primary}
[Contact](#contact){: .btn .btn--primary}
[LinkedIn](https://www.linkedin.com/in/jkuehnemund/){: .btn .btn--info}
[GitHub](https://github.com/jahknem){: .btn .btn--info}

## Projects

{% assign featured_projects = site.projects | where: "lang", "en" | where: "featured", true %}
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

[View all projects](/en/portfolio/){: .btn .btn--primary}

{% else %}

{% for project in site.data.projects %}
<div class="feature__item">
  <div class="archive__item-body">
    <h3 class="archive__item-title">{{ project.title }}</h3>
    <p><strong>Role:</strong> {{ project.role }} | <strong>Tech Stack:</strong> {{ project.stack }}</p>
    <div class="archive__item-excerpt">
      <p>{{ project.description_en }}</p>
    </div>
  </div>
</div>
{% endfor %}

{% endif %}

## Skills

* **Reliability:** Kubernetes, Prometheus, Grafana
* **Automation:** Ansible, AWX, Python, CI/CD
* **Network:** Cisco, Nokia, FreeRADIUS, TR-069
* **Virtualization:** Proxmox, Linux

## Experience

* **Site Reliability Engineer** @ DFS Deutsche Flugsicherung GmbH  
  *Langen (Hesse) | Dec 2025 – present*
* **DevOps-/Network Engineer** @ blue networks GmbH & Co. KG  
  *Oct 2021 – Nov 2025*  
  Clustered automation solutions to streamline network configuration processes.
* **Admin & Android Developer Roles** @ RoNikJa GmbH  
  *Jan 2020 – Nov 2021*  
  Internal server/network ops, microcontroller code for a digital microscope, and Android app development.
* **Internship** @ blue networks  
  *Oct 2020 – Mar 2021*  
  AAA solution using FreeRADIUS; started ACS solution based on CWMP/TR-069.

## Education

* **M.Sc Computer Science** @ TU Darmstadt *(Expected Mar 2026)*  
  *Apr 2023 – present*
* **Study Abroad** @ ISEP  
  *Jan – Jul 2025*
* **B.Eng Computer Engineering**  
  *Sep 2017 – Sep 2022*

## Certifications & Languages

* **Certifications:** CCNA (ENSA), CCNA (SRWE), Cambridge English: First (FCE)
* **Languages:** German (Native), English (Professional), French (Elementary)

## Contact {#contact}

I am available for projects. Let's discuss how I can optimize your infrastructure.

📧 [jan@kuehnemund.io](mailto:jan@kuehnemund.io)
