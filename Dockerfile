FROM python:3.9-slim-buster

ARG UID
RUN apt update && \
    apt install -y build-essential libpq-dev netcat-openbsd && \
    adduser \
        --uid "${UID?}" \
        --disabled-password \
        --gecos "Orchard user" \
        orchard && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN mkdir /app

COPY manage.py /app/manage.py
COPY scripts /app/scripts
COPY requirements /app/requirements
COPY orchard /app/orchard

WORKDIR /app

ARG DJANGO_ENV
RUN pip install --require-hashes -r /app/requirements/${DJANGO_ENV?}.txt

USER orchard
CMD /app/scripts/run-django
