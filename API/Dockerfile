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

FROM python:3.6-slim

RUN apt-get clean \
    && apt-get -y update

RUN apt-get -y install \
    nginx \
    python3-dev \
    build-essential

WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt --src /usr/local/src

COPY . .

EXPOSE 5000
CMD [ "python", "app.py" ]
