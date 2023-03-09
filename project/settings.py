import os
from environs import Env
import dj_database_url


env = Env()
env.read_env()

DATABASES = {
    'default': dj_database_url.parse(env('DB_URL'))
}

INSTALLED_APPS = ['datacenter']

SECRET_KEY = env('SECRET_PASSWORD', 'DEFAULT_KEY')

DEBUG = env.bool('DJANGO_DEBUG', False)

ROOT_URLCONF = 'project.urls'

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', 'http://127.0.0.1:8000')


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
    },
]


USE_L10N = True

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'
