FROM python:3.9

# When it's building and it reaches this point, the docker-compose didn't set up the volumes yet.
# So poetry install it's going to fail without copying the files.
COPY poetry.lock pyproject.toml /srv/

ENV PYTHONFAULTHANDLER=1
ENV PYTHONUNBUFFERED=1
ENV PYTHONHASHSEED=random
# pip:
ENV PIP_NO_CACHE_DIR=off
ENV PIP_DISABLE_PIP_VERSION_CHECK=on
ENV PIP_DEFAULT_TIMEOUT=100
# poetry:
ENV POETRY_VERSION=1.0.0

WORKDIR /srv

RUN pip install "poetry==$POETRY_VERSION"
RUN poetry config virtualenvs.create false
RUN pwd
RUN ls -la
# If in production, remember to remove dev packages:
# RUN poetry install --no-dev --no-interaction --no-ansi
RUN poetry install --no-interaction --no-ansi
