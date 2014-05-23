docker-django
=============

A simple docker container that runs ssh

To build the image do:

```
docker build -t kartoza/mezzanine git://github.com/timlinux/docker-mezzanine
```

To run a container do:

```
docker run --name "ssh" -p 9001:22 -p 9000:80 -d -t kartoza/mezzanine
```

To log into your container do:

```
ssh root@localhost -p 9001
```

Default password will appear in docker logs:

```
docker logs <container name> | grep root login password
```

To open the web site go to http://localhost:9000

-----------

Tim Sutton (tim@linfiniti.com)
May 2014
