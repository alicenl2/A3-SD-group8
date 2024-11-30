#!/bin/sh
# Wait for the PostgreSQL database to be available
if [ -z "$DATABASE_URL" ]; then
  echo "Error: DATABASE_URL environment variable is not set."
  exit 1
fi

python create_tables.py

# if everything is good, we start the Flask application
exec gunicorn -w 4 -b 0.0.0.0:5000 app:app

