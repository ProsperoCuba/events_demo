"""
Development settings
"""

from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]

# Application definition

INSTALLED_APPS = INSTALLED_APPS + ["django_extensions"]

AUTH_PASSWORD_VALIDATORS = []

INTERNAL_IPS = ["127.0.0.1"]

if DEBUG:
    CORS_ALLOW_ALL_ORIGINS = True

if DOMAIN:
    CORS_ALLOWED_ORIGINS = [
        f"http://{DOMAIN}",
        f"https://{DOMAIN}",
        f"https://www.{DOMAIN}",
    ]
