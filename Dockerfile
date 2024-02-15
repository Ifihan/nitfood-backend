# pull official base image
FROM python:3.9-slim-bullseye

# set work directory
WORKDIR /code

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# hack to fix time-sync issue on M1
RUN echo "Acquire::Check-Valid-Until \"false\";\nAcquire::Check-Date \"false\";" | cat > /etc/apt/apt.conf.d/10no--check-valid-until

# install necessary packages
RUN apt-get update \
    && apt-get -y install libpq-dev gcc

# install pipenv and project dependencies
RUN pip install -U pipenv
COPY Pipfile Pipfile.lock ./
RUN pipenv install --system --deploy --ignore-pipfile

COPY . . 

# Make the entrypoint script executable
RUN chmod +x entrypoint.sh

# Set the entrypoint
ENTRYPOINT ["./entrypoint.sh"]

# ARG PORT

# ENV PORT=$PORT

# RUN echo $PORT

# ENTRYPOINT python manage.py runserver 0.0.0.0:$PORT