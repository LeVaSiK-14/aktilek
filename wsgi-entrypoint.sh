#!/bin/sh

until cd /app/
do 
    echo "waiting for server volume..."
done 

until ./manage.py migrate --noinput

do 
    echo "Waiting for db to be ready "
    sleep 2
done 


./manage.py collectstatic --noinput

gunicorn core.wsgi --bind 0.0.0.0:8001 --workers 4 --threads 4