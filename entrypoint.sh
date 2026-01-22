#!/bin/sh

echo "run migrations"
python manage.py migrate

# the command to execute the commands passed in this entrypoint.sh
exec "$@"