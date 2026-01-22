FROM python:3.12-alpine

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN pip install --upgrade pip

# requirements is inside dcelery/, but context is repo root
COPY dcelery/requirements.txt /usr/src/app/requirements.txt
RUN pip install -r /usr/src/app/requirements.txt

# entrypoint is in repo root (per your screenshot)
COPY entrypoint.sh /usr/src/app/entrypoint.sh
RUN chmod +x /usr/src/app/entrypoint.sh \
    && sed -i 's/\r$//' /usr/src/app/entrypoint.sh

# copy the whole repo (manage.py, apps, dcelery module, etc.)
COPY . /usr/src/app

ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
