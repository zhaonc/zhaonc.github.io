---
title: "Potential memory leak of Container Manager on Synology NAS"
layout: post
date: '2023-09-02 22:30:00 +0800'
categories: setup
excerpt: Potential memory leak since 20.10.23-1413 and workaround
---

After upgrading to 20.10.23-1413 (DSM 7.2-64570 Update 3), I started observing a memory leak from Container Manager/ Docker. It seems to keep on launching new processes "docker system dial-stdio" slowly, which gradually takes up all the memory.

Having tried uninstalling and reinstalling Container Manager, and restarting multiple times, the issue persisted. After starting Container Manager, the issue starts to appear after a few minutes.

```text
zhaonc@zhaonc-nas:~$ ps -ef | grep "docker system dial-stdio" | grep -v grep
zhaonc 3104 3103 0 22:17 ? 00:00:00 docker system dial-stdio
zhaonc 3160 3159 0 22:17 ? 00:00:00 docker system dial-stdio
zhaonc 3179 3177 0 22:17 ? 00:00:00 docker system dial-stdio

zhaonc@zhaonc-nas:~$ lsof -p 3104
3104 /volume2/@appstore/ContainerManager/usr/bin/docker 0 pipe:[14184724]
3104 /volume2/@appstore/ContainerManager/usr/bin/docker 1 pipe:[14184725]
3104 /volume2/@appstore/ContainerManager/usr/bin/docker 2 pipe:[14184726]
3104 /volume2/@appstore/ContainerManager/usr/bin/docker 3 anon_inode:[eventpoll]
3104 /volume2/@appstore/ContainerManager/usr/bin/docker 4 pipe:[14184731]
3104 /volume2/@appstore/ContainerManager/usr/bin/docker 5 pipe:[14184731]
3104 /volume2/@appstore/ContainerManager/usr/bin/docker 6 socket:[14183725]
3104 /volume2/@appstore/ContainerManager/usr/bin/docker 7 socket:[14183728]
3160 /volume2/@appstore/ContainerManager/usr/bin/docker 0 pipe:[14185098]
3160 /volume2/@appstore/ContainerManager/usr/bin/docker 1 pipe:[14185099]
3160 /volume2/@appstore/ContainerManager/usr/bin/docker 2 pipe:[14185100]
3160 /volume2/@appstore/ContainerManager/usr/bin/docker 3 anon_inode:[eventpoll]
3160 /volume2/@appstore/ContainerManager/usr/bin/docker 4 pipe:[14185117]
3160 /volume2/@appstore/ContainerManager/usr/bin/docker 5 pipe:[14185117]
3160 /volume2/@appstore/ContainerManager/usr/bin/docker 6 socket:[14185120]
3160 /volume2/@appstore/ContainerManager/usr/bin/docker 7 socket:[14185123]
3179 /volume2/@appstore/ContainerManager/usr/bin/docker 0 pipe:[14184175]
3179 /volume2/@appstore/ContainerManager/usr/bin/docker 1 pipe:[14184176]
3179 /volume2/@appstore/ContainerManager/usr/bin/docker 2 pipe:[14184177]
3179 /volume2/@appstore/ContainerManager/usr/bin/docker 3 anon_inode:[eventpoll]
3179 /volume2/@appstore/ContainerManager/usr/bin/docker 4 pipe:[14184191]
3179 /volume2/@appstore/ContainerManager/usr/bin/docker 5 pipe:[14184191]
3179 /volume2/@appstore/ContainerManager/usr/bin/docker 6 socket:[14185169]
3179 /volume2/@appstore/ContainerManager/usr/bin/docker 7 socket:[14185172]
15639 /usr/bin/bash 0 /dev/pts/1
15639 /usr/bin/bash 1 /dev/pts/1
15639 /usr/bin/bash 2 /dev/pts/1
15639 /usr/bin/bash 3 socket:[11735039]
15639 /usr/bin/bash 255 /dev/pts/1

zhaonc@zhaonc-nas:~$ pstree -ps 3104
systemd(1)───sshd(9653)───sshd(3099)───sshd(3103)───docker(3104)─┬─{docker}(3108)
├─{docker}(3109)
├─{docker}(3110)
├─{docker}(3111)
└─{docker}(3112)
```

With this issue, it is practically impossible to use Docker on Synology NAS, which surprising that I have not yet seen the issue widely reported - therefore I do suspect this may have been an isolated issue on my side.. Having submitted a support ticket to Synology, I have created a scheduled task to kill these processes on hourly basis:

```bash
#!/bin/bash

n=$(pgrep -f "docker system dial-stdio" | wc -l)

if [ $n -gt 0 ]; then
    ps -ef | grep "docker system dial-stdio" | grep -v grep | awk '{print $2}' | xargs kill -9
    echo "Killed $n processes"
else
    echo "No process found"
fi
```

I will share more updates once I hear back from Synology support.
