# See https://docs.djangoproject.com/en/3.2/topics/settings/
# and https://docs.djangoproject.com/en/3.2/ref/settings/

import os
from pathlib import Path


# Build paths inside the project like this: BASE_DIR / 'subdir'.

BASE_DIR = Path(__file__).resolve().parent.parent

# -------- Application definition --------

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.sites",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "crispy_forms",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "rest_framework",
    "rest_framework.authtoken",
    "orchard",
    "orchard.users.apps.UsersConfig",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

WSGI_APPLICATION = "orchard.wsgi.application"

ROOT_URLCONF = "orchard.urls"

ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS", "localhost").split()

# -------- Templates --------

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# -------- Database --------

# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

pg_conn_keys = ("NAME", "USER", "PASSWORD", "HOST", "PORT")
pg_conn_info = {k: os.environ.get(f"DJANGO_DB_{k}") for k in pg_conn_keys}

if all(pg_conn_info.values()):
    engine = "django.db.backends.postgresql_psycopg2"
    engine_config = pg_conn_info
else:
    engine = "django.db.backends.sqlite3"
    engine_config = {"NAME": BASE_DIR.parent / "db.sqlite3"}

DATABASES = {
    "default": {"ENGINE": engine, **engine_config},
}

# -------- Default primary key field type --------

# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# -------- Auth --------

# https://docs.djangoproject.com/en/dev/ref/settings/#auth-user-model
# https://docs.djangoproject.com/en/dev/ref/settings/#login-redirect-url
# https://docs.djangoproject.com/en/dev/ref/settings/#login-url

AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
]
AUTH_USER_MODEL = "users.User"
LOGIN_REDIRECT_URL = "users:redirect"
LOGIN_URL = "account_login"

# -------- Password validation --------

# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# -------- Internationalization --------

# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"

USE_I18N = False
USE_L10N = False
USE_TZ = True

# -------- Static files (CSS, JavaScript, Images) --------

# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = "/static/"

# -------- Email --------

DEFAULT_FROM_EMAIL = os.environ.get("DJANGO_DEFAULT_FROM_EMAIL")
INSTALLED_APPS += ["anymail"]  # noqa F405
EMAIL_BACKEND = "anymail.backends.mailgun.EmailBackend"
ANYMAIL = {
    "MAILGUN_API_KEY": os.environ.get("MAILGUN_API_KEY"),
    "MAILGUN_SENDER_DOMAIN": os.environ.get("MAILGUN_DOMAIN"),
}
