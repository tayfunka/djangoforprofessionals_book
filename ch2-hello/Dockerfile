# Pull base image
# smaller in size slim
# bullseye: latest stable Debian release
FROM python:3.13.3-slim-bullseye

# Set environment variables
# disables an automatic check for pip updates each time
# Python will not try to write .pyc files
# ensures our console output is not buffered by Docker
ENV PIP_DISABLE_PIP_VERSION_CHECK=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set a default working directory
WORKDIR /app

# Install dependencies
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# Copy project
COPY . .