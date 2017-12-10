FROM ubuntu:14.04
MAINTAINER Ankush Jhalani <ankush.jhalani@gmail.com> 
ENV REFRESHED_AT 2017-07-18

RUN apt-get -yqq update
RUN apt-get -yqq install software-properties-common python-software-properties
RUN apt-add-repository ppa:chris-lea/redis-server
RUN apt-get -yqq update
RUN apt-get -yqq install redis-server redis-tools

VOLUME [ "/var/lib/redis", "/var/log/redis" ]

EXPOSE 6379

CMD []

