#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os.path

AUTHOR = '__AUTHOR__'
SITENAME = '__TITLE__'
SITEURL = '__DOMAIN____PATH__'
SITESUBTITLE = "__SUBTITLE__"
MENUITEMS = [
    # ("title", "link")
]

DISPLAY_PAGES_ON_MENU = True

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'
LOCALE = 'en_GB.UTF-8'
APP_DIR = '__APPPATH__'

PATH = os.path.join(APP_DIR, "content")
THEME= os.path.join(APP_DIR, "themes", __THEMENAME__)
PLUGIN_APP_PATH= os.path.join(APP_DIR, "plugins")

ARTICLE_PATHS = (d for d in os.listdir() if os.is_dir(os.path.join(PATH, d)) and d != "static")
STATIC_PATHS = ('static', ) 
ARTICLE_SAVE_AS = '{category}/{slug}.html'
ARTICLE_URL = '{category}/{slug}.html'

# plugins are shared for all pelican instances
PLUGIN_PATHS = [PLUGIN_APP_PATH, ]
PLUGINS = ['pelican-readtime', 'neighbors']

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/atom.xml'
CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'
FEED_ALL_RSS = 'feeds/rss.xml'
CATEGORY_FEED_RSS = 'feeds/{slug}.rss.xml'

TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

COPYRIGHT = AUTHOR
DEFAULT_PAGINATION = 30
LAST_ARTICLE_COUNT = 9

OUTPUT_PATH="__FINALPATH__"
DELETE_OUTPUT_DIRECTORY = False

# DISQUS_SITENAME='discus-key'
