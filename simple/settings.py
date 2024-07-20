from pathlib import Path
from datetime import timedelta
import os

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = 'django-insecure-q=dn3pt1lkp*^!fkntp)@@#a07#b_+dr__rg8fb^2uvvit185_'
DEBUG = True
HOSTS = os.getenv('ALLOWED_HOSTS', '')
ALLOWED_HOSTS = HOSTS.split(',') if HOSTS else []
INSTALLED_APPS = [
  'django.contrib.admin',
  'django.contrib.auth',
  'django.contrib.contenttypes',
  'django.contrib.sessions',
  'django.contrib.messages',
  'django.contrib.staticfiles',
  'rest_framework',
  'django_rename_app',
  'django_mailjet',
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

CSRF_TRUSTED_ORIGINS = [f"https://{host}" for host in ALLOWED_HOSTS]

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
    'NAME': os.getenv('DATABASE_NAME'),
    'USER': os.getenv('DATABASE_USER'),
    'PASSWORD': os.getenv('DATABASE_PASSWORD'),
    'HOST': os.getenv('DATABASE_HOST'),
    'PORT': os.getenv('DATABASE_PORT'),
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

MAILJET_API_KEY = os.getenv('MAILJET_ACCESS_KEY')
MAILJET_API_SECRET = os.getenv('MAILJET_SECRET_KEY')
EMAIL_BACKEND = 'django_mailjet.backends.MailjetBackend'
DEFAULT_FROM_EMAIL = os.getenv('MAILJET_DEFAULT_EMAIL')

AWS_ACCESS_KEY_ID = os.getenv('MINIO_ACCESS_KEY')
AWS_SECRET_ACCESS_KEY = os.getenv('MINIO_SECRET_KEY')
AWS_STORAGE_BUCKET_NAME = os.getenv('MINIO_BUCKET_NAME')
AWS_S3_ENDPOINT_URL = os.getenv('MINIO_ENDPOINT')
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

MONGO_URI = os.getenv('DATABASE_MONGODB_URI')

SIMPLE_JWT = {
  'ACCESS_TOKEN_LIFETIME': timedelta(days=7),
  'REFRESH_TOKEN_LIFETIME': timedelta(days=30),
}