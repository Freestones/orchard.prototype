from django.core.management.utils import get_random_secret_key
from .base import *  # noqa


DEBUG = False

SECRET_KEY = get_random_secret_key()

SITE_ID = 1
