import os
from .base import *  # noqa


DEBUG = False

SECRET_KEY = os.environ["DJANGO_SECRET_KEY"]
