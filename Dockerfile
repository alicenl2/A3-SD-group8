# python image from the Docker Hub, slim version for smaller size
FROM python:3.10-slim

# we set the working directory in the container to be /app
WORKDIR /app

# Install system dependencies needed for psycopg2 and PostgreSQL client libraries
RUN apt-get update && apt-get install -y \
    libpq-dev gcc netcat-openbsd --no-install-recommends && \
    rm -rf /var/lib/apt/lists/*

# Copy the requirements.txt file into the container
COPY requirements.txt .

RUN pip install -r requirements.txt

# copy rest of the application code into the container
COPY . .

# make sure that the entrypoint script is executable
RUN chmod +x /app/entrypoint.sh

# the entrypoint script contains the exec command, and verifies conditions
ENTRYPOINT ["/app/entrypoint.sh"]
# replaces CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]


