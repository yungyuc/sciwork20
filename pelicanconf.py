#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'sciwork team'
SITENAME = 'Sciwork'
SITEURL = 'https://conf.sciwork.dev/2020'
SITESUBTITLE = 'code for science'

PATH = 'content'

TIMEZONE = 'Asia/Taipei'

DEFAULT_LANG = 'en'
ARTICLE_TRANSLATION_ID = None
PAGE_TRANSLATION_ID = None

DEFAULT_CATEGORY = 'Misc'
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False
MENUITEMS = (
    ('Welcome', 'index.html'),
    ('Program', 'program.html'),
    ('Sponsors', 'sponsors.html'),
    ('Venue', 'venue.html'),
)

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
#    ('Pelican', 'http://getpelican.com/'),
#    ('Python.org', 'http://python.org/'),
#    ('Jinja2', 'http://jinja.pocoo.org/'),
#    ('You can modify those links in your config file', '#'),
)

# Social widget
SOCIAL = (
#    ('twitter', 'https://twitter.com/sciwork/'),
)

DEFAULT_PAGINATION = 10
#PAGINATED_DIRECT_TEMPLATES = ('categories', 'archives')

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
