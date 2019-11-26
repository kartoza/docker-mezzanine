## Quick Installation Guide

For deployment we use [docker](http://docker.com) so you need to have docker 
running on the host. Ford3 is a django app so it will help if you have
some knowledge of running a django site.

### Clone

```
git clone git://github.com/kartoza/docker-mezzanine.git
cd docker-mezzanine
```

- We will use Makefile script available under deployment folder.
- Any `make` commands should be run under deployment folder.

### Build
```
cd deployment
make build
make web
make devweb
```
### Restore DB and Media Files
#### With an existing environment

At this point you need to obtain and restore a copy of the database and media files.<br>
Note that the website will not function correctly without the database. Media files are not critical.

#### Without an existing environment
First we need to make our migrations and migrate.
```
make update-migrations
make migrate
```
After your database schema is in place, you need to:
1. Create a site 
2. Start adding pages
### Add superuser
In order to grant yourself access to the admin page (/admin) you must create youreself a superuser using:
```
make superuser
```

### Run a server from a container
```
make up
make shell
python manage.py runserver 0.0.0.0:8080
```

### Browse

Open your favorite browser and go to: `http://localhost`