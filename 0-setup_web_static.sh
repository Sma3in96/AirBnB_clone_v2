#!/usr/bin/env bash
# setup a web server

sudo apt-get update
sudo apt-get install nginx -y

mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/

sudo echo "its working" > /data/web_static/releases/test/index.html

sudo ln -fs /data/web_static/releases/test/ /data/web_static/current

sudo chown -R ubuntu:ubuntu /data/

sudo sed -i '39 i\ \tlocation /hbnb_static {\n\t\talias /data/web_static/current;\n\t}\n' /etc/nginx/sites-enabled/default

sudo service nginx restart
