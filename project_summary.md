<!-- Project Summary -->

### Flow

1 Dockerization
Add a django service container
Add a redis service container
Add a celery worker service container
2 Create and register a task
3 Staring the celery worker
4 Calling the task from iterative django shell

## Dockerization

# docker-compose.yml
- Add a venv,
- Add git and gitignore

Start by adding this file, it defines how the micro services will eventually communicate.
define services, their build context, environment variables and dependencies plus commands.
a simple format is shown below.

```yaml
version: "3.8"
services:
  django: #-this is the name of the service
    build:
      context: ./dcelery #- the build context is the directory where the Dockerfile is located
      dockerfile: Dockerfile #- the name of the dockerfile which further defines how the image is built
    ports:
      - "8000:8000" #- where to get the service from outside the container if its required to be accessed externally
    volumes:
      - .:/usr/src/app #-the volumes is a means of making our work available to the container by mounting the current directory to the container's working directory.
    environment: #- environment variables to be passed to the container and accessed in the application via os.getenv
      - ALLOWED_HOSTS=localhost,127.0.0.1
      - SECRET_KEY=your_secret_key_here
      - CELERY_BROKER_URL=redis://redis:6379/0
    depends_on: #what the service could depend on
      - redis
```

# Dockerfile

this file defines how the image is built for the django service.

```dockerfile
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
```

# other additives

-create a entry.sh file, be carefull eith this as when working with bash terminal and windows some commands wont work, so use the ,,, /bin/sh not /bin/bash
-same applies when accessing the iterative terminal, where we create manage.py commands but in a space that the container can see and track, be cautious of the command in bash env

- Creating other services will be the same, route, just add them to the docker-compose.yml

# Creating the worker

- This is a entity that listens to the message provider always for any tasks and run them and produce a result that can be sent back to the original provider
- This can be another django app, but its executing a django related tsak that we wanted to distribute off the main server

**_ Make the celery accessible eacross the workspace _**

- In the core backend dir, you add a celery file, add the configs and allow celery to such for tasks across all modules
- In this very dir's **init**.py,

```ini
# make the celery app accessible across the project
from .celery import app as celery_app
__all__ = ("celery_app",)
```

- Ensure you also adjust your settings.py, to
  read from the os.env()
  add the celery broker and result backend routes

- Ensure you also freeze the essential packages that the container has to install to run,
  asgiref==3.11.0
  Django==6.0.1
  sqlparse==0.5.5
  tzdata==2025.3
  celery==5.6.2
  redis==7.1.0

## Creating a task
- Add the fbv or cbv with a decorator @shared_task accompined in the tasks.py in the modules dir ideally workers
- 

## Initiating and completinga task
- Access the iterative terminal
- head to python manage.py shell
- access the taks
``` task
from worker.tasks import task_function_name
task_function_name.delay() or async()
``` then watch the container logs it should show recived and succeded , then a result of the task

