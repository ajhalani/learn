FROM ubuntu:14.04
MAINTAINER Ankush Jhalani "ankush.jhalani@example.com"
ENV REFRESHED_AT 2014-06-01
RUN apt-get -yyq update && apt-get -yqq install redis-server redis-tools
EXPOSE 6379
ENTRYPOINT [ "/usr/bin/redis-server" ]
CMD []
