# -*- coding: utf-8 -*-
from os import environ

from .base import *


# Email configuration
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = environ.get('EMAIL_HOST', 'smtp.gmail.com')
EMAIL_HOST_PASSWORD = environ.get('EMAIL_HOST_PASSWORD', '')
EMAIL_HOST_USER = environ.get('EMAIL_HOST_USER', 'your_email@example.com')
EMAIL_PORT = environ.get('EMAIL_PORT', 587)
EMAIL_SUBJECT_PREFIX = '[priver.org] '
EMAIL_USE_TLS = True
SERVER_EMAIL = EMAIL_HOST_USER

# Cache configuration
CACHES = {}

# Secret configuration
SECRET_KEY = environ.get('SECRET_KEY')
