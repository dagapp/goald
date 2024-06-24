FROM ubuntu:latest

RUN apt update && apt install --no-install-recommends -y \
    nginx

COPY ./nginx.conf /etc/nginx/sites-enabled/goald.conf

RUN rm /var/www/html/*
#RUN mkdir -p /var/www/frontend/
COPY ./frontend/public /var/www/html/
RUN rm /etc/nginx/sites-enabled/default

CMD ["nginx", "-g", "daemon off;"]
