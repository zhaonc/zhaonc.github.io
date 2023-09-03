---
title: "Unable to resolve CNAME domain in Home Assistant"
layout: post
date: '2023-09-02 15:00:00 +0800'
categories: setup
excerpt: CNAME domain resolution issue
---

I have a setup where I run a Home Assistant HAOS as a VM, which queries some sensor data from a self-made API endpoint. The endpoint is hosted on a static LAN-only domain name for ease of access and management.

Recently during a setup refactoring, I changed some of the static DNS entries to CNAME to point to an A record to avoid repetition. Well the rest worked well, Home Assistant started to see failures in scarping the API endpoint:

```text
Platform rest not ready yet: [Errno -2] Name does not resolve; Retrying in background in 30 seconds.
```

After logging onto Home Assistant instance via the [Terminal & SSH add-on](https://github.com/home-assistant/addons/tree/master/ssh):

```text
[core-ssh ~]$ nslookup <CNAME domain>
Server:         127.0.0.11
Address:        127.0.0.11#53

Non-authoritative answer:
<CNAME domain>  canonical name = <A record>
Name:    <A record>
Address: 192.168.1.10

[core-ssh ~]$ curl <CNAME domain>
curl: (6) Could not resolve host: <CNAME domain>
[core-ssh ~]$ ping <CNAME domain>
ping: bad address '<CNAME domain>'
```

After multiple attempts in restarting HAOS VM and the host, and resetting HAOS DNS settings via `ha dns`, I came across [this issue](https://github.com/alpinelinux/docker-alpine/issues/283), which appears to echo what I have seen.

After changing from CNAME to A record, the issue immediately goes away. I'm writing this down hoping to help anyone who is running into the same issue.
