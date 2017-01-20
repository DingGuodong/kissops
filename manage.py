#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
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
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
