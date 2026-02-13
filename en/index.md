---
layout: single
permalink: /en/
author_profile: true
toc: true
toc_label: "Content"
toc_icon: "cog"
title: "Jan Kühnemund - SRE & Cloud Consultant"
excerpt: "Freelance Consultant for Kubernetes, Virtualization, and Cloud Infrastructure."
header:
  overlay_color: "#333"
---

I am **Jan Kühnemund**, a freelance consultant specializing in **Site Reliability Engineering (SRE)**, **Kubernetes**, and **Virtualization**. With a strong background in Computer Engineering and years of hands-on experience, I help businesses scale and automate their infrastructure.

## About Me

Born in 1995, I combine academic knowledge with practical technical expertise. My journey started with an apprenticeship as an **IT Systems Electronics Technician** and led to a **Bachelor of Engineering in Computer Engineering**. This combination gives me a deep understanding from hardware to high-level software architecture.

## Services

My focus is on robust, scalable solutions:

*   **Kubernetes & Containers**: Concept and operation of High Availability Clusters (e.g., k3s).
*   **Virtualization**: Expert knowledge in Proxmox VE (10+ years experience) and virtualization technologies.
*   **Infrastructure as Code (IaC)**: Automation with Ansible and AWX.
*   **SRE & Development**: Development of production-ready Python applications and automation pipelines.

## Featured Projects

{% assign featured_projects = site.projects | where: "lang", "en" | where: "featured", true %}
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

[View all projects](/en/portfolio/){: .btn .btn--primary}

## Contact

I am available for freelance projects. Let's discuss how I can optimize your infrastructure.

📧 [jan@kuehnemund.io](mailto:jan@kuehnemund.io)
