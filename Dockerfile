FROM python:3.11.0-slim-buster

RUN apt-get update -y && \
    apt-get install -y less vim curl libpq-dev gcc \
    && apt-get clean \
    && rm -rf /var/lib/apt/list/*

WORKDIR /code

COPY poetry.lock ./
COPY pyproject.toml ./
COPY poetry.toml ./


RUN curl -sSL https://install.python-poetry.org | python - --version 1.3.1
ENV PATH=/root/.local/bin:$PATH

RUN poetry install --no-interaction --no-root

COPY ./app /code/app