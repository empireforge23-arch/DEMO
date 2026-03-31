# Use an official Python runtime as base image
FROM python:3.9-slim

WORKDIR /app

# Copy requirements first (for better caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY app.py .
COPY deploy.sh .

# Make the deploy script executable
RUN chmod +x deploy.sh

# Expose port 5000 (the port your app runs on)
EXPOSE 5000

#
CMD ["python", "app.py"]