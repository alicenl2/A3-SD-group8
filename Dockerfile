# Development stage
FROM python:3.10-slim AS development

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Production stage
FROM python:3.10-slim AS production

WORKDIR /app
COPY --from=development /app /app
RUN pip install --no-cache-dir gunicorn

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
