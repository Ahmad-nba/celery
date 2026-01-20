# Use an official Python runtime as a parent image
FROM python:3.12-alpine

# set the working directory in the container
WORKDIR /usr/src/app

# set environment variables, tell Python to not buffer outputs and not to write .pyc files
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# upgrade pip to the latest version
RUN pip install --upgrade pip 
# install dependencies and copy the requirements file to the working directory's requirements.txt file
COPY ./requirements.txt /usr/src/app/requirements.txt
# run pip install to install the dependencies required
RUN pip install -r requirements.txt

COPY ./entrypoint.sh /usr/src/app/entrypoint.sh

# copy the whole project to the container working directory
COPY . /usr/src/app/

# run the entrypoint.sh file ; runs every time the container starts
ENTRYPOINT ["/usr/src/app/dcelery/entrypoint.sh"]
