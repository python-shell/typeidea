from .base import * #NOQA

DEBUG = True
# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'typeidea_db',
        'USER': 'root',
        'PASSWORD': '123456',
        'HOST': '192.168.0.106',
        'PORT': '3306',
        'OPTIONS': {
            'charset': 'utf8'
        }
    }
}

# LANGUAGE_CODE = 'en-us'

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
        'height': 300,
        'width': 800,
        'tabSpace': 4,
        'extraPlugins': 'codesnippet'
    }
}

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
CKEDITOR_UPLOAD_PATH = "article_images"

# DJANGO REST FRAMEWORK CONFIG
# REST_FRAMEWORK = {
#     'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
#     'PAGE_SIZE': 2
# }

# INSTALLED_APPS += [
#     'debug_toolbar',
# ]
#
# MIDDLEWARE += [
#     'debug_toolbar.middleware.DebugToolbarMiddleware',
# ]
# ip = '192.168.0.104'
# INTERNAL_IPS = [ip]


# DEBUG_TOOLBAR_PANELS = [
#     'debug_toolbar.panels.versions.VersionsPanel',
#     'debug_toolbar.panels.timer.TimerPanel',
#     'debug_toolbar.panels.settings.SettingsPanel',
#     'debug_toolbar.panels.headers.HeadersPanel',
#     'debug_toolbar.panels.request.RequestPanel',
#     'debug_toolbar.panels.sql.SQLPanel',
#     'debug_toolbar.panels.staticfiles.StaticFilesPanel',
#     'debug_toolbar.panels.templates.TemplatesPanel',
#     'debug_toolbar.panels.cache.CachePanel',
#     'debug_toolbar.panels.signals.SignalsPanel',
#     'debug_toolbar.panels.logging.LoggingPanel',
#     'debug_toolbar.panels.redirects.RedirectsPanel',
# ]

# DEBUG_TOOLBAR_PANELS = [
#     'djdt_flamegraph.FlamegraphPanel',
# ]

# DEBUG_TOOLBAR_CONFIG = {
#     'JQUERY_URL': 'https://cdn.bootcss.com/jquery/3.3.1/jquery.min.js',
# }

# INSTALLED_APPS += [
#     'pympler',
# ]

# DEBUG_TOOLBAR_PANELS = [
#     'pympler.panels.MemoryPanel',
# ]

# INSTALLED_APPS += [
#     'debug_toolbar_line_profiler',
# ]
#
# DEBUG_TOOLBAR_PANELS = [
#     'debug_toolbar_line_profiler.panel.ProfilingPanel',
# ]

# SILK CONFIG
INSTALLED_APPS += [
    'silk',
]

MIDDLEWARE += [
    'silk.middleware.SilkyMiddleware',
]

