"""
Django settings for guyamoe project.

Generated by 'django-admin startproject' using Django 2.2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""


"""
    !! DOCKER NOTE !!
    Modifying the root guyamoe/settings.py file will trigger
    a Django restart, but the bind will shadow that file. Thus,
    change this file if you want to reconfigure.

    For all intents and purposes, this file should be compatible
    with the base settings.py, but with some slight changes to
    the db and memcached naming.

"""

import subprocess
import os
import json
from django.core.exceptions import ImproperlyConfigured


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

SECRET_KEY = "asdf"  # randomly generated by yours truly
CANONICAL_ROOT_DOMAIN = "guya.moe"
X_FRAME_OPTIONS = "DENY"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["web", "localhost"]

CANONICAL_SITE_NAME = "guya.moe"

# Application definition

INSTALLED_APPS = [
    "api.apps.ApiConfig",
    "reader.apps.ReaderConfig",
    "homepage.apps.HomepageConfig",
    "misc.apps.MiscConfig",
    "proxy.apps.ProxyConfig",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.sitemaps",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_extensions",
]

SITE_ID = 1

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.memcached.MemcachedCache",
        "LOCATION": "memcached:11211",
    }
}

MIDDLEWARE = [
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "homepage.middleware.ReferralMiddleware",
]

# REFERRAL_SERVICE = 'http://127.0.0.1:8080' # Change this to where-ever Ai is hosted

ROOT_URLCONF = "guyamoe.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
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

WSGI_APPLICATION = "guyamoe.wsgi.application"


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "kaguyamoe",
        "USER": "POSTGRES_USER",
        "PASSWORD": "POSTGRES_PASSWORD",
        "HOST": "postgres",
        "PORT": "",
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",},
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

PREFERRED_SORT = ["3", "2", "1", "4"]

STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static_global"),
]
STATIC_VERSION = (
    f"?v={subprocess.check_output('git rev-parse --short HEAD', shell=True, text=True)}"
)
# STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
# MEDIAFILES_DIRS = [
#    os.path.join(BASE_DIR, "media"),
#    '/media/',
# ]

MAIL_DISCORD_WEBHOOK_ID = 1
MAIL_DISCORD_WEBHOOK_TOKEN = ""

IMGUR_CLIENT_ID = ""
