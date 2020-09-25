release: python manage.py migrate --no-input && python manage.py createsu
web: gunicorn voting.wsgi:application --log-file -
