import dj_database_url
import os
from path import path

PROJECT_ROOT = path(__file__).abspath().dirname().dirname().dirname()
os.sys.path.append(PROJECT_ROOT)
os.sys.path.append(PROJECT_ROOT / 'app')
os.sys.path.append(PROJECT_ROOT / 'tests')


def is_true(value):
    if value:
        return value.lower() == "true"
    return False

DEBUG = is_true(os.environ.get('DEBUG'))


ALLOWED_HOSTS = []
MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
)

TIME_ZONE = 'America/New_York'
USE_TZ = True
LANGUAGE_CODE = 'en-us'

DATABASES = {
    'default': dj_database_url.parse(os.environ.get('DATABASE_URL')),
}

INSTALLED_APPS = [
    # Local apps.
    'example',
]

ROOT_URLCONF = 'app.config.urls'

# Environment variables
# Classic Django secret key
SECRET_KEY = os.environ.get('SECRET_KEY')
