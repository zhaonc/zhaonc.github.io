---
title: "Archive files on NAS"
layout: post
date: '2022-12-25 17:51:00 +0800'
categories: platform
excerpt: Use tar to archive large number of files
---

## Goal

Archive files on a NAS onto another NAS so that I could migrate the filesystem to [btrfs](https://www.synology.com/en-my/dsm/Btrfs). This means:

- large number of files to be archived (perhaps in millions, e.g. project files), and large in total size (>3TB)
- need to keep file attributes and ownership
- need to be safe but fast
- in this case there is no spare disks - therefore cannot use [dd](https://linuxhint.com/clone-disk-using-dd-linux/)
- specifically in this case, the two Synology NAS hosts are both relatively slow, and certain packages such as `pv` are missing on their OS

## Solution

Mount the destination host folder (via Samba) on a computer. Then on the computer run the following:

```bash
echo $PASSWORD | ssh $SOURCE_HOST "sudo -S tar cf - -C $PATH ." | pv | pigz | cat > $DEST_HOST
```

## Discussion

- __rsync vs tar__: Given we have large number of files, `tar` has proven to be much faster than using `rsync` between the NAS boxes, while it keeps attributes and ownership
- __compression__: In my case, the destination NAS is slower and it struggled to keep up. Therefore compression removes this bottleneck
- __why another computer__: While not necessary, running on the computer gives us `pv` which shows the progress, and `pigz` which utilizes all cores and avoids bottleneck on NAS's low-spec CPU
- __Samba vs SSH__: In my experiments, Samba has been faster than SSH (or `rsync` daemon over SSH), potentially due to less overhead
- __path__: `-C` would change the working directory, and therefore essentially "remove" this hierarchy (useful when extracted to a different directory later)
- __why root__: `echo $PASSWORD` and `sudo -S` is to run with `root` to copy files owned by other users. To avoid storing password into shell history, simply insert a space before the command
