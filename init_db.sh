#!/bin/sh
python manage.py migrate --noinput
gunicorn opencodereview.wsgi --workers 2
