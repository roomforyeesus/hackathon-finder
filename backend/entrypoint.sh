#!/bin/bash


# Making migrations
python3 manage.py makemigrations

# Apply database migrations
echo "Apply database migrations"
python3 manage.py migrate

# Collect static files
echo "Collect static files"
python3 manage.py collectstatic --no-input

# Start server
echo "Starting server"
python3 manage.py runserver 0.0.0.0:8000
gunicorn config.wsgi:application --bind 0.0.0.0:8000

exec "$@"