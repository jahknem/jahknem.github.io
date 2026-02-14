---
layout: splash
permalink: /en/
author_profile: false
title: "Jan Kühnemund - SRE & DevOps"
header:
  overlay_color: "#333"
---

<div class="hero">
  <div class="hero__content">
    <h1>Jan Kühnemund</h1>
    <p class="lead">Site Reliability Engineer @ DFS | DevOps & Network Automation</p>
    <p>Specializing in Reliability Engineering, Automation, and complex Network Infrastructures. Focused on scalable solutions and efficient operations through code.</p>
    <p>
      <a href="/en/portfolio/" class="btn btn--primary">View Portfolio</a>
      <a href="/en/cv/" class="btn btn--primary">View CV</a>
      <a href="/en/contact/" class="btn btn--info">Contact</a>
    </p>
  </div>
  <div class="hero__image">
    <img src="/assets/images/jan-kuehnemund.jpg" alt="Jan Kühnemund Portrait">
  </div>
</div>

<div class="pillars-grid">
  <div class="pillar-card">
    <h3>Reliability / SRE</h3>
    <p>Kubernetes, Prometheus, Grafana. Ensuring stability and observability in complex systems.</p>
  </div>
  <div class="pillar-card">
    <h3>Automation / IaC</h3>
    <p>Ansible, AWX, Python. Automating configurations and processes to reduce errors.</p>
  </div>
  <div class="pillar-card">
    <h3>Networking</h3>
    <p>Cisco, Nokia, FreeRADIUS. Deep knowledge in network protocols and infrastructure.</p>
  </div>
  <div class="pillar-card">
    <h3>Virtualization</h3>
    <p>Proxmox, Linux, Containerization. Efficient resource usage and flexible environments.</p>
  </div>
</div>

<h2>Selected Experience</h2>

<div class="experience-timeline">
  <div class="experience-item">
    <h3>Site Reliability Engineer</h3>
    <div class="role-meta">DFS Deutsche Flugsicherung GmbH | Dec 2025 – present</div>
    <p>Focusing on reliability and system stability in critical air traffic control environments.</p>
  </div>
  <div class="experience-item">
    <h3>DevOps-/Network Engineer</h3>
    <div class="role-meta">blue networks GmbH & Co. KG | Oct 2021 – Nov 2025</div>
    <p>Development of clustered automation solutions and optimization of network configuration processes.</p>
  </div>
</div>

<h2>Selected Projects</h2>

<div class="pillars-grid">
{% assign featured_projects = site.projects | where: "lang", "en" | where: "featured", true %}
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
  <a href="/en/portfolio/" class="btn btn--outline-primary">View all projects</a>
</p>
