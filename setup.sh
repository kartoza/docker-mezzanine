# Add any tasks here that should happen during image creation
#!/bin/bash
cd /etc/nginx/sites-available/
rm default
ln -s /home/web/server-conf/nginx-site.conf default

cd /etc/uwsgi/apps-available/
ln -s /home/web/server-conf/django_project_uwsgi.ini default

cd /etc/uwsgi/apps-enabled/
ln -s ../apps-available/default .

cd /etc/supervisor/conf.d/
ln -s /home/web/server-conf/supervisor-nginx.conf .
ln -s /home/web/server-conf/supervisor-uwsgi.conf .

cd /home/web
virtualenv venv
venv/bin/pip install -r REQUIREMENTS.txt
