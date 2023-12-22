#!/bin/bash

PROJECT_DIR=$PWD

echo "+--------------------------------------------------------+"
echo "  Project dir: $PROJECT_DIR                               "
echo "+--------------------------------------------------------+"


sudo apt update
sudo apt upgrade

sudo apt install nginx python3-virtualenv python3-dev uwsgi uwsgi-plugin-python3

echo
echo "+--------------------------------------------------------+"
echo "Activating virtual environment"
echo "+--------------------------------------------------------+"
echo

virtualenv "$PROJECT_DIR"
source "$PROJECT_DIR/bin/activate"

echo
echo "+--------------------------------------------------------+"
echo "Installing django"
echo "+--------------------------------------------------------+"
echo

pip3 install django bcrypt Pillow

python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py collectstatic

sudo mkdir -p /var/www/goald
sudo rm /var/www/goald/*
sudo ln -s "$PROJECT_DIR" /var/www/goald
sudo rm /etc/nginx/sites-enabled/goald_nginx.conf
sudo ln -s "$PROJECT_DIR/goald_site/nginx.conf" /etc/nginx/sites-enabled/goald_nginx.conf

echo
echo "+--------------------------------------------------------+"
echo "Starting uwsgi"
echo "+--------------------------------------------------------+"
echo
# uwsgi stuff
sudo rm /etc/uwsgi/apps-enabled/goald.ini
sudo ln -s "$PROJECT_DIR/goald_site/goald.ini" /etc/uwsgi/apps-enabled/
sudo service uwsgi restart # restart because it restarts uwsgi if it works or just starts uwsgi if it stopped

echo
echo "+--------------------------------------------------------+"
echo "Starting nginx"
echo "+--------------------------------------------------------+"
echo
# nginx stuff
sudo service nginx restart # restart because it restarts server if it works or just starts server if it stopped
