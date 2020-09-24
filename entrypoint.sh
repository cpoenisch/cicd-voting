#!/bin/sh

echo "Waiting for postgres..."
while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do
  sleep 1.0
done
echo "PostgreSQL started"

python manage.py flush --no-input
python manage.py migrate --noinput
python manage.py createsu
python manage.py collectstatic --no-input --clear

exec "$@"
