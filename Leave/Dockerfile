# Dockerfile for Django frontend
FROM python:3.12

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . /app/

# Expose port 8005
EXPOSE 8005

# Command to run the application
CMD ["gunicorn", "--bind", "0.0.0.0:8005", "Leave.wsgi:application"]
