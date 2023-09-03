---
layout: page
title: setup
permalink: /categories/setup/
---

{% assign category_name = "setup" %}
<div id="archives">
    {% for post in site.categories[category_name] %}
    <li><span>{{ post.date | date: "%Y-%m-%d" }}</span> &raquo; <a href="{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a></li>
    {% endfor %}
</div>
