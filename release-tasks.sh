#!/bin/sh

python manage.py migrate --no-input
python manage.py createsu
python manage.py collectstatic --no-input --clear
