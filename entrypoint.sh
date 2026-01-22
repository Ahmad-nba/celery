#!/bin/sh
set -e

echo "run migrations"
python manage.py migrate --noinput

exec "$@"
