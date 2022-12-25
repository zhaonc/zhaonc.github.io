---
title: "Copy files between Linux hosts over LAN"
layout: post
date: '2022-12-25 17:51:00 +0800'
tags:
- linux
- nas
categories:
- Notes
excerpt: Use tar to move large number of files between hosts
---

## Goal

Move files from one Linux host to another (specifically in my case, migrating files to another smaller NAS).

- Large number of files (perhaps in millions because of project files), and large total size (3+TB)
- Need to keep file attributes and ownership
- Need to be robust but fast

Some limitations in this case:

- No spare disks - therefore cannot use [dd](https://linuxhint.com/clone-disk-using-dd-linux/)
- Not "migration" - therefore cannot use out-of-box solutions e.g. [Synology migration](https://www.synology.com/en-sg/dsm/feature/migration)
- The two NAS hosts are connected via Gigabit ethernet
- Specifically in my case, the two Synology NAS hosts are both relatively slow, and certain packages such as `pv` are missing on their OS

## Solution

Mount the destination host folder (via Samba) on another PC. Then on the PC run the following:

```bash
echo $PASSWORD | ssh $SOURCE_HOST "sudo -S tar cf - -C $PATH ." | pv | pigz | cat > $DEST_HOST
```

## Discussion

- __rsync vs tar__: Given we have large number of files, `tar` has proven to be much faster than using `rsync` between the hosts, while it keeps attributes and ownership
- __compression__: Specifically in this case, compression seems to have improved the performance as destination is slow
- __via third PC__: Technically not necessary, but running on the third PC gives us `pv` which shows us the progress, and `pigz` which utilizes all cores and avoids bottleneck on NAS's low-spec CPU
- __Samba vs SSH__: In my test, Samba has been faster than SSH (or `rsync` daemon over SSH), potentially due to less overhead
- __path__: `-C` would change the working directory, and therefore essentially "remove" this hierarchy (useful when we want to extract to a different location)
- __why root__: `echo $PASSWORD` and `sudo -S` is to run with `root` to copy files owned by other users. To avoid storing password into shell history, simply insert a space before the command
