#FROM mcr.microsoft.com/devcontainers/python:1-3.11-bullseye
#
#ENV PYTHONUNBUFFERED 1
#
## Copy the requirements file into the container
#COPY requirements.txt /tmp/pip-tmp/
#
## Install any needed packages specified in requirements.txt
#RUN pip3 --disable-pip-version-check --no-cache-dir install -r /tmp/pip-tmp/requirements.txt \
#    && rm -rf /tmp/pip-tmp
#
## Install additional OS packages
#RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
#    && apt-get -y install --no-install-recommends postgresql-client
#
## Clean up
#RUN apt-get clean && rm -rf /var/lib/apt/lists/*

#### New Below #####
# Use the official Python image from the Docker Hub
FROM python:3.11

# Set the working directory in the container
WORKDIR /app/backend

# Copy the requirements file into the container
COPY requirements.txt /app/

# Install the dependencies
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy the rest of the application code into the container
COPY backend /app/backend

# Expose the port the app runs on
EXPOSE 8000

# Command to run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]