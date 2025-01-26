# WLLR Rostering Website
A django website for rostering at WLLR.

Django tutorial: https://docs.djangoproject.com/en/5.1/intro/tutorial04/

## Run locally

### Install Postgres locally, create database, create app user and apply migrations 

#### Install Postgres Linux Ubuntu

Install: `sudo apt install postgresql postgresql-contrib libpq-dev`
Run server: `sudo service postgresql start`
Check if server running: `sudo systemctl status postgresql`

#### Create database and user

Access command line tool psql: `sudo -u postgres psql` (quit: `\q`)
Create database: `CREATE DATABASE wllr_rostering;`
Create user: `CREATE USER django_app WITH ENCRYPTED PASSWORD 'password';`
Grant user permissions on database: `GRANT ALL PRIVILEGES ON DATABASE wllr_rostering TO django_app;`

#### Create and run migrations

Create migrations: `python WLLRRosteringDjangoWebsite/manage.py makemigrations`
Run migrations: `python WLLRRosteringDjangoWebsite/manage.py migrate`

Squash migrations: `python WLLRRosteringDjangoWebsite/manage.py squashmigrations <app> <max_migration_file_number>`
E.g.: `python WLLRRosteringDjangoWebsite/manage.py squashmigrations get_availability 0003`

#### Once database exists

Once database already created, login to database directly as superuser: `sudo -u postgres psql wllr_rostering`

### Run Django app

Create superuser: `python WLLRRosteringDjangoWebsite/manage.py createsuperuser`

Run server: `python WLLRRosteringDjangoWebsite/manage.py runserver`
