# DRIVER v2
This is a docker template for bootstraping a dev environment for DRIVER v2.

## Prepare Source Code
Cloning the source codes into respect folders `backend, admin, user`

    git clone BACKEND_SOURCE_CODE backend
    git clone ADMIN_SOURCE_CODE admin
    git clone USER_SOURCE_CODE user

## Starting Up
Start up all servers

    cd docker
    docker-compose up
**Build particular images**

    docker-compose build backend
**Build particular images (force)**

    docker-compose build --no-cache backend
**URL**

 - http://localhost:8000 -> API
 - http://localhost:4200 -> Admin (Ashalar Editor)
 - http://localhost:4300 -> User

## Config Backend (API)
  ### DRIVER/settings.py

    REDIS_HOST = os.environ.get('DRIVER_REDIS_HOST', 'redis')
    DATABASES = {
	    ...
	    'default': {
		    'HOST': os.environ.get('DRIVER_DB_HOST', 'postgres'),
		    'NAME': os.environ.get('DRIVER_DB_NAME', 'postgres'),
		},
		'OPTIONS': { 'sslmode': 'disable' }
	}

### Migrations
Due to some errors when execute `python manage.py migrate`  class **DriverRecord** and **DriverRecordCopy** need to temporary extends from **models.Model** under the data/models.py

    ...
    class DriverRecord(models.Model):
    class DriverRecordCopy(models.Model):
    ...

   Then run the migration to partially initialse the database

    cd docker
    docker-compose exec backend bash -c "python manage.py migrate"

### Insert to Postgres

    cd docker
    docker-compose exec postgres bash -c "psql postgres postgres"
    insert into auth_group (name) values ('Superadmin');
    insert into auth_group (name) values ('Public');

### Create a super user

    cd docker
    docker-compose exec backend bash -c "python manage.py createsuperuser"


## Web Admin (Ashlar Editor)

  ### package.json
  The docker file will use `npm start` to start the local dev server.

    "scripts": {
	    ...
	    "start": "ng serve --host=0.0.0.0 --port=4200",
	}

### src/environments/environment.ts

    API_BASE: 'http://localhost:8000/'

## User


  ### package.json
  The docker file will use `npm start` to start the local dev server.


    "scripts": {
	    ...
	    "start": "ng serve --host=0.0.0.0 --port=4300",
	}
### src/environments/environment.ts

    API_BASE: 'http://localhost:8000/'

## Todos

 - fixed postgres schema, missing migration script
 - seed data for testing/demo
 - production deployment config
