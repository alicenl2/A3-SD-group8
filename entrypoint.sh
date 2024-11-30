#!/bin/sh
# Wait for the PostgreSQL database to be available
echo "Waiting for PostgreSQL to be ready..."
while ! nc -z db 5432; do
  sleep 1
done
echo "PostgreSQL is ready!"

python create_tables.py

# if everything is good, we start the Flask application
exec gunicorn -w 4 -b 0.0.0.0:5000 app:app

