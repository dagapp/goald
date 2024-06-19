FROM debian:bookworm

WORKDIR /goald-frontend

RUN apt-get update && apt-get install --no-install-recommends -y \
    nodejs  \
    npm     \
    nginx   \
&& rm -rf /var/lib/apt/lists/*

COPY . .

RUN npm install
RUN npm run build

# nginx stuff
COPY ./nginx.conf /etc/nginx/sites-enabled/goald.conf
RUN mkdir -p ./static /var/www/goald-frontend/
RUN ln -s ./static /var/www/goald-frontend/static

# entrypoint stuff
RUN chmod +x /goald-frontend/entrypoint.sh
ENTRYPOINT ["/goald-frontend/entrypoint.sh"]
