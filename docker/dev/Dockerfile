FROM python:3.11

ARG UID=1000
ARG GID=1000

RUN mkdir /app
WORKDIR /app

RUN groupadd -g $GID app && useradd --create-home --no-log-init -u "${UID}" -g "${GID}" app && chown -R app:app /app

USER app

ENV PYTHONUNBUFFERED 1

COPY backend/requirements*.txt /app/

# Installing dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install -r requirements-dev.txt