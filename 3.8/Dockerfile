FROM            python:3.8

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
                && apt-get update \
                && apt-get install -y gcc git make $EXTRA_BUILD_DEPS --no-install-recommends \
                && apt-get install -y libjpeg-dev libmagic-dev libpq-dev $EXTRA_DEPS --no-install-recommends \
                && pip install --no-cache-dir -r $REQUIREMENTS \
                && apt-get remove -y gcc git make $EXTRA_BUILD_DEPS --purge \
                && rm -rf /var/lib/apt/lists/

ONBUILD COPY    ./src /app

ENV             PYTHONUNBUFFERED=1 \
                PYTHONPATH=/app \
                APP_MODULE=app.main:app \
                WORKERS_PER_CORE=1

EXPOSE          80

ENTRYPOINT      ["/prestart.sh"]

CMD             ["/start.sh"]
