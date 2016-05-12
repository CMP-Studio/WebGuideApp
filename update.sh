#!/bin/bash

PROJECT_PATH=/var/www/guideapp/

echo "Starting update"

cd $PROJECT_PATH
exec python manage.py update_all

echo "Data updated!"
