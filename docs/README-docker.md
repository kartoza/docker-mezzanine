## Production

1. After setting up your host, from the catalogue select KartozaWebsite. Set the site address and the host affinity (it should be a label that matches the name of the host you wish to deploy on).
2. Copy/Download the latest database backup into the SFTP container folder home/ftp/postigs-history-data
3. Copy/Download the latest media files into the SFTP container folder home/ftp/django-media-data
4. SSH into the postgress container, and run “pg_restore latest.dmp” in /home/backups. You may need to run “pg_restore latest.dmp -d gis” if the sites aren’t added correctly. Pg_restore also sometime does not run to completion. Using “pg_restore latest.dmp --clean” may help.

5. https://stackoverflow.com/questions/8370658/how-to-serve-django-media-files-via-nginx - Ensure the nginx config file is serving media files correctly. You need:

    location /media { <br>
    autoindex on; <br>
    alias /home/web/media/; 
    }

    In your nginx configuration file.
6. Add a load balancer listening on web port 80:80 in a separate stack.

###HTTPS:

The preferred way to install SSL on rancher is via letsencrypt.

An applicable guide in Nov 2019: https://www.digitalocean.com/community/tutorials/how-to-secure-your-rancher-web-app-with-let-s-encrypt-on-ubuntu-16-04 

###DNS:

Note that three domains should point to the public site:

www.kartoza.com
Kartoza.com
*.kartoza.com

###Backups:

#### Deploying the SFTP container: 

Use can be made of any simple SFTP container. In Nov 2019, the https://hub.docker.com/r/atmoz/sftp/ container could be used as follows: <br>
Command = kartoza:kartoza:1001 <br>
Volumes: Add applicable volumes. <br>
Open the port (public) 2222 - (private) 22 <br>

Run “usermod -d / kartoza” inside the sftp container to set the default sftp directory to the root.

You should now be able to sftp into kartoza@www.kartoza.com to pull the necessary files.

#### Pulling the files from the SFTP container:
The simplest method to retrieve the files from the container is with an ftp cronjob.

![](docs/architecture.png)