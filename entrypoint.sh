#!/bin/sh

# Script to wait for the database to be ready, run Django migrations, and start the Django application

echo "Waiting for database..."

# Replace 'db_host' and 'db_port' with your database host and port
while ! nc -z db_host db_port; do
  sleep 1
done

echo "Database started"

# Navigate to your Django project directory if necessary
# cd /path/to/your/django/project

# Run Django migrations
# Note: You might need to adjust this if you're using a custom manage.py path or virtual environment
python manage.py makemigrations
python manage.py migrate
python manage.py shell
python manage.py test

# You can also include other Django management commands if necessary
# For example, to create a superuser (remove if not needed)
# python manage.py createsuperuser --no-input

# Start the Django application
# Adjust this command based on how you run your Django app (e.g., using Gunicorn)
web: python manage.py migrate && gunicorn backend.wsgi --log-file -
# gunicorn your_project.wsgi:application --bind 0.0.0.0:8000
