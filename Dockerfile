FROM python:3.12-slim

WORKDIR /starWarsApi

ENV PYTHONPATH="/starWarsApi"

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app/ ./app/
COPY tests/ ./tests/

CMD ["python", "app/star_wars_api.py"]