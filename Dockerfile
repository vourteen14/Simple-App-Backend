FROM arm64v8/python:3.10-slim-bullseye

RUN mkdir /app
WORKDIR /app

RUN apt-get update && apt-get install -y build-essential libpq-dev && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app

RUN pip install --upgrade pip
RUN pip install --disable-pip-version-check --root-user-action=ignore -r requirements.txt

COPY . /app

EXPOSE 9090
CMD ["python3", "manage.py", "runserver", "0.0.0.0:9090"]
