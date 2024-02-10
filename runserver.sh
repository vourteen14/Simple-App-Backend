#!/bin/bash

unset DB_NAME
unset DB_USER
unset DB_PASSWORD
unset DB_HOST
unset DB_PORT
unset MINIO_STORAGE_ENDPOINT
unset MINIO_STORAGE_ACCESS_KEY
unset MINIO_STORAGE_SECRET_KEY
unset MINIO_STORAGE_MEDIA_BUCKET_NAME
unset MINIO_STORAGE_STATIC_BUCKET_NAME

export DEFAULT_FILE_STORAGE=minio_storage.storage.MinioMediaStorage
export MINIO_STORAGE_ENDPOINT="bucket_endpoint"
export MINIO_STORAGE_ACCESS_KEY="minio_access_key"
export MINIO_STORAGE_SECRET_KEY="minio_secret_key"
export MINIO_STORAGE_MEDIA_BUCKET_NAME="media_bucket"
export MINIO_STORAGE_STATIC_BUCKET_NAME="static_bucket"

export DB_NAME="database_name"
export DB_USER="database_user"
export DB_PASSWORD="database_password"
export DB_HOST="database_host"
export DB_PORT="database_port"

python manage.py runserver 10.1.0.10:34515