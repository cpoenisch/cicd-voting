#!/bin/sh

if [ "$USE_POSTGRES" = "1" ]; then
  echo "Waiting for postgres..."
  while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do
    sleep 1.0
  done
  echo "PostgreSQL started"
fi

python manage.py flush --no-input
python manage.py migrate --no-input
python manage.py createsu
python manage.py collectstatic --no-input --clear

exec "$@"
