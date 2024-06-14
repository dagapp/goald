FROM ubuntu:latest

RUN apt update && apt install --no-install-recommends -y \
    nginx

COPY ./nginx.conf /etc/nginx/sites-enabled/goald.conf

RUN mkdir -p /var/www/goald-frontend/
COPY frontend/static /var/www/goald-frontend/

CMD ["nginx", "-g", "daemon off;"]
