FROM postgres

RUN apt-get update
RUN apt-get install -y postgresql-12-postgis-3

