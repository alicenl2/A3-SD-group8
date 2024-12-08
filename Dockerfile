# python image from the Docker Hub, slim version for smaller size
FROM python:3.10-slim AS development

# we set the working directory in the container to be /app
WORKDIR /app

# Install system dependencies needed for psycopg2 and PostgreSQL client libraries
RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    netcat-openbsd \ 
    --no-install-recommends

# Copy the requirements.txt file into the container
COPY requirements.txt .
RUN pip install -r requirements.txt

#production
FROM python:3.10-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    libpq-dev \
    netcat-openbsd \
    --no-install-recommends && \
    rm -rf /var/lib/apt/lists/*

# copy installed packages from builder
COPY --from=development /usr/local/lib/python3.10/site-packages/ /usr/local/lib/python3.10/site-packages/
COPY --from=development /usr/local/bin/ /usr/local/bin/

# copy rest of the application code into the container
COPY . .

# make sure that the entrypoint script is executable
RUN chmod +x /app/entrypoint.sh

ENTRYPOINT ["/app/entrypoint.sh"]


