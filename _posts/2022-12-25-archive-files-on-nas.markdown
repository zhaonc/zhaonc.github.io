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

## First attempt: rsync over SSH and Samba

```bash
# On source NAS
sudo rsync -avh $PATH $NAS:/$DEST
```

`rsync` is handy here because it persists the attributes and ownership, and it could resume if transmission is interrupted. Note in modern version of `rsync` we could also do `--info=progress2` for aggregated information on progress, however this is not supported on my NAS. Also running this with `root` privileges because there were files owned by other users.

When I tested this, it is unfortunately slow (it was so slow that I didn't even have to benchmark it). Thinking this may be due to the SSH overhead, I switched over to Samba. First mounted the destination to the source NAS `$DEST`, then with a small change in path: `sudo rsync -avh $PATH $DEST`. This resulted in a much better throughput.

Can we do better?

1. How can we get overall idea of the progress? 3TB takes at least 6.8 hours to complete theoretcally.
2. Technically we are doing an one-time dump. We will not be "synchronizing" them. Therefore the "incremental" benefit of `rsync` is not relevant here.
3. Can we also compress to achieve an even better throughput? Compression over `rsync` is not ideal because it operates on a per file basis and we have huge number of files.

## Second attempt: tar

```bash
# On source NAS
sudo tar -vczf - -C $PATH . > $DEST
```

Here `tar` places all the files into one archive and compresses with `gzip`. However very quickly I realized the weak CPU on the source NAS now becomes the bottleneck. Also the verbose mode in tar is not very helpful as it only lists out the files it is touching. Ideally we want to show how much data has been processed so far.

## Final solution

```bash
# On another PC
sudo tar cf - -C $PATH . | ssh $PC "pv --force | pigz" > $DEST
```

Here we work around the NAS CPU bottleneck by using a third PC, which also enables us to use `pv` to show progress and `pigz` to utilize all cores in compressing. Note here the destination NAS was mounted to `$DEST`. Also `--force` is required here as "pv will not output any visual display if standard error is not a terminal"[^1].

[^1]: [man pv](https://man7.org/linux/man-pages/man1/pv.1.html)
