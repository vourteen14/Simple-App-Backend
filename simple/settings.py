from pathlib import Path
from datetime import timedelta
import os

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = 'django-insecure-q=dn3pt1lkp*^!fkntp)@@#a07#b_+dr__rg8fb^2uvvit185_'
DEBUG = True
HOSTS = os.environ.get('ALLOWED_HOSTS', '')
ALLOWED_HOSTS = HOSTS.split(',') if HOSTS else []
INSTALLED_APPS = [
  'django.contrib.admin',
  'django.contrib.auth',
  'django.contrib.contenttypes',
  'django.contrib.sessions',
  'django.contrib.messages',
  'django.contrib.staticfiles',
  'rest_framework',
  'simple_user',
  'simple_catalog',
  'simple_todo',
  'simple_note',
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
    'NAME': os.environ.get('DATABASE_NAME'),
    'USER': os.environ.get('DATABASE_USER'),
    'PASSWORD': os.environ.get('DATABASE_PASSWORD'),
    'HOST': os.environ.get('DATABASE_HOST'),
    'PORT': os.environ.get('DATABASE_PORT'),
  }
}

REST_FRAMEWORK = {
  'DEFAULT_AUTHENTICATION_CLASSES': [
    'rest_framework_simplejwt.authentication.JWTAuthentication',
  ],
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

AWS_ACCESS_KEY_ID = os.environ.get('MINIO_ACCESS_KEY')
AWS_SECRET_ACCESS_KEY = os.environ.get('MINIO_SECRET_KEY')
AWS_STORAGE_BUCKET_NAME = os.environ.get('MINIO_BUCKET_NAME')
AWS_S3_ENDPOINT_URL = os.environ.get('MINIO_ENDPOINT')
AWS_S3_SECURE_URLS = False

STATIC_URL = f"{AWS_S3_ENDPOINT_URL}/{AWS_STORAGE_BUCKET_NAME}/static/"
MEDIA_URL = f"{AWS_S3_ENDPOINT_URL}/{AWS_STORAGE_BUCKET_NAME}/media/"
STATICFILES_DIRS = [ os.path.join(BASE_DIR, 'simple_static'), ]

STATICFILES_STORAGE = 'simple.storages.MinioStorageStatic'
DEFAULT_FILE_STORAGE = 'simple.storages.MinioStorageMedia'

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Jakarta'
USE_I18N = True
USE_L10N = True
USE_TZ = True
STATIC_URL = '/static/'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MONGO_URI = os.environ.get('DATABASE_MONGODB_URI')

SIMPLE_JWT = {
  'ACCESS_TOKEN_LIFETIME': timedelta(days=7),
  'REFRESH_TOKEN_LIFETIME': timedelta(days=30),
}