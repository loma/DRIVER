FROM php:7.3.11-fpm

RUN apt-get update
RUN apt-get install -y libfreetype6-dev libjpeg62-turbo-dev \
      libmcrypt-dev default-mysql-client libmagickwand-dev \
      gnupg2 libzip-dev \
      memcached libmemcached-dev \
      libgif7 libpng-dev --no-install-recommends \
      libxpm4 libxrender1 libgtk2.0-0 libnss3 libgconf-2-4 \
      xvfb gtk2-engines-pixbuf \ 
      xfonts-cyrillic xfonts-100dpi xfonts-75dpi xfonts-base xfonts-scalable \
      imagemagick x11-apps 

RUN pecl install imagick mcrypt-1.0.1 memcached pcov
RUN docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/
RUN docker-php-ext-install pdo_mysql mbstring zip gd opcache

RUN usermod -u 33 www-data

COPY docker-php-ext-upload-size.ini /usr/local/etc/php/conf.d/docker-php-ext-upload-size.ini
COPY docker-php-ext-session.ini /usr/local/etc/php/conf.d/docker-php-ext-session.ini
COPY docker-php-ext-opcache.ini /usr/local/etc/php/conf.d/docker-php-ext-opcache.ini

RUN docker-php-ext-enable imagick memcached opcache pcov

RUN apt-get install -y fonts-liberation libappindicator3-1 \
          libasound2 libatk-bridge2.0-0 libatspi2.0-0 libgbm1 \
          libgtk-3-0 libxss1 libxtst6 wget xdg-utils

COPY google-chrome-stable_current_amd64.deb /tmp/google-chrome-stable_current_amd64.deb
RUN dpkg -i /tmp/google-chrome-stable_current_amd64.deb
