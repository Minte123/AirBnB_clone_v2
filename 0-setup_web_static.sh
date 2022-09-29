#!/usr/bin/env bash
#setup new server
# check for nginx installation, install if not installed
if ! nginx -v &>/dev/null ;
then
        apt-get -y update
        apt-get install -y nginx
fi

# create required folder and index file
#create /data folder
if [ ! -d /data/ ];
then
        mkdir /data
fi

#create subfolders
if [ ! -d /data/web_static/ ];
then
        mkdir -p /data/web_static/
fi

if [ ! -d /data/web_static/releases/ ];
then
        mkdir -p /data/web_static/releases/
fi
if [ ! -d /data/web_static/shared/ ];
then
        mkdir -p /data/web_static/shared/
fi
if [ ! -d /data/web_static/releases/test/ ]
then
        mkdir -p /data/web_static/releases/test/
fi
printf "
<html>
        <head>
        </head>
        <body>
                Holberton School
        </body>
</html>" >/data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu /data/
chgrp -R ubuntu /data/
# create nginx configuration
printf "server {
        listen   80 default_server;
        listen   [::]:80 default_server;
        root     /var/www/html;
        index    index.html index.htm;
        location /hbnb_static {
                alias /data/web_static/current;
                index index.html;
                }
        location /redirect_me {
                return 301 https://www.youtube.com;
        }
        error_page 404 /custom_404.html;
        location = /custom_404.html {
                root /var/www/errors/;
                internal;
        }
        location / {
                add_header X-Served-By %s;
        }

}" "$HOSTNAME"> /etc/nginx/sites-available/default
service nginx restart
