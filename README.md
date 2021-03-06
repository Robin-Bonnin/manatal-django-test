# manatal-django-test
 
## Pre-requisites 
- Python installed
- PostgreSQL server installed
- pipenv installed

## Installation
1. In the main folder, run `pipenv shell`
1. Go to the ***school_backend/school_backend*** folder and add a .env file with details as below
1. Go to the ***school_backend*** folder
1. Run `python manage.py makemigrations school_backend`
1. Run `python manage.py migrate`
1. Run `python manage.py runserver`
1. Open the browser at `127.0.0.1:8000/`
1. Browse through the api

## Time spent 
- Django & Django Rest Framework documentation reading : 1h
- Setup installation : 1h (issues with previous POSTGRESQL installations) 
- Part 1 : 30min
- Part 2 : 30min
- Part 3 : 1h
- Refinement : 10min

## .env file requirements
Example of the .env file
`SECRET_KEY= secret_key
DATABASE_NAME=school_backend
DATABASE_USER=postgres
DATABASE_PASSWORD=admin
DATABASE_HOST=localhost
DATABASE_PORT=5432`
