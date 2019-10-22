FROM            python:3.8-alpine

ONBUILD ARG     EXTRA_DEPS
ONBUILD ARG     EXTRA_BUILD_DEPS
ONBUILD ARG     REQUIREMENTS_FILE

WORKDIR         /app

COPY            build/prestart.sh /prestart.sh
COPY            build/start.sh /start.sh
COPY            build/start-reload.sh /start-reload.sh
COPY            build/gunicorn_conf.py /gunicorn_conf.py

ONBUILD COPY    requirements /requirements

ONBUILD RUN     set -ex \
                && if [ "x$REQUIREMENTS_FILE" = "x" ] ; then REQUIREMENTS="/requirements/base.txt" ; else REQUIREMENTS="$REQUIREMENTS_FILE" ; fi \
                && apk update \
                && apk add --no-cache --virtual .build-deps gcc git libc-dev linux-headers make musl-dev postgresql-dev \
                && apk add --no-cache --virtual .build-deps-extra $EXTRA_BUILD_DEPS \
                && apk add --no-cache jpeg-dev libpq zlib-dev \
                && apk add --no-cache $EXTRA_DEPS \
                && pip install --no-cache-dir -r $REQUIREMENTS \
                && apk del --no-cache .build-deps \
                && apk del --no-cache .build-deps-extra

ONBUILD COPY    ./src /app

ENV             PYTHONUNBUFFERED=1 \
                PYTHONPATH=/app \
                APP_MODULE=app.main:app \
                WORKERS_PER_CORE=1

EXPOSE          80

ENTRYPOINT      ["/prestart.sh"]

CMD             ["/start.sh"]
