# bullseye: latest stable Debian release (base image)
FROM python:3.13.3-slim-bullseye

# Set environment variables
# disables an automatic check for pip updates each time
# Python will not try to write .pyc files
# ensures our console output is not buffered by Docker
ENV PIP_DISABLE_PIP_VERSION_CHECK=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory
WORKDIR /app

# Copy the requirements file into the container
COPY ./requirements.txt .

# Install the dependencies
RUN pip install -r requirements.txt

# Copy the rest of the application code into the containenr
COPY . .