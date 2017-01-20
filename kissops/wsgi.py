"""
WSGI config for kissops project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "kissops.settings")
getEnvFromSystem = os.getenv('RUN_ENVIRONMENT', "default").lower().strip()

if getEnvFromSystem in "production":
    default_setting = "kissops.environments.production_settings"
elif getEnvFromSystem in "test":
    default_setting = "kissops.environments.test_settings"
elif getEnvFromSystem in "development":
    default_setting = "kissops.environments.development_settings"
elif getEnvFromSystem in "local":
    default_setting = "kissops.environments.local_settings"
else:
    default_setting = "kissops.settings"

os.environ.setdefault("DJANGO_SETTINGS_MODULE", default_setting)

application = get_wsgi_application()
