"""
Django settings for sunday project.

Generated by 'django-admin startproject' using Django 4.2.10.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

import os
import logging
import sys
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-#bua605wsmrhmra^w*$kss!*mwb!%rru)i4gd9v39^2q8b8j#m'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	"rest_framework",
	"rest_framework.authtoken",
	"drf_yasg",
	"django_redis",
	"api",
	"users",
]

MIDDLEWARE = [
	'django.middleware.security.SecurityMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'sunday.urls'

TEMPLATES = [
	{
		"BACKEND": "django.template.backends.django.DjangoTemplates",
		"DIRS": [BASE_DIR / "templates"],
		'APP_DIRS': True,
		'OPTIONS': {
			'context_processors': [
				'django.template.context_processors.debug',
				'django.template.context_processors.request',
				'django.contrib.auth.context_processors.auth',
				'django.contrib.messages.context_processors.messages',
			],
		},
	},
]

WSGI_APPLICATION = 'sunday.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

if "test" in sys.argv:
	USER = os.environ.get("MYSQL_ROOT_USER")
	PASSWORD = os.environ.get("MYSQL_ROOT_PASSWORD")
else:
	USER = os.environ.get("MYSQL_USER")
	PASSWORD = os.environ.get("MYSQL_USER_PASSWORD")

DATABASES = {
	'default': {
		"ENGINE": "dj_db_conn_pool.backends.mysql",
		"NAME": os.environ.get("MYSQL_DATABASE"),
		"USER": USER,
		"PASSWORD": PASSWORD,
		"HOST": os.environ.get("MYSQL_HOST"),
		"POOL_OPTIONS": {
			"MAX_OVERFLOW": 10,
			"POOL_SIZE": 10,
			"RECYCLE": 24 * 60 * 60,
			"USE_THREADLOCAL": True,
		},
	}
}

CACHES = {
	"default": {
		"BACKEND": "django_redis.cache.RedisCache",
		"LOCATION": ["redis://rdCache:6379/1", ],
		"OPTIONS": {
			"CLIENT_CLASS": "django_redis.client.DefaultClient",
		},
	}
}

SESSION_ENGINE = 'django.contrib.sessions.backends.cache'
SESSION_CACHE_ALIAS = 'default'
# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
	{
		'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
	},
	{
		'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
	},
	{
		'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
	},
	{
		'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
	},
]

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
REST_FRAMEWORK = {
	"DATE_INPUT_FORMATS": ["%d-%m-%Y"],
	"DEFAULT_PAGINATION_CLASS": "api.utils.pagination.BasePagination",
	"PAGE_SIZE": 100,
	"DEFAULT_AUTHENTICATION_CLASSES": (
		"rest_framework.authentication.TokenAuthentication",
		"rest_framework.authentication.SessionAuthentication",
		"rest_framework.authentication.BasicAuthentication",
		"rest_framework_simplejwt.authentication.JWTAuthentication",
	)
}

SWAGGER_SETTINGS = {
	"USE_SESSION_AUTH": False,
	"SECURITY_DEFINITIONS": {
		"Bearer": {
			"type": "apiKey",
			"name": "Authorization",
			"in": "header"
		}
	}
}

LOGGING = {
	"version": 1,
	"disable_existing_loggers": False,
	"handlers": {
		"console": {
			"level": 'DEBUG',
			'class': 'logging.StreamHandler',
		},
		"file": {
			"level": "DEBUG",
			"class": "logging.FileHandler",
			"filename": 'logs/sunday.log',
		},
	},
	"loggers": {
		# "django": {
		# 	"handlers": ["console", "file"],
		# 	"level": "DEBUG",
		# 	"propagate": True,
		# },
		"django.request": {
			"handlers": ["console", "file"],
			"level": "DEBUG",
			"propagate": False,
		},
		"api": {
			"handlers": ["console", "file"],
			"level": "DEBUG",
			"propagate": False,
		},
		"users": {
			"handlers": ["console", "file"],
			"level": "DEBUG",
			"propagate": False,
		},
	},
}

# EMAIL_HOST = config('EMAIL_HOST', default='localhost')
# EMAIL_PORT = config('EMAIL_PORT', default=25, cast=int)
# EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD', default='')
# EMAIL_HOST_USER = config('EMAIL_HOST_USER', default='')
# EMAIL_USE_TLS = config('EMAIL_USE_TLS', default=False, cast=bool)
# DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
# SERVER_EMAIL = EMAIL_HOST_USER
# EMAIL_SUBJECT_PREFIX = 'bing'

AUTH_USER_MODEL = "users.User"
