FROM python:3.12-slim

WORKDIR /starWarsApi

ENV PYTHONPATH="/starWarsApi"

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app/ ./app/
COPY tests/ ./tests/

HEALTHCHECK --interval=30s --timeout=5s --start-period=5s --retries=3 \
  CMD python -c "import app.star_wars_api" || exit 1

CMD ["python", "app/star_wars_api.py"]