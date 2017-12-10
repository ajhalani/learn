FROM ubuntu:14.04
MAINTAINER Ankush Jhalani <ankush.jhalani@gmail.com> 
ENV REFRESHED_AT 2017-07-18

RUN apt-get -yqq update && apt-get -yqq install nodejs npm
RUN ln -s /usr/bin/nodejs /usr/bin/node
RUN mkdir -p /var/log/nodeapp

ADD nodeapp /opt/nodeapp/

WORKDIR /opt/nodeapp
RUN npm install

VOLUME [ "/var/log/nodeapp" ]

EXPOSE 3000

ENTRYPOINT [ "nodejs", "server.js" ]

