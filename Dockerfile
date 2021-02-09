# Pull base image
FROM python:3.9

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /testcsv-main

# Install dependencies
COPY Pipfile Pipfile.lock /testcsv-main/
RUN pip install pipenv && pipenv install --system

# Copy project
COPY . /testcsv-main/
