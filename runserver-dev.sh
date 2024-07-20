#!/bin/bash

export DJANGO_SETTINGS_MODULE=simple.locals
export ALLOWED_HOSTS=private.karuhun.online
export DATABASE_NAME=simple
export DATABASE_USER=simple
export DATABASE_PASSWORD=*Kcd64jnNJHCDf
export DATABASE_HOST=postgresql.infra.karuhun.online
export DATABASE_PORT=5432
export DATABASE_MONGODB_URI=mongodb://192.168.1.100:27017/simple
export MINIO_ACCESS_KEY=FIu33DxzmRXep2hDHXDV
export MINIO_SECRET_KEY=60zJIaw4L7WtggKdS6mDHhKZRnE4b3gBZ8odmBv4
export MINIO_BUCKET_NAME=simple-local
export MINIO_ENDPOINT=https://object.karuhun.online
export MAILJET_ACCESS_KEY=695a5c3a87db091d98f99ae9833b007f
export MAILJET_SECRET_KEY=bbafcf7988025e20e2330c1ee66c94ff
export MAILJET_DEFAULT_EMAIL=admin@mail.karuhun.online

python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --no-input
python manage.py runserver 127.0.0.1:34515
