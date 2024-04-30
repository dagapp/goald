FROM debian:bookworm

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /goald

RUN apt update && apt install --no-install-recommends -y \
    uwsgi                   \
    uwsgi-plugin-python3    \
    python3-django          \
    python3-pillow          \
    python3-bcrypt          \
    nginx                   \
    vim                     \
&& rm -rf /var/lib/apt/lists/*

COPY goald_app goald_app
COPY goald_site goald_site
COPY manage.py manage.py

# nginx stuff
COPY goald_site/nginx.conf /etc/nginx/sites-enabled/goald.conf

# entrypoint stuff
COPY entrypoint.sh entrypoint.sh
RUN chmod +x /goald/entrypoint.sh
ENTRYPOINT ["/goald/entrypoint.sh"]
