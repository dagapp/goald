#!/bin/bash

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

# nginx stuff
nginx

UWSGI_LOGPATH=/var/log/uwsgi.log
# uwsgi stuff
if [ $# -ne 0 ]
then
    uwsgi --ini "$PWD/goald_site/goald.ini" --daemonize "$UWSGI_LOGPATH"
    exec "$@"
else
    uwsgi --ini "$PWD/goald_site/goald.ini"
fi


