# python-poetry-iot

## Running nginx and uwsgi on Arch Linux
Install dependencies:
```
pacman -S uwsgi uwsgi-plugin-python nginx
```
However, I do not advice to use uwsgi specific to any Linux distro, as it is better to use one that is built for python:
```
pip install uwsgi
```
Make a directory for server config:
```
sudo mkdir /server/app
sudo chown -R http:http /server/app
```
Create a directory and config file for uWSGI: 

```
sudo mkdir -p /etc/uwsgi/vassals
sudo chown -R http:http /etc/uwsgi/vassals
sudo touch /etc/uwsgi/vassals/app.ini
```
Config (`app.ini`) file:
```
[uwsgi]
socket = /server/app/uwsgi.sock
chmod-socket = 775
chdir = /server/app
master = true
binary-path = /server/app/venv/bin/uwsgi
virtualenv = /server/app/venv
module = crud:app
uid = http
gid = http
processes = 1
threads = 1
plugins = python3,logfile
logger = file:/server/app/uwsgi.log
```
Settings for nginx:
In `/etc/nginx/nginx.conf`, under `http directive`:
```
include /etc/nginx/conf.d/*.conf;
``` 
Config file (`/etc/nginx/conf.d/app.conf`):
```
server {
    listen 80;
    # listen 443 ssl;
    server_name 192.168.0.107; # your internal ip

    location / {
        include uwsgi_params;
        uwsgi_pass unix:/server/app/uwsgi.sock;
    }

    location /static {
        alias /server/app/static;
    }

    location /favicon.ico {
        alias /server/app/static/favicon.ico;
    }
}
```

Run services:
```
systemctl start nginx
systemctl start emperor.uwsgi
```
