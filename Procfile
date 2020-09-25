release: python manage.py migrate --no-input && python manage.py migrate --no-input && python manage.py collectstatic --no-input --clear
web: gunicorn voting.wsgi:application --log-file -
