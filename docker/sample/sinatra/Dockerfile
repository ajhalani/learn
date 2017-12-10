FROM ubuntu:14.04
MAINTAINER Ankush Jhalani "ankush.jhalaniexample.com"
ENV REFRESHED_AT 2014-06-01
RUN apt-get update -yqq && apt-get -yqq install software-properties-common
RUN apt-add-repository ppa:brightbox/ruby-ng
RUN apt-get update -yqq && apt-get -yqq install ruby2.3 ruby2.3-dev build-essential redis-tools
RUN gem install --no-rdoc --no-ri sinatra json redis
RUN mkdir -p /opt/webapp
EXPOSE 4567
CMD [ "/opt/webapp/bin/webapp" ]
