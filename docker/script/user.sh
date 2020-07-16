#!/bin/bash

npm install
sed -i "s/54.193.25.161:8000/localhost/g" src/app/config.js
./node_modules/@angular/cli/bin/ng serve --baseHref=/user/ --host=0.0.0.0 --port=4300 --disableHostCheck=true --liveReload=false --optimization=true --watch=false --verbose=true --progress=true
