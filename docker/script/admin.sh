#!/bin/bash

npm install
sed -i "s/13.52.193.94:8000/localhost/g" src/environments/environment.ts
./node_modules/@angular/cli/bin/ng serve --baseHref=/admin/ --host=0.0.0.0 --port=4200 --disableHostCheck=true --liveReload=false --optimization=true --watch=false
