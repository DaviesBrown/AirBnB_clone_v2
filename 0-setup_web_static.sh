#!/usr/bin/env bash
# Bash script that sets up your web servers for the deployment of web_static
sudo apt-get update -y
sudo apt-get install nginx -y
mkdir -p /data/web_static/releases/test/
echo "hello world" > /data/web_static/realeases/test/index.html
mkdir -p /data/web_static/shared/
ln -s /data/web_static/current/ /data/web_static/releases/test/
sudo chown -R ubuntu:ubuntu /data/

