# Use an official Python runtime as the base image
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the application code into the container
COPY app.py /app/
COPY requirements.txt /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the default port (optional, depends on your needs)
EXPOSE 8000

# Set environment variables (override these when running the container)
ENV KUMA__URL="http://uptime-kuma-instance/api"
ENV KUMA__USERNAME="your-username"
ENV KUMA__PASSWORD="your-password"

# Command to run the application
ENTRYPOINT ["python", "app.py"]
