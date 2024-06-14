FROM ubuntu:latest

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV TZ=Etc/UTC
ENV DEBIAN_FRONTEND=noninteractive

WORKDIR /goald-app

RUN apt update && apt install --no-install-recommends -y \
    uwsgi                           \
    uwsgi-plugin-python3            \
    python3-django                  \
    python3-djangorestframework     \
    python3-pillow                  \
    python3-psycopg2                \
    python3-bcrypt                  \
&& rm -rf /var/lib/apt/lists/*

COPY backend backend
COPY goald goald
COPY manage.py manage.py

RUN mv /goald-app/goald/goald.ini /etc/uwsgi/apps-available/
RUN ln -s /etc/uwsgi/apps-available/goald.ini /etc/uwsgi/apps-enabled/

# entrypoint stuff
COPY app-entrypoint.sh app-entrypoint.sh
ENTRYPOINT ["/goald-app/app-entrypoint.sh"]
