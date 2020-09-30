#!/bin/bash

rm black_spots/migrations/0001_initial.py
rm data/migrations/0001_initial.py
rm driver_advanced_auth/migrations/0001_initial.py
rm user_filters/migrations/0001_initial.py

sed -i "s/'sslmode': 'require'/'sslmode': 'disable'/g" DRIVER/settings.py
sed -i "s/redis==3.4.1/redis==2.10.6/g" requirements.txt

cp /usr/src/app/script/views.py /usr/local/lib/python3.8/site-packages/grout/views.py
cp /usr/src/app/script/filters.py /usr/local/lib/python3.8/site-packages/grout/filters.py

pip install --no-cache-dir -r requirements.txt

python manage.py makemigrations
python manage.py migrate

python manage.py runserver 0.0.0.0:8000
