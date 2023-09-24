FROM nvidia/cuda:11.8.0-cudnn8-runtime-ubuntu22.04

ENV PATH=/opt/poetry/bin:$PATH \
    POETRY_HOME=/opt/poetry \
    POETRY_VIRTUALENVS_CREATE=false

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        curl \
        python3-minimal \
        python3-pip \
    && ln -s /usr/bin/python3.10 /usr/bin/python \
    && rm -rf /var/lib/apt/lists/* \
    && curl -sSL https://install.python-poetry.org | python -

WORKDIR /app
COPY . .
RUN poetry install
