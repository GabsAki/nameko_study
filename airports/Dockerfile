FROM python:3

RUN apt-get update && apt-get -y install netcat && apt-get clean

# This will create the working directory for the other commands.
WORKDIR /app

COPY pyproject.toml poetry.lock

RUN poetry config virtualenvs.create false \
    && poetry install --no-dev --no-interaction -vvv

COPY config.yml ./
COPY run.sh ./
COPY aiports.py ./

RUN chmod +x ./run.sh

CMD ["./run.sh"]
