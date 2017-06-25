#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Nelson Zhao'
SITENAME = u'Nelson Zhao'
SITEURL = 'http://localhost:8000'

PATH = 'content'

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
#LINKS = (('My Douban', 'https://www.douban.com/people/zhaonaichuan/'),)

# Social widget
SOCIAL = (('envelope-o', 'mailto:zhaonaichuan+com@gmail.com'),
          ('twitter', 'http://twitter.com/zhaonc'),
          ('linkedin', 'http://www.linkedin.com/in/zhaonc'),
          ('github', 'http://github.com/zhaonc'),)
# SOCIAL = (('envelope-o', 'mailto:zhaonaichuan+com@gmail.com'),
#           ('twitter', 'http://twitter.com/zhaonc'),
#           ('linkedin', 'http://www.linkedin.com/in/zhaonc'),
#           ('github', 'http://github.com/zhaonc'),
#           ('stack-overflow', 'http://stackoverflow.com/users/4624073/zhaonc'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Theme
THEME = 'themes/Flex'

# Static resources
# CNAME and avatar
STATIC_PATHS = ['images', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},
                       'images/favicon.ico': {'path': 'favicon.ico'},}

# Theme-specific (Flex) settings
SITETITLE = u'Nelson Zhao'
SITESUBTITLE = u'Financial Technology Developer'
SITELOGO = SITEURL + '/images/avatar.jpg'
SITEDESCRIPTION = u"Nelson's home page."
COPYRIGHT_YEAR = 2016
CC_LICENSE = {
    'name': 'Creative Commons Attribution-ShareAlike',
    'version': '4.0',
    'slug': 'by-sa'
}
MAIN_MENU = True
MENUITEMS = [('Archives', SITEURL + '/archives.html'),
             ('Categories', SITEURL + '/categories.html'),
             ('Tags', SITEURL + '/tags.html'), ]
FAVICON = SITEURL + '/favicon.ico'
