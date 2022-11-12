# pull official base image
FROM python:3.9-alpine

# set work directory
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DEBUG 0

# install psycopg2
RUN apk update \
    && apk add --virtual build-essential gcc python3-dev musl-dev \
    && apk add postgresql-dev \
    && pip install psycopg2

# install dependencies
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .

# collect static files
RUN python manage.py collectstatic --noinput

RUN python manage.py migrate

# # add and run as non-root user
# RUN adduser -D myuser
# USER myuser

# run gunicorn
CMD gunicorn galleria.wsgi:application --bind 0.0.0.0:8080

EXPOSE 8080






# # For more information, please refer to https://aka.ms/vscode-docker-python
# FROM python:3.9-slim
#
# ENV VAR1=10
#
# # Keeps Python from generating .pyc files in the container
# ENV PYTHONDONTWRITEBYTECODE=1
#
# # Turns off buffering for easier container logging
# ENV PYTHONUNBUFFERED=1
#
# # Install & use pipenv
# COPY Pipfile Pipfile.lock ./
# RUN python -m pip install --upgrade pip
# RUN pip install pipenv && pipenv install --dev --system --deploy
#
# WORKDIR /app
# COPY . /app
#
#
#
#
# # ARG PYTHON_VERSION=3.9
# #
# # FROM python:${PYTHON_VERSION}
# #
# # RUN apt-get update && apt-get install -y \
# #     python3-pip
# #     # python3-venv \
# #     # python3-dev \
# #     # python3-setuptools \
# #     # python3-wheel
# #
# # RUN python3 -m pip install --user pipenv
# #
# # RUN mkdir -p /app
# # WORKDIR /app
# #
# # COPY Pipfile Pipfile.lock .
# # # https://stackoverflow.com/questions/46503947/how-to-get-pipenv-running-in-docker
# #
# # RUN python -m pip install --upgrade pip
# # RUN pip install pipenv && pipenv install --dev --system --deploy
# # # RUN pip install pipenv && pipenv install --dev --system --deploy --ignore-pipfile
# #
# # COPY . .
#
# RUN python manage.py collectstatic --noinput
#
# EXPOSE 8080
#
# CMD ["gunicorn", "--bind", ":8080", "--workers", "2", "galleria.wsgi"]
