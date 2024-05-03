#!/bin/bash

if ! [ -f /goald/db.sqlite3 ]; then
    cd /goald || (echo "/goald dir was not found!"; exit)
    echo "DB not found! Creating a new one!"
    python3 manage.py makemigrations
    python3 manage.py migrate
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


