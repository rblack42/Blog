AUTHOR = u'Roie R. Black'
SITENAME = u"Random Ramblings"
SITEURL = 'http://www.co-pylit.org/blog'

PATH = 'content'
TIMEZONE = 'America/Chicago'
DEFAULT_LANG = u'en'

PLUGINS = None

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
RELATIVE_URLS = True

# Theme Settings ##############################################################
THEME = 'themes/pelican-clean-blog'
HEADER_TITLE_LOGO = 'images/Phantom_II.jpg'
FAVICON = 'favicon.ico'
STATIC_PATHS= ['images', 'extra/favicon.ico']
EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'}
}
DISPLAY_PAGES_ON_MENU = True
