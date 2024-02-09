#!/bin/bash

unset DB_NAME
unset DB_USER
unset DB_PASSWORD
unset DB_HOST
unset DB_PORT

export DB_NAME="database_name"
export DB_USER="database_user"
export DB_PASSWORD="database_password"
export DB_HOST="database_host"
export DB_PORT="database_port"

python manage.py runserver 10.1.0.10:34515