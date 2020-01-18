#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import os

AUTHOR = 'Sciwork Team'
SITENAME = 'Sciwork'
SITEURL = os.environ.get('SITEURL', 'https://conf.sciwork.dev/2020')
REGURL = 'https://sciwork.kktix.cc/events/sciwork2020'
if os.environ.get('GOOGLE_ANALYTICS'):
    GOOGLE_ANALYTICS = os.environ['GOOGLE_ANALYTICS']
SITESUBTITLE = 'code for science'
SITEDESC = (
    'Sciwork is a conference to share and discuss computer code for scientific, '
    'numerical, and engineering work.  We will focus on source code, and encourage '
    'attendees to share open-source work for both scientific researches and '
    'technical applications.')
TWITTER_USERNAME = 'sciwork'

PATH = 'content'
STATIC_PATHS = ['images']

TIMEZONE = 'Asia/Taipei'

DEFAULT_LANG = 'en'
ARTICLE_TRANSLATION_ID = None
PAGE_TRANSLATION_ID = None

PLUGIN_PATHS = ['plugins']
PLUGINS = ['headerid']
HEADERID_LINK_CHAR = '&nbsp;'
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.toc': {'permalink': '&nbsp;'},
    },
}

DEFAULT_CATEGORY = 'Misc'
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False
MENUITEMS = (
    ('Welcome', 'index.html'),
    ('Blog', 'blog.html'),
    ('Program', 'program.html'),
    ('Sponsors', 'sponsors.html'),
    ('Venue', 'venue.html'),
    ('About', 'about.html'),
)


CATEGORY_SAVE_AS = ''
# If pagination is active, subsequent pages will reside in output/blog`n`.html.
INDEX_SAVE_AS = 'blog.html'
DEFAULT_PAGINATION = 10
#PAGINATED_DIRECT_TEMPLATES = ('categories', 'archives')
ARTICLE_PATHS = ['articles']
ARTICLE_SAVE_AS = 'articles/{date:%Y}/{slug}.html'
ARTICLE_URL = 'articles/{date:%Y}/{slug}.html'

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

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
