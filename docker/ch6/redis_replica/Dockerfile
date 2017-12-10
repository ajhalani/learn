FROM ajhalani/redis
MAINTAINER Ankush Jhalani <ankush.jhalani@gmail.com> 
ENV REFRESHED_AT 2017-07-18

ENTRYPOINT [ "redis-server", "--logfile /var/log/redis/redis-server.log", "--slaveof redis_primary 6379", "--protected-mode no" ]

