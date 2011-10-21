# -*- coding: utf-8 -*-
# Django settings for project project.

import os.path
import posixpath

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

# Change the following to False for production
DEBUG = True
TEMPLATE_DEBUG = True
SERVE_MEDIA = True

INTERNAL_IPS = [
    "127.0.0.1",
]

ADMINS = [
    ("Flake", "flakever@gmail.com"),
]

MANAGERS = ADMINS

DATABASES = {
    "default": {
        #one of "postgresql_psycopg2", "postgresql", "mysql", "sqlite3" or "oracle"
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": "dev.db",
        "USER": "",
        "PASSWORD": "",
        "HOST": "",
        "PORT": "",
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = "Europe/Amsterdam"

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = "en-us"

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = False

MEDIA_ROOT = None
MEDIA_URL = None

# Absolute path to the directory that holds static files like app media.
# Example: "/home/media/media.lawrence.com/apps/"
STATIC_ROOT = os.path.join(PROJECT_ROOT, "static")

# URL that handles the static files like app media.
# Example: "http://media.lawrence.com"
STATIC_URL = "/s/"

# Additional directories which hold static files
STATICFILES_DIRS = [
    STATIC_ROOT,
]

# Make this unique, and don't share it with anybody.
SECRET_KEY = "$&li378l3_8wform1%!hphxb3_#bqomk!302kplo)16j1tp)z#"

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = [
    "django.template.loaders.filesystem.load_template_source",
    "django.template.loaders.app_directories.load_template_source",
]

MIDDLEWARE_CLASSES = [
    "django.middleware.common.CommonMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

ROOT_URLCONF = "classify.urls"

TEMPLATE_DIRS = [
    os.path.join(PROJECT_ROOT, "templates"),
]

TEMPLATE_CONTEXT_PROCESSORS = [
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.request",
    "staticfiles.context_processors.static_url",
]

INSTALLED_APPS = [
    # Django
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.humanize",

    # "django.contrib.humanize",

    # external
    "staticfiles",
    "debug_toolbar",

    # project
    "classifier",
]

FIXTURE_DIRS = [
    os.path.join(PROJECT_ROOT, "fixtures"),
]

MESSAGE_STORAGE = "django.contrib.messages.storage.session.SessionStorage"

DEBUG_TOOLBAR_CONFIG = {
    "INTERCEPT_REDIRECTS": False,
}

# local_settings.py can be used to override environment-specific settings
# like database and email that differ between development and production.
try:
    from local_settings import *
except ImportError:
    pass
