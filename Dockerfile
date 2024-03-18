FROM python:3.9-slim-bullseye

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /goald

RUN apt update
RUN apt install --no-install-recommends -y nginx uwsgi uwsgi-plugin-python3 vim

# django stuff
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt --no-cache-dir

COPY . .

# nginx stuff
COPY goald_site/static /var/www/goald/static
COPY goald_site/nginx.conf /etc/nginx/sites-enabled/goald.conf

# entrypoint stuff
RUN chmod +x /goald/entrypoint.sh
ENTRYPOINT ["/goald/entrypoint.sh"]
