---
layout: splash
permalink: /
author_profile: false
title: "Jan Kühnemund - SRE & DevOps"
header:
  overlay_color: "#333"
---

<div class="hero">
  <div class="hero__content">
    <h1>Jan Kühnemund</h1>
    <p class="lead">Site Reliability Engineer @ DFS | DevOps & Network Automation</p>
    <p>Spezialisiert auf Reliability Engineering, Automatisierung und komplexe Netzwerkinfrastrukturen. Fokus auf skalierbare Lösungen und effiziente Operations durch Code.</p>
    <p>
      <a href="/portfolio/" class="btn btn--primary">Portfolio ansehen</a>
      <a href="/cv/" class="btn btn--primary">Lebenslauf (CV)</a>
      <a href="/contact/" class="btn btn--info">Kontakt</a>
    </p>
  </div>
  <div class="hero__image">
    <img src="/assets/images/jan-kuehnemund.jpg" alt="Jan Kühnemund Portrait">
  </div>
</div>

<div class="pillars-grid">
  <div class="pillar-card">
    <h3>Reliability / SRE</h3>
    <p>Kubernetes, Prometheus, Grafana. Sicherstellung von Stabilität und Observability in komplexen Systemen.</p>
  </div>
  <div class="pillar-card">
    <h3>Automation / IaC</h3>
    <p>Ansible, AWX, Python. Automatisierung von Konfigurationen und Prozessen zur Fehlerreduktion.</p>
  </div>
  <div class="pillar-card">
    <h3>Networking</h3>
    <p>Cisco, Nokia, FreeRADIUS. Fundiertes Wissen in Netzwerkprotokollen und -infrastruktur.</p>
  </div>
  <div class="pillar-card">
    <h3>Virtualization</h3>
    <p>Proxmox, Linux, Containerisierung. Effiziente Ressourcennutzung und flexible Umgebungen.</p>
  </div>
</div>

<h2>Ausgewählte Erfahrung</h2>

<div class="experience-timeline">
  <div class="experience-item">
    <h3>Site Reliability Engineer</h3>
    <div class="role-meta">DFS Deutsche Flugsicherung GmbH | Dez 2025 – heute</div>
    <p>Fokus auf Reliability und Systemstabilität im kritischen Umfeld der Flugsicherung.</p>
  </div>
  <div class="experience-item">
    <h3>DevOps-/Network Engineer</h3>
    <div class="role-meta">blue networks GmbH & Co. KG | Okt 2021 – Nov 2025</div>
    <p>Entwicklung von Cluster-Automatisierungslösungen und Optimierung von Netzwerkkonfigurationsprozessen.</p>
  </div>
</div>

<h2>Ausgewählte Projekte</h2>

<div class="pillars-grid">
{% assign featured_projects = site.projects | where: "lang", "de" | where: "featured", true %}
{% for project in featured_projects %}
  <div class="project-card">
    <h3><a href="{{ project.url | relative_url }}">{{ project.title }}</a></h3>
    <div class="project-meta">{{ project.role_context }}</div>
    <div class="project-excerpt">
      {{ project.excerpt | markdownify | strip_html | truncate: 120 }}
    </div>
  </div>
{% endfor %}
</div>

<p style="text-align: center;">
  <a href="/portfolio/" class="btn btn--outline-primary">Alle Projekte ansehen</a>
</p>
