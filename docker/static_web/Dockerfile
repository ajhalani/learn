FROM ubuntu:14.04
MAINTAINER Ankush Jhalani "ajhalani@bgov.com"
ENV REFRESHED_AT 2014-07-02
RUN apt-get update && apt-get install -y nginx
RUN echo 'Hi I am your container' \
		> /usr/share/nginx/html/index.html
EXPOSE 80
ENTRYPOINT ["/usr/sbin/nginx"]
CMD ["-h"]
