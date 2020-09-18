#!/bin/bash

npm install
sed -i "s/52.53.243.250:8000/localhost/g" src/app/config.js
sed -i "s/52.53.243.250:8000/localhost/g" src/environments/environment.ts
#./node_modules/@angular/cli/bin/ng serve --baseHref=/user/ --host=0.0.0.0 --port=4300 --disableHostCheck=true --liveReload=false --optimization=true --watch=false --verbose=true --progress=true
node --max_old_space_size=8192 ./node_modules/@angular/cli/bin/ng build --baseHref=/wb-driver/

