#!/bin/bash

npm install
sed -i "s/54.193.25.161:8000/localhost:8080/g" src/app/config.js
sed -i "s/54.193.25.161:8000/localhost:8080/g" src/environments/environment.ts

sed -i "s/54.215.143.19:8000/localhost:8080/g" src/app/config.js
sed -i "s/54.215.143.19:8000/localhost:8080/g" src/environments/environment.ts

node --max_old_space_size=8192 ./node_modules/@angular/cli/bin/ng build --baseHref=/WB-Driver/ --source-map=false

