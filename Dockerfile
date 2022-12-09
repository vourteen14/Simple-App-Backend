FROM python:3.8

RUN mkdir /app
WORKDIR /app

ENV DB_USER hqanbcui
ENV DB_NAME hqanbcui
ENV DB_HOST mouse.db.elephantsql.com
ENV DB_PORT 5432
ENV DB_PASS N2mzLkXM8m73sueyeoYSqlk0aEh_MqBN

COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

RUN python manage.py makemigrations
RUN python manage.py migrate

EXPOSE 9090
CMD python manage.py runserver 0.0.0.0:9090
