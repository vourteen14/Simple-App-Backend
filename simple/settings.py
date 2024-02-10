from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = 'django-insecure-q=dn3pt1lkp*^!fkntp)@@#a07#b_+dr__rg8fb^2uvvit185_'
DEBUG = True
ALLOWED_HOSTS = ['10.1.0.10']
INSTALLED_APPS = [
  'django.contrib.admin',
  'django.contrib.auth',
  'django.contrib.contenttypes',
  'django.contrib.sessions',
  'django.contrib.messages',
  'django.contrib.staticfiles',
  'simple_user',
  'simple_catalog',
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

ROOT_URLCONF = 'simple.urls'

TEMPLATES = [
  {
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [],
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

WSGI_APPLICATION = 'simple.wsgi.application'

DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.postgresql',
    'NAME': os.environ.get('DB_NAME'),
    'USER': os.environ.get('DB_USER'),
    'PASSWORD': os.environ.get('DB_PASSWORD'),
    'HOST': os.environ.get('DB_HOST'),
    'PORT': os.environ.get('DB_PORT'),
  }
}

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

AUTH_USER_MODEL = 'simple_user.CustomUser'

DEFAULT_FILE_STORAGE = os.environ.get('DEFAULT_FILE_STORAGE')
MINIO_STORAGE_ENDPOINT = os.environ.get('MINIO_STORAGE_ENDPOINT')
MINIO_STORAGE_ACCESS_KEY = os.environ.get('MINIO_STORAGE_ACCESS_KEY')
MINIO_STORAGE_SECRET_KEY = os.environ.get('MINIO_STORAGE_SECRET_KEY')
MINIO_STORAGE_MEDIA_BUCKET_NAME = os.environ.get('MINIO_STORAGE_MEDIA_BUCKET_NAME')
MINIO_STORAGE_STATIC_BUCKET_NAME = os.environ.get('MINIO_STORAGE_STATIC_BUCKET_NAME')

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True
STATIC_URL = '/static/'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'