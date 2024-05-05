FROM python:3:11.1
RUN curl -sSL https://install.python-poetry.org python3 -
COPY ./app
WORKDIR /app
ENV PATH=$PATH:/root/.local/bin/
RUN poetry install
ENTRYPOINT poetry run flask run --host 0.0.0.0
