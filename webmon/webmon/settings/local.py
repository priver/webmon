# -*- coding: utf-8 -*-
from .base import *

# Debug configuration
DEBUG = True
TEMPLATE_DEBUG = DEBUG

# Email configuration
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Cache configuration
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}

# Debug toolbar configuration
INSTALLED_APPS += ('debug_toolbar', )
INTERNAL_IPS = ('127.0.0.1', )
MIDDLEWARE_CLASSES += ('debug_toolbar.middleware.DebugToolbarMiddleware', )
DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
    'SHOW_TEMPLATE_CONTEXT': True,
}

STATICFILES_DIRS = ('C:\\projects\\webmon\\webmon\\static\\', )