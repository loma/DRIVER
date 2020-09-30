#!/bin/bash

npm install
sed -i "s/52.53.243.250:8000/localhost:8080/g" src/environments/environment.ts
sed -i "s/54.215.143.19:8000/localhost:8080/g" src/environments/environment.ts
#./node_modules/@angular/cli/bin/ng serve --baseHref=/admin/ --host=0.0.0.0 --port=4200 --disableHostCheck=true --liveReload=false --optimization=true --watch=false
./node_modules/@angular/cli/bin/ng build --baseHref=/web-driver-admin/ --optimization=true --source-map=false
