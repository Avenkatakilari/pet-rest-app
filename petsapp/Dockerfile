FROM python:3.12.2-slim

ENV PYTHONUNBUFFERED 1

RUN mkdir /app

WORKDIR /app

COPY . .

# Install packages needed to build node modules
RUN apt-get update -qq && \
    apt-get install -y build-essential pkg-config python-is-python3 default-libmysqlclient-dev

RUN pip install -r requirements.txt

# Starting our application
CMD [ "python", "./petsapp/manage.py", "makemigrations", "api" && "python", "./petsapp/manage.py", "migrate" && "python", "./petsapp/manage.py", "runserver"]

# Exposing server port
EXPOSE 9090