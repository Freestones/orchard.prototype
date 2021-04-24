import os
from django.core.management.utils import get_random_secret_key
from .base import *  # noqa


DEBUG = bool(os.environ.get("DJANGO_DEBUG", "yes"))

SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY", get_random_secret_key())

SITE_ID = 1
