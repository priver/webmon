# -*- coding: utf-8 -*-
from os import environ

from .base import *

# Secret configuration
SECRET_KEY = environ.get('SECRET_KEY')
