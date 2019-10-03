#--------- Generic stuff all our Dockerfiles should start with so we get caching ------------
# Note this base image is based on debian
FROM kartoza/django-base
MAINTAINER Christiaan van der Merwe <christiaan@kartoza.com>

#RUN  ln -s /bin/true /sbin/initctl

# Pandoc needed to generate rst dumps, uic compressor needed for django-pipeline
RUN apt-get update -y; apt-get -y --force-yes install yui-compressor
RUN apt-get -y install locales && \
    echo "en_ZA.UTF-8 UTF-8" >> /etc/locale.gen && \
    locale-gen en_ZA.UTF-8
ENV LANG en_ZA.UTF-8
ENV LANGUAGE en_ZA:en
ENV LC_ALL en_ZA.UTF-8

ARG Project_tag=live_push
RUN mkdir -p /usr/src; mkdir -p /home/web  && \
	git clone --branch ${Project_tag} --depth 1 https://github.com/christiaanvdm/docker-mezzanine.git /usr/src/website/ && \
	rm -rf /home/web/django_project && \
	ln -s /usr/src/website/django_project /home/web/django_project

RUN cd /usr/src/website/deployment/docker && \
	pip install -r REQUIREMENTS.txt && \
	pip install uwsgi && \
	rm -rf /uwsgi.conf && \
	ln -s ${PWD}/uwsgi.conf /uwsgi.conf && \
	pip uninstall -y django-contrib-comments && \
	pip install django-contrib-comments==1.8.0

RUN apt-get -y install pandoc
RUN dpkg-reconfigure locales
# Open port 8080 as we will be running our uwsgi socket on that
EXPOSE 80

WORKDIR /home/web/django_project
CMD ["uwsgi", "--env", "LC_ALL=en_ZA.UTF-8", "--ini", "/uwsgi.conf"]
