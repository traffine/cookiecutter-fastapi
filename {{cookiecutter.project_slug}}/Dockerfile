FROM python:3.10.0

ENV PYTHONUNBUFFERED 1

EXPOSE 8080
WORKDIR /app

COPY poetry.lock pyproject.toml ./
RUN pip install --upgrade pip && \
    pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-dev

COPY app ./app
ENV PYTHONPATH app
ENTRYPOINT ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]
