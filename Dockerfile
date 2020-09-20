# Dockerfile чтобы собрать образ

FROM python:3.7-alpine
WORKDIR /usr/src/app
COPY  requirements.txt .
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev && pip install --no-cache-dir psycopg2 && pip install --no-cache-dir -r requirements.txt
ENTRYPOINT /bin/sh
