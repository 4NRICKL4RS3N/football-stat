#!/usr/bin/env bash
# exit on error
chmod a+x build.sh
poetry add gunicorn

set -o errexit

poetry install

python manage.py collectstatic --no-input
python manage.py migrate