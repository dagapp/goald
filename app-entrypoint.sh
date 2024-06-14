#!/bin/bash

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi


UWSGI_LOGPATH=/var/log/uwsgi.log
UWSGI_INI=/etc/uwsgi/apps-enabled/goald.ini

if [ $# -ne 0 ]
then

    uwsgi --ini "$UWSGI_INI" --daemonize "$UWSGI_LOGPATH"
    exec "$@"
else
    uwsgi --ini "$UWSGI_INI"
fi


