#!/bin/bash

unset DATABASE_NAME
unset DATABASE_USER
unset DATABASE_PASSWORD
unset DATABASE_HOST
unset DATABASE_PORT
unset MINIO_ENDPOINT
unset MINIO_ACCESS_KEY
unset MINIO_SECRET_KEY
unset MINIO_MEDIA_BUCKET_NAME
unset MINIO_STATIC_BUCKET_NAME

export DEFAULT_FILE_STORAGE=minio_storage.storage.MinioMediaStorage
export MINIO_STORAGE_ENDPOINT="bucket_endpoint"
export MINIO_STORAGE_ACCESS_KEY="minio_access_key"
export MINIO_STORAGE_SECRET_KEY="minio_secret_key"

export DATABASE_NAME="database_name"
export DATABASE_USER="database_user"
export DATABASE_PASSWORD="database_password"
export DATABASE_HOST="database_host"
export DATABASE_PORT="database_port"

python manage.py runserver 192.168.1.100:34515