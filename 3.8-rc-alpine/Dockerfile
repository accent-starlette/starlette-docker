FROM            python:3.8-rc-alpine

ONBUILD ARG     REQUIREMENTS_FILE=/requirements/base.txt

RUN             set -ex \
                && apk update \
                && apk add --no-cache \
                    jpeg-dev \
                    libmagic \
                    libpq \
                    zlib-dev

WORKDIR         /app

COPY            build/prestart.sh /prestart.sh
COPY            build/start.sh /start.sh
COPY            build/start-reload.sh /start-reload.sh
COPY            build/gunicorn_conf.py /gunicorn_conf.py

ONBUILD COPY    requirements /requirements

ONBUILD RUN     set -ex \
                && apk update \
                && apk add --no-cache --virtual .build-deps \
                    gcc \
                    git \
                    libc-dev \
                    linux-headers \
                    make \
                    musl-dev \
                    postgresql-dev \
                && pip install --no-cache-dir -r $REQUIREMENTS_FILE \
                && apk del --no-cache .build-deps

ONBUILD COPY    ./src /app

ENV             PYTHONUNBUFFERED=1 \
                PYTHONPATH=/app \
                APP_MODULE=app.main:app \
                WORKERS_PER_CORE=1

EXPOSE          80

ENTRYPOINT      ["/prestart.sh"]

CMD             ["/start.sh"]
