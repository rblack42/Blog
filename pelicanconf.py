#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Roie R. Black'
SITENAME = u"Random Ramblings"
BANNER_SUBTITLE = u"from Roie Black's Life"
SITEURL = 'http://www.co-pylit.org/blog'

PATH = 'content'
STATIC_PATHS = ['images', 'extra/robots.txt', 'extra/favicon.ico']
EXTRA_PATH_METADATA = {
    'exra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'}
}

TIMEZONE = 'America/Chicago'

USE_FOLDER_AS_CATEGORY = False
DEFAULT_LANG = u'en'
DEFAULT_CATEGORY = 'Life'


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
SOCIAL = (('LinkedIn', 'https://www.linkedin.com/profile/view?id=103423831&trk=spm_pic'),
        ('Google+', 'https://www.google.com/+RoieBlack'),)

DEFAULT_PAGINATION = 10
DISPLAY_CATEGORIES_ON_MENU = True
DISPLAY_PAGES_ON_MENU = True

ARCHIVE_SAVE_AS = 'archives.html'

YEAR_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/{date:%b}/index.html'

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = False

# Exterior Services ###########################################################
GOOGLE_ANALYTICS = "UA-44564689-4"

# Theme Settings ##############################################################
THEME = 'themes/pelican-bootstrap3'
BOOTSTRAP_THEME = 'cosmo'
SHOW_ARTICLE_CATEGORY = False
FAVICON = 'images/favicon.png'
BANNER = 'images/collingsF4.png'

TAG_CLOUD_STEPS = 4
TAG_CLOUD_MAX_ITEMS = 20
TAGS_URL = "tag-{slug}.html"
TAGS_SAVE_A = "tags.html"
TAG_SAVE_AS = "tag-{slug}.html"
TAG_URL = "tag-{slug}.html"

PLUGIN_PATHS = ['plugins']
PLUGINS = [
    'i18n_subsites',
    'sitemap',
    'pelican_comment_system',
    'tag_cloud',
    'tipue_search',
]
JINJA_ENVIRONMENT =  {"extensions" : ['jinja2.ext.i18n'] }

PELICAN_COMMENT_SYSTEM = False
SEARCH_URL = SITEURL + '/search.html'
DIRECT_TEMPLATES = ['search', 'index', 'tags']
SITEMAP = {
    'format': 'xml',
    'exclude': ['tag/', '/category/']
}
ISSO_SITEURL = 'http://isso.co-pylit.org'
