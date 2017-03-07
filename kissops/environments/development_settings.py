"""
Django  development environment(short form 'dev') settings for kissops project.

Generated by 'django-admin startproject' using Django 1.9.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TOP_DIR = os.path.dirname(BASE_DIR)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'b%f&_#_jr9#@4$_)%xla-1u4o#p_p*oqq19!_(uw7b5n5&gqp('

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG_SETTING = os.getenv('ENABLE_DEBUG', 'True').lower().strip()
if DEBUG_SETTING in "true|yes|on|1|enable":
    DEBUG = True
elif DEBUG_SETTING in "false|no|off|0|disable":
    DEBUG = False
else:
    DEBUG = False

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(asctime)s %(module)s %(message)s'
        },
    },
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': '/var/log/kissops_debug.log',
            'formatter': 'simple'
        },
        'console': {
            'class': 'logging.StreamHandler',
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'include_html': True,
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': False,
        },
    },
}

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'kissops.apps.KissOpsConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'itoms',
    'login',
    'inventory.host',
    'inventory.project',
    'inventory.datacenter',
    'inventory.device',
    'inventory.machine',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'kissops.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(TOP_DIR, 'templates')],
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

WSGI_APPLICATION = 'kissops.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases
# https://docs.djangoproject.com/en/1.10/topics/db/multi-db/

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(TOP_DIR, 'db.sqlite3'),
    },
    'itoms_db': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.getenv('MYSQL_DATABASE_NAME', 'devdb'),
        'USER': os.getenv('MYSQL_DATABASE_USER', 'dev'),
        'PASSWORD': os.getenv('MYSQL_DATABASE_PASSWORD', 'dEvp@ssw0rd'),
        'HOST': os.getenv('MYSQL_DATABASE_HOST', '127.0.0.1'),
        'PORT': os.getenv('MYSQL_DATABASE_PORT', '3306'),
        'CONN_MAX_AGE': None
    },

}

# Using routers
# https://docs.djangoproject.com/en/1.10/topics/db/multi-db/#topics-db-multi-db-routing

DATABASE_ROUTERS = [
    'kissops.database_routers.ItomsRouter',
]

DATABASE_APPS_MAPPING = {
    # example:
    # 'app_name':'database_name',
    'itoms': 'itoms_db',
}

# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'

local_static_root = ''
remote_static_root = '/home/docker/volatile/static'

FAVICON_PATH = os.path.join(STATIC_URL, 'images/favicon.ico')

# https://docs.djangoproject.com/en/1.10/howto/static-files/#deployment
# $ python manage.py collectstatic
STATIC_ROOT = remote_static_root

STATICFILES_DIRS = [
    os.path.join(TOP_DIR, 'static'),
]

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_USE_TLS = False
EMAIL_USE_SSL = False
EMAIL_HOST = 'smtp.exmail.qq.com'
EMAIL_PORT = 25
EMAIL_HOST_USER = 'noreply@example.com'
EMAIL_HOST_PASSWORD = 'password here'
EMAIL_TIMEOUT = 3
DEFAULT_FROM_EMAIL = 'noreply <noreply@example.com>'
ADMINS = [('Guodong Ding', 'dinggd@example.com'), ]
