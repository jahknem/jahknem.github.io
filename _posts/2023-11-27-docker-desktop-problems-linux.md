---
title: "Docker Desktop Issues"
date: 2023-11-27T23:57:30+01:00
categories:
  - blog
tags:
  - docker
  - desktop
---

# Docker Desktop creates and switches the Docker Context but does not switch back when uninstalling

TL;DR: The Headline. Just use "docker context set default" to fix it.

Hey y'all! Today I tried running willow-interference-server (Great project btw, check it out under: ) on my desktop. I had Docker Desktop installed, which led to some problems with docker and nvidia... I don't have the logs anymore, otherwiese that would probably be worth a blogpost on its own.
Anyways. After uninstalling docker desktop and instead installing docker-ce, I got this:

jan@desktop1:~/Projects/willow-inference-server$ ./utils.sh install
Using configuration overrides from .env file
ERROR: Cannot connect to the Docker daemon at unix:///home/jan/.docker/desktop/docker.sock. Is the docker daemon running?

So obviously it is trying to use the wrong path. But hellow world runs without a hitch, so what gives?

jan@desktop1:~$ sudo docker run hello-world

Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
    (amd64)
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.

To try something more ambitious, you can run an Ubuntu container with:
 $ docker run -it ubuntu bash

Share images, automate workflows, and more with a free Docker ID:
 https://hub.docker.com/

For more examples and ideas, visit:
 https://docs.docker.com/get-started/


This led to me searchimg through all my .profile, .bashrc and docker config files.. not finding anything at all. It seemed weird, but as I'm not a Docker Guru I started grepping my complete home directory.

find /home/jan/ -type f -size -10M -exec grep -H "docker/desktop/docker.sock" {} +

And after crwaling through the cache of firefox, which contained an intense discussion between me and chatgpt about just this topic, I found this entry:

/home/jan/.docker/contexts/meta/fe9c6bd7a66301f49ca9b6a70b217107cd1284598bfc254700c989b916da791e/meta.json:{"Name":"desktop-linux","Metadata":{"Description":"Docker Desktop"},"Endpoints":{"docker":{"Host":"unix:///home/jan/.docker/desktop/docker.sock","SkipTLSVerify":false}}}

So.. Docker Desktops switches the context silently and does not remove that context when getting uninstalled. Annoying. I'm sure its somewhere in the Docs, but I have not found it yet.

Thats all, see ya!
