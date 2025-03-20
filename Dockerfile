# Use an official Python runtime as a parent image
FROM python:3.13.2-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements-deploy.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements-deploy.txt

# Copy the current directory contents into the container
COPY . .

# Expose port 5000 for the Flask app
EXPOSE 5008

# Set environment variables
ENV FLASK_APP=app.py
ENV MLFLOW_TRACKING_URI=http://host.docker.internal:5003

# Run the Flask app
CMD ["flask", "run", "--host=0.0.0.0", "--port=5008"]