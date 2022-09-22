FROM python:3

RUN apt-get update && apt-get install -y netcat && apt-get clean

WORKDIR /app

COPY pyproject.toml poetry.lock ./

RUN curl -sSL https://install.python-poetry.org | python3 -

ENV PATH="/root/.local/bin:$PATH"

RUN python -m pip install --upgrade pip
RUN poetry config virtualenvs.create false \
    && poetry install --no-dev --no-interaction

COPY config.yml ./
COPY run.sh ./
COPY trips.py ./

RUN chmod +x ./run.sh

ENV RABBIT_HOST=nameko-rabbit
ENV RABBIT_PORT=5672
ENV REDIS_HOST=redis
ENV REDIS_PORT=6379

CMD ["./run.sh"]
