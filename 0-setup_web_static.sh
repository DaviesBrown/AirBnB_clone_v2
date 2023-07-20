#!/usr/bin/env bash
# a script to setup my web servers for the deployment of web_static

# update packages and install nginx
sudo apt-get -y update
sudo apt-get -y install nginx

# creating paths
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared
sudo touch /data/web_static/releases/test/index.html

# Print Welcome message
echo "Welcome to my site!"  >> /data/web_static/releases/test/index.html

# Check if directory current exist
if [ -d "/data/web_static/current" ]
then
        sudo rm -rf /data/web_static/current
fi

# creating a symbolink link  linked to the folder
sudo ln -s -f /data/web_static/releases/test/ /data/web_static/current

# give ownership of the /data/ folder to the ubuntu user AND group
sudo chown -hR ubuntu:ubuntu /data/

# Update the Nginx configuration to serve the file content
sudo sed -i '38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t\tautoindex off;\n\t}\n' /etc/nginx/sites-enabled/default

# restart nginx server
sudo service nginx restart
