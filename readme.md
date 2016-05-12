# Oakland Web guide

## Introduction

  This a the web version of the Oakland Guide application.  The other parts of this application are a CMS ([github](https://github.com/CMP-Studio/cmoa-app-cms)) and iOS application ([github](https://github.com/CMP-Studio/cmoa-app-ios)).  It's purpose is to have a device non-specific way to view the content of the iOS application.

## Limitations

  Due to this being a website it will not have access to the iBeacon stack of the native iOS application and can therefore not give location-aware notifications.  Other than that it should be a very similar experience.

## Installing

  1. This is a [Django Framework](https://www.djangoproject.com/) application. start by installing Django 1.9.5 and it's requirements
  2. Install [Nginx](https://www.nginx.com/)
  3. Install [Postgres](http://www.postgresql.org/)
  4. Pull this repo to a location on the server you want to serve this application from.
  5. Install the other requirements by using `pip install -r requirements.txt` (you can also view requirements.txt to see what pythong packages it uses)
  6. Configure the application to your setup (see below)
  7. Copy the nginx file to the sites-avalible folder and link it to the sites-enabled (if you are using the default nginx site this file will need to be modified)
  8. Start up the gunicorn server using `sudo ./start.sh` and you should be running.

## Configuration

  There are several places that have configurations
  * guideapp/secrets.py - with the database configuration and a secret key for Django to use. This is ignored by git for obvious reasons so I've included an example @ secrets.example.py
  * guideapp/settings.py - API settings at the bottom point to locations dependent on the CMS location
  * nginx - nginx config file, make sure all filepaths in that file go to where you put this application
  * .sh scripts - both scripts have filepaths to the application
  * crontab - Use `crontab -e` to make update.sh run periodically to update from the CMS
