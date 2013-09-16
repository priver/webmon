# -*- coding: utf-8 -*-
import dj_database_url
from unipath import Path


# Path configuration
BASE_DIR = Path(__file__).ancestor(3)

# Debug configuration
DEBUG = False
TEMPLATE_DEBUG = DEBUG

# Manager configuration
ADMINS = (
    ('Mikhail Priver', 'mikhail@priver.org'),
)

MANAGERS = ADMINS

# Database configuration
#DATABASES = {'default': dj_database_url.config()}

# General configuration
TIME_ZONE = 'Europe/Moscow'
LANGUAGE_CODE = 'ru-ru'
SITE_ID = 1
USE_I18N = True
USE_L10N = True
USE_TZ = True
LOCALE_PATHS = (BASE_DIR.child('locale'), )

# Media configuration
MEDIA_ROOT = BASE_DIR.child('media')
MEDIA_URL = '/media/'

# Static file configuration
STATIC_ROOT = BASE_DIR.child('assets')
STATIC_URL = '/static/'
STATICFILES_DIRS = (BASE_DIR.child('static'), )

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

# Secret configuration
# Note: This key only used for development and testing.
SECRET_KEY = r'+5xw$95^-wdq3kuc_3$zt*ht^ut84$t+-ojkl*ruvu5fdo_!kv'

# Site configuration
ALLOWED_HOSTS = ['*', ]

# Fixture configuration
FIXTURE_DIRS = (BASE_DIR.child('fixtures'), )

# Template configuration
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.request',
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

TEMPLATE_DIRS = (BASE_DIR.child('templates'), )

# Middleware configuration
MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

# URL configuration
ROOT_URLCONF = 'webmon.urls'

# WSGI configuration
WSGI_APPLICATION = 'webmon.wsgi.application'

# Apps configuration
INSTALLED_APPS = (
    # django apps
    #'django.contrib.auth',
    #'django.contrib.contenttypes',
    'django.contrib.sessions',
    #'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #'django.contrib.admin',
    # 'django.contrib.humanize',

    # 3rd party_apps
    #'south',

    # webmon apps
    # 'monitor'
)

# Logging configuration
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
