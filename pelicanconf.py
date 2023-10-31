# Site settings
AUTHOR = 'Bode Okunfolami'

SITENAME = 'Pythoneer'

SITEURL = ''

SITEIMAGE = 'theme/pythoneer-dev.png'

SITESUBTITLE = 'Learn computer programming with simplicity and clarity'

HIDE_AUTHORS = True

FOOTER_LINKS = [['pythoneer.dev', 'https://pythoneer.dev']]

DEFAULT_PAGINATION = 8

# URL
ARTICLE_URL = '{slug}/'
ARTICLE_SAVE_AS = '{slug}/index.html'
PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'

# Path Settings
OUTPUT_PATH = 'blog/'

PATH = 'content'

# Timezone and language
TIMEZONE = 'UTC'

DEFAULT_LANG = 'en'

# Markdown setting
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
    },
    'output_format': 'html5',
}


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None

CATEGORY_FEED_ATOM = None

TRANSLATION_FEED_ATOM = None

AUTHOR_FEED_ATOM = None

AUTHOR_FEED_RSS = None

# Social widget
SOCIAL = (('Twitter', 'https://www.twitter.com/bodeokunfolami'),
          ('Github', 'https://www.github.com/bodeokunfolami'),
          ('Linkedin', 'https://www.linkedin.com/in/bode-okunfolami-04156419a/'),
          ('Youtube', 'https://www.youtube.com/@PythoneerAcademy'))



# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Theme
THEME = 'theme/'

BOOTSTRAP_CSS = 'theme/style.css'

THEME_CSS_OVERRIDES = ['theme/oldstyle.css',]

THEME_JS_OVERRIDES = ['theme/main.js',]

# Analytics
GOOGLE_ANALYTICS = ''

# Plugins
PLUGIN_PATHS = ['plugins']

PLUGINS = ['pelican-bootstrapify', 'sitemap']

SITEMAP = {
    "format": "xml",
    "priorities": {
        "articles": 0.5,
        "indexes": 0.5,
        "pages": 0.5
    },
    "changefreqs": {
        "articles": "monthly",
        "indexes": "daily",
        "pages": "monthly"
    }
}

BOOTSTRAPIFY = {
    'h3': ['my-3', 'my-md-4'],
    'table': ['table', 'table-bordered'],
    'img': ['img-fluid', 'my-3', 'my-md-4', 'shadow'],
    'blockquote': ['custom-blockquote'],
}
