#!/bin/sh
python manage.py makemigrations authentication
python manage.py makemigrations --no-input
python manage.py migrate --no-input
python manage.py collectstatic --no-input

# running with guicorn
gunicorn djdocker.wsgi:application --bind 0.0.0.0:8000
