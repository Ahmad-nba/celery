FROM python:3.12-alpine

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN pip install --upgrade pip

# requirements is inside dcelery/, but context is repo root
COPY requirements.txt /usr/src/app/requirements.txt
RUN pip install -r /usr/src/app/requirements.txt


# copy the whole repo (manage.py, apps, dcelery module, etc.)
COPY . /usr/src/app

