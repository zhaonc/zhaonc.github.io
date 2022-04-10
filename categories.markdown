---
layout: page
title: Categories
permalink: /categories/
---

<div id="archives">
{% for category in site.categories %}
  <div class="archive-group">
    {% capture category_name %}{{ category | first }}{% endcapture %}
    <a name="{{ category_name | slugize }}" href="{{ site.baseurl }}{{ category_name | slugize }}"><h1 class="category-head">{{ category_name }}</h1></a>
    {% for post in site.categories[category_name] limit:5 %}
    <li><span>{{ post.date | date: "%Y-%m-%d" }}</span> &raquo; <a href="{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a></li>
    {% endfor %}
  </div>
{% endfor %}
</div>