#!/bin/bash

rm black_spots/migrations/0001_initial.py
rm data/migrations/0001_initial.py
rm driver_advanced_auth/migrations/0001_initial.py
rm user_filters/migrations/0001_initial.py

sed -i "s/'sslmode': 'require'/'sslmode': 'disable'/g" DRIVER/settings.py

python manage.py makemigrations
python manage.py migrate

python manage.py runserver 0.0.0.0:8000
