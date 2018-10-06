#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'mpeaton'
SITENAME = 'Michael P. Eaton'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None

#FEED_ALL_ATOM = 'feeds/all.atom.xml'
#FEED_ALL_RSS = 'feeds/all.rss.xml'
#AUTHOR_FEED_RSS = 'feeds/%s.rss.xml'
#RSS_FEED_SUMMARY_ONLY = False

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget

SOCIAL = (('twitter', 'http://twitter.com/mpeaton'),
          ('linkedin', 'http://www.linkedin.com/in/mpeaton'),
          ('github', 'http://github.com/mpeaton'),
          ('stackoverflow', 'https://stackoverflow.com/cv/mpeaton'),)

DEFAULT_PAGINATION = 10
STATIC_PATHS = ['images']
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
