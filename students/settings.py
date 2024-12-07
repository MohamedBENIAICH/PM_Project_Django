# settings.py
from pathlib import Path

import MIDDLEWARE

BASE_DIR = Path(__file__).resolve().parent.parent

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
ALLOWED_HOSTS = ['*']


INSTALLED_APPS = [
    # other apps...
    'rest_framework',
]

MIDDLEWARE += [
    'django.middleware.common.CommonMiddleware',
]