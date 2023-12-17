#!/bin/bash

PROJECT_DIR=$PWD

echo "+--------------------------------------------------------+"
echo "  Project dir: $PROJECT_DIR                               "
echo "+--------------------------------------------------------+"


sudo apt update
sudo apt upgrade

sudo apt install nginx python3-venv python3-dev uwsgi uwsgi-plugin-python3

echo
echo "+--------------------------------------------------------+"
echo "Activating virtual environment"
echo "+--------------------------------------------------------+"
echo

virtualenv .
source bin/activate

echo
echo "+--------------------------------------------------------+"
echo "Installing django"
echo "+--------------------------------------------------------+"
echo

pip3 install django bcrypt Pillow

python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py collectstatic

sudo mkdir -p /var/www/goald_deployment
sudo ln -s $PROJECT_DIR /var/www/goald_deployment
sudo ln -s $PROJECT_DIR/goald_site/nginx.conf /etc/nginx/sites-enabled/goald_nginx.conf

echo
echo "+--------------------------------------------------------+"
echo "Starting uwsgi"
echo "+--------------------------------------------------------+"
echo
# uwsgi stuff
uwsgi --ini $PROJECT_DIR/goald_site/goald.ini &

echo
echo "+--------------------------------------------------------+"
echo "Starting nginx"
echo "+--------------------------------------------------------+"
echo
# nginx stuff
sudo /etc/init.d/nginx restart # restart because it restarts server if it works or just starts server if it stopped
