FROM python:3

RUN apt-get update
RUN apt-get install -y binutils libproj-dev gdal-bin libgdal-dev

WORKDIR /usr/src/app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
