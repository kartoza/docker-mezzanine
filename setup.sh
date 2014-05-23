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

# nginx config - don't daemonize
sed -i -e"s/keepalive_timeout\s*65/keepalive_timeout 2/" /etc/nginx/nginx.conf
sed -i -e"s/keepalive_timeout 2/keepalive_timeout 2;\n\tclient_max_body_size 100m/" /etc/nginx/nginx.conf
echo "daemon off;" >> /etc/nginx/nginx.conf

cd /home/web
virtualenv venv
venv/bin/pip install -r REQUIREMENTS.txt
