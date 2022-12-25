---
layout: page
title: Tags
permalink: /tags/
---

<div id="archives">
{% for tag in site.tags %}
  <div class="archive-group">
    {% capture tag_name %}{{ tag | first }}{% endcapture %}
    <h2 class="category-head">{{ tag_name }}</h2>
    {% for post in site.tags[tag_name] %}
    <li><span>{{ post.date | date: "%Y-%m-%d" }}</span> &raquo; <a href="{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a></li>
    {% endfor %}
  </div>
{% endfor %}
</div>