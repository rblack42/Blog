#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Roie R. Black'
SITENAME = u"Random Ramblings from Roie Black's Life"
SITEURL = ''

PATH = 'content'
STATIC_PATHS = ['images']

TIMEZONE = 'America/Chicago'

USE_FOLDER_AS_CATEGORY = False
DEFAULT_LANG = u'en'
DEFAULT_CATEGORY = 'Life'

THEME = 'themes/pelican-bootstrap3'
BANNER = 'images/collingsF4.png'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('ACC Home Page', 'http://www.austincc.edu/rblack/'),
         ('GitHub', 'https://github.com/rblack42'),)

# Social widget
SOCIAL = (('LinkedIn', 'https://www.linkedin.com/profile/view?id=103423831&trk=spm_pic'),)

DEFAULT_PAGINATION = 10
DISPLAY_CATEGORIES_ON_MENU = True
DISPLAY_PAGES_ON_MENU = True

YEAR_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/{date:%b}/index.html'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
