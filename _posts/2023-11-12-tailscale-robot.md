---
title: "Installing Tailscale on a Roborock Vacuum"
date: 2023-11-12T14:27:30+01:00
categories:
  - blog
tags:
  - update
  - tailscale
  - roborock
---


# Installation von Tailscale auf einem Roborock Staubsaugerroboter

## Einleitung

In diesem Blogpost beschreibe ich die Erstellung eines Tailscale Installers für Valetudo Roborock Vacuum Robots. Ursprünglich habe ich den Roborock S50 Staubsauger meiner Schwiegereltern-in-Spe neu eingerichtet. Die Ansaugpumpe war ausgefallen, aber das ist nicht Thema dieses Blogposts. Bei der Reparatur habe ich den Roboter resettet und dabei auch Valetudo, Root und die Sprachausgabe verloren. Nach der Installation von Valetudo wollte ich die deutsche Sprachausgabe wiederherstellen, scheiterte aber an der unvollständigen GUI und dem fehlenden SFTP-Server. Um das später fixen zu könne, installierte ich Tailscale um so aus der Ferne darafu zugreifen zu kpönnen. Die Installation war nicht ganz einfach, da bisherige dokumentierte Versuche entweder fehlerhaft oder unvollständig sind. Daher das Tailscale Installer Skript.

## Schritte der Installation

1. **Erkennung der CPU-Architektur:** Zuerst identifizierte ich die CPU-Architektur des Staubsaugers mit `uname -m`, um den passenden Tailscale-Downloadlink zu ermitteln.

2. **Download und Installation:** Das Tailscale-Paket wurde in die `/mnt/data`-Partition heruntergeladen und entpackt. Anschließend wurden die Tailscale-Executables (`tailscale` und `tailscaled`) in `/usr/local/bin` kopiert.

3. **Daemon-Problematik:** Aufgrund des Fehlens von systemd oder init.d auf dem Roborock nutzte ich start-stop-daemon, um Tailscaled  lassen.

4. **Automatischer Start beim Booten:** Durch Hinzufügen des Startbefehls in die `rc.local`-Datei startete Tailscale automatisch beim Booten des Systems. Dem Befehl wird noch "--state=/mnt/data/tailscale/tailscaled.state" angehängt, um den Speicherort des Tailscale-Status zu definieren. Da Roborock alle Partitionen außer der `/mnt/data`-Partition beim Booten zurücksetzt, würde der Status verloren gehen, wenn er nicht in der `/mnt/data`-Partition gespeichert würde.

5. **Anpassung des Hostnamens:** Um den Staubsaugerroboter unter dem korrekten Namen in der Tailscale-App anzeigen zu lassen, passte ich den Hostnamen in den Dateien `/etc/hostname` und `/etc/hosts` an.

## Fazit

Das gesamte Verfahren habe ich in einem Skript zusammengefasst, das in meinem GitHub-Repository [Robrorock-Tailscale-Installer](https://github.com/jahknem/Roborock-Tailscale-Installer) zu finden ist. Im Prinzip ist das Skript ziemlich einfach, aber es spart einige Schritte.

## Quellen

- [Gist](https://gist.github.com/johnDorian/4c530adfd08d70108c08e8bbc6368091) by [johnDorian](https://gist.github.com/johnDorian)
- [Tailscale Sucks](https://tailscale.dev/blog/tailscale-sucks) by [Tailscale](https://tailscale.com/)
---