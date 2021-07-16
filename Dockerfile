# Use an official Python runtime as a parent image
FROM python:3.7.5-stretch

RUN apt-get update && apt-get install -y \
python3-dev \
build-essential    
        
COPY requirements.txt /app/requirements.txt
# Set the working directory to /app
WORKDIR /app

# Install any needed packages specified in requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /app
# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD ["python", "app.py"]
