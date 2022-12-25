---
title: "Organize photos"
layout: post
date: '2022-11-08 00:13:00 +0800'
categories: platform
excerpt: Update EXIF and modified date
---

## Motivation

Over the years I have migrated a few times among various photo management tools, from [Google Picasa](https://en.wikipedia.org/wiki/Picasa), to Google Photos, Apple Photos, [Synology Moments](https://www.synology.com/en-sg/dsm/feature/moments), and most recently [Synology Photos](https://www.synology.com/en-sg/dsm/feature/photos). The photos also came from various sources, e.g. digital camera (before smart phones), smart phones, and photos saved from instant messengers (e.g. WhatsApp) and social media platform. Recently I decided to finally clean up my photos archive, as there were so many duplicates and incorrect metadata. It turned out to be more complex than I thought.

## Remove Synology thumbnails

Synology automatically generated thumbnail images `@eaDir` for indexing. These images are not necessary (and can be troublesome when we update metadata later).

```bash
find . -type d -name @eaDir -prune -exec rm -r {} \;
```

Note the usage of `-prune` to avoid showing errors like `find: ...: No such file or directory` so `find` would not go into the deleted folders.

## Update photo's EXIF time

Some photos (e.g. those from WhatsApp) do not come with EXIF data. Most of the times, the photo management software would fall back to file's modified date time. To update the EXIF date time:

```bash
exiftool -DateTimeOriginal="2019:07:06 17:30:00+08:00" photo.jpg
```

## Sync modified date time of live photo's video

Live photos from iPhone have two components: an image and a video clip. Somehow some video clips' modified time was updated (perhaps due to migration). With such discrepancy, photo management software would incorrectly display these video clips.

First, update the image's modified date time from its EXIF information. We need to use [ExifTool](https://exiftool.org/).

```bash
exiftool '-DateTimeOriginal>FileModifyDate' .
```

Optionally, you may need to specify the timezone:

```bash
exiftool '-DateTimeOriginal>FileModifyDate' -TimeZone=+8:00 .
```

Then update the MP4's modified date time from JPG files of the same name.

```bash
for f in *.MP4; do touch -r ${f//MP4/JPG} $f; done
```

Note you may need to replace MP4/JPG with the correct file extensions.

## De-duplicates

Given the photos were from multiple sources, there are duplicates in the same folder. To de-duplicate the photos, I'd start by looking if the photos are the same. For the duplicates, I'd prefer keeping the ones with live photo. If there are duplicated live photos, then I'd sort the files by their names alphabetically and keep the first one (as the duplicated one may have names like "photo(1).jpg").

Since this is rather tedious, I wrote a small python script to automate this. Inspirations especially those on the hash part go to [Mateusz Soszyński](https://github.com/TheLastGimbus), who came up with the excellent tool [GooglePhotosTakeoutHelper](https://github.com/TheLastGimbus/GooglePhotosTakeoutHelper/). See my script in [this repo](https://github.com/zhaonc/photo-utils/blob/main/dedup.py).

```bash
python dedup.py <photos_dir> <trash_dir>
```