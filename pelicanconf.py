AUTHOR = 'EUMETNET PP Module'
SITENAME = 'EUMETNET EUPP Benchmark'
SITEURL = ""
SITETITLE = "EUPP Benchmark"

PATH = "content"

TIMEZONE = 'Europe/Rome'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("Datasets documentation", "https://eupp-benchmark.github.io/EUPPBench-doc/"),
    # ("Pelican", "https://getpelican.com/"),
    # ("Python.org", "https://www.python.org/"),
    # ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    # ("You can modify those links in your config file", "#"),
)

# Social widget
SOCIAL = (
    ("You can add links in your config file", "#"),
    ("Another social link", "#"),
)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

THEME = "/home/jodemaey/pelican-themes/Flex"
BROWSER_COLOR = "#94c1cf"
SITEDESCRIPTION = "Presentation and News about the EUPP Benchmark activities"
SITELOGO = SITEURL + "/images/EUMETNETLogo.png"
FAVICON = SITEURL + "/images/EUMETNETLogo.png"

ROBOTS = "index, follow"

CC_LICENSE = {
    "name": "Creative Commons Attribution-ShareAlike",
    "version": "4.0",
    "slug": "by-sa"
}

COPYRIGHT_YEAR = 2024

# STATIC_PATHS = ["extra/custom.css"]
#
# EXTRA_PATH_METADATA = {
#     "extra/custom.css": {"path": "static/custom.css"},
# }
#
# CUSTOM_CSS = "static/custom.css"

MAIN_MENU = True

# ADD_THIS_ID = "ra-77hh6723hhjd"
# DISQUS_SITENAME = "yoursite"
# GOOGLE_ANALYTICS = "UA-1234-5678"
# GOOGLE_TAG_MANAGER = "GTM-ABCDEF"

# # Enable i18n plugin.
# PLUGINS = ["i18n_subsites"]
# # Enable Jinja2 i18n extension used to parse translations.
# JINJA_ENVIRONMENT = {"extensions": ["jinja2.ext.i18n"]}
#
# # Translate to German.
# DEFAULT_LANG = "de"
# OG_LOCALE = "de_DE"
# LOCALE = "de_DE"
#
# # Default theme language.
# I18N_TEMPLATES_LANG = "en"
#
# # Pelican-search Configuration
# STORK_INPUT_OPTIONS = {"stemming": "German", "url_prefix": SITEURL}

THEME_COLOR_AUTO_DETECT_BROWSER_PREFERENCE = True
THEME_COLOR_ENABLE_USER_OVERRIDE = True

GITHUB_CORNER_URL = "https://github.com/EUPP-benchmark"
