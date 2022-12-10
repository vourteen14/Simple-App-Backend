FROM python:3.8

RUN mkdir /app
WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

RUN python manage.py makemigrations
RUN python manage.py migrate

EXPOSE 9090
CMD python manage.py runserver 0.0.0.0:9090
