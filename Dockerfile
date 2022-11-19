# Python base image. Get this from dockerhub
FROM python:3.11-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Set your working directory
WORKDIR /usr/src/app

# Install dependencies required by the image
RUN apt update && apt install -y g++ libpq-dev gcc musl-dev

# Allow docker to cache installed dependencies between builds 
COPY requirements.txt .
RUN python3 -m pip install -r requirements.txt --no-cache-dir

# Copy and mount the project to the working directory
COPY . .
# Script to run given instruction eg running production server.
CMD ["./run.sh"]
