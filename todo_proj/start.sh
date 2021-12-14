#!/bin/bash
#this script will makemigrations & migrate & runserver
if [ $ON_SERVER ]; then
    python3 manage.py runserver 0.0.0.0:8000
else
    python3 manage.py makemigrations
    python3 manage.py migrate
    python3 manage.py runserver
fi