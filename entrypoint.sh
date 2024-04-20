#!/bin/bash

if ! [ -f /goald/db.sqlite3 ]; then
    cd /goald || (echo "/goald dir was not found!"; exit)
    echo "DB not found! Creating a new one!"
    python3 manage.py makemigrations
    python3 manage.py migrate
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


