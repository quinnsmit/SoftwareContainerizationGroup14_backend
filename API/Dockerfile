## Use a base Python image
#FROM python:3.9-slim
#
## Set environment variables
#ENV PYTHONDONTWRITEBYTECODE 1
#ENV PYTHONUNBUFFERED 1
#
## Set the working directory inside the container
#WORKDIR /app
#
## Install system dependencies
#RUN apt-get update && \
#    apt-get install -y default-libmysqlclient-dev && \
#    apt-get install -y pkg-config && \
#    apt-get install -y gcc && \
#    apt-get install -y python3-dev
#
## Copy the application code to the working directory
#COPY . .
#
## Install Python dependencies
#RUN pip install --no-cache-dir -r requirements.txt
#
## Expose the port your app runs on
#EXPOSE 5000
#
## Command to run the application
#CMD ["python", "app.py"]

FROM python:3.9

# Install MySQL development libraries
RUN apt-get update && \
    apt-get install -y default-libmysqlclient-dev && \
    rm -rf /var/lib/apt/lists/*

# Set the working directory in the container
WORKDIR /app

# Copy the dependencies file to the working directory
COPY requirements.txt .

# Install any needed dependencies specified in requirements.txt
RUN pip install -r requirements.txt --src /usr/local/src

# Copy the rest of the application code to the working directory
COPY . .


EXPOSE 5000
CMD [ "python", "app.py" ]
