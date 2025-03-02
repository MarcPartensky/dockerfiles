# Dockerfile
FROM python:3.11-alpine as builder

# Configuration de base
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_DEFAULT_TIMEOUT=100

# Installation des dépendances système
RUN apk add --no-cache --virtual .build-deps \
    build-base \
    postgresql-dev \
    git \
    poetry

RUN git clone https://github.com/ankicommunity/ankicommunity-api-server /app

WORKDIR /app
RUN ls /app

RUN pip install --upgrade pip
RUN poetry export -o requirements.txt
RUN pip install -r requirements.txt

# ------------------------------------------------------------------------
# Stage finale
# ------------------------------------------------------------------------
FROM python:3.11-alpine

# Dépendances runtime minimales
RUN apk add --no-cache --update \
    libpq \
    busybox-extras \
    su-exec

# Copie des artefacts depuis le builder
COPY --from=builder /usr/local/lib/python3.11/site-packages/ /usr/local/lib/python3.11/site-packages/
COPY --from=builder /usr/local/bin/ /usr/local/bin/
COPY --from=builder /app /app

# Configuration de l'utilisateur non-root
RUN addgroup -S djankiserv && adduser -S djankiserv -G djankiserv \
    && mkdir -p /static /media \
    && chown -R djankiserv:djankiserv /app /static /media

WORKDIR /app

# Entrypoint optimisé
RUN echo $'#!/bin/sh\n\
set -e\n\
\n\
# Attente PostgreSQL\n\
until nc -z $DB_HOST $DB_PORT; do\n\
  echo "Waiting for PostgreSQL..."\n\
  sleep 1\n\
done\n\
\n\
# Migrations et collectstatic\n\
su-exec djankiserv python manage.py migrate --noinput\n\
su-exec djankiserv python manage.py collectstatic --noinput\n\
\n\
# Exécution de l\'application\n\
exec su-exec djankiserv gunicorn --bind 0.0.0.0:8000 --workers $(( $(nproc) * 2 + 1 )) config.wsgi:application\n\
' > /entrypoint.sh && chmod +x /entrypoint.sh

VOLUME /static /media
EXPOSE 8000
ENTRYPOINT ["/entrypoint.sh"]
