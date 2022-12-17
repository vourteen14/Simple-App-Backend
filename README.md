# Mengontil

ENV VAR POS GRE
- DB_USER
- DB_NAME
- DB_HOST
- DB_PORT
- DB_PASS

This APP run on port 9090 make sure no other service use that port or you can edit Dockerfile on 'EXPOSE' section

To access API it need to create new superuser and generate new rest token.

Use command below to create new superuser:

`python manage.py createsuperuser --username <username> --email <username>@domain.com`

Use command below to generate new rest token:

`python manage.py drf_create_token <username>`
