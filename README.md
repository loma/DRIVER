# DRIVER v2
This is a docker template for bootstraping a dev environment for DRIVER v2.

## Prepare Source Code
Cloning the source codes into respect folders `backend, admin, user`

    git clone BACKEND_SOURCE_CODE backend
    git clone ADMIN_SOURCE_CODE admin
    git clone USER_SOURCE_CODE user

## Backend (API)
#### Pull the latest changes

    cd backend
    git fetch origin
    git reset --hard origin/master

#### Up postgres

    cd docker
    docker-compose up -d postgres

#### Init database (only run once, this will clear all tables)

    cd docker
    docker-compose exec postgres bash -c "./script/postgres.sh"

#### Up backend to migrate schema
Update any config changes in *docker/script/backend.sh*

    cd docker
    docker-compose up -d backend

#### Create superadmin

    cd docker
    docker-compose exec backend bash -c "python manage.py createsuperuser"

#### Seed database with first records setting

    cd docker
    docker-compose exec postgres bash -c "./script/copyfirst_record_to_db.sh"


## Web Admin (Ashlar Editor)
#### Pull the latest changes

    cd admin
    git fetch origin
    git reset --hard origin/master

#### Up admin, (this will build angular admin and put under docker/dist/wb-driver-admin)
Update config api url in *script/admin.sh* before build the admin

    cd docker
    docker-compose up admin


## User
#### Pull the latest changes

    cd user
    git fetch origin
    git reset --hard origin/master

#### Up user, (this will build angular user and put under docker/dist/WB-Driver)
Update config api url in *script/user.sh* before build the user

    cd docker
    docker-compose up user

## Nginx
#### Up nginx to serve admin/user site

    docker-compose up -d nginx

- http://localhost:8000 -> API driect to django api
- http://localhost:8080 -> API via nginx
- http://localhost:8080/wb-admin-driver -> Admin
- http://localhost:8080/web-driver -> User
