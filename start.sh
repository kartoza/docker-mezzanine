#!/bin/bash

# Put any tasks you would like to have carried
# out when the container is first created here
# We do this below because the django_project
# is copied over in a separate docker fs layer
# and so we can't assign www-data write permissions
# to it. So we make a throw away copy in /tmp
# and copy it on first run so that www-data cane
# access the copy...
cp -r /tmp/django_project /home/web/
chown -R www-data.www.data /home/web/django_project

# Set the root passwd - grep docker logs for it
ROOT_PASSWORD=`pwgen -c -n -1 12`
echo "root:$ROOT_PASSWORD" | chpasswd
echo "root login password: $ROOT_PASSWORD"

# Launch supervisor
supervisord -n
