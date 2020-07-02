#!/bin/bash

npm install
./node_modules/@angular/cli/bin/ng serve --baseHref=/admin/ --host=0.0.0.0 --port=4200 --disableHostCheck=true --liveReload=false --optimization=true --watch=false
