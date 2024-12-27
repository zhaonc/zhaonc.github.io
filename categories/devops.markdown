---
layout: page
title: devops
permalink: /categories/devops/
---

{% assign category_name = "devops" %}
<div id="archives">
    {% for post in site.categories[category_name] %}
    <li><span>{{ post.date | date: "%Y-%m-%d" }}</span> &raquo; <a href="{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a></li>
    {% endfor %}
</div>
