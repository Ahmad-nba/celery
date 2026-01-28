import os
from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dcelery.settings")
# Create the Celery application instance
app = Celery("dcelery")
# Point Celery to the Django settings module for configuration
app.config_from_object("django.conf:settings", namespace="CELERY")

# now we can create tasks using functions with decorators or use classes, like in views, FBV, CBV etc.
# a brief example task is shown below

# and in the tasks.py, we decorate a function as a task like so: @shared_task and define the FVB

# allocating the queues to the workers is done in the docker-compose.yml file
app.conf.task_routes = {
    "cworker.tasks.task1": {"queue": "queue1"}, 
    "cworker.tasks.task2": {"queue": "queue2"},
}
 

# Autodiscover tasks in installed apps, we tell Celery to go through each of the installed apps,
# find a tasks.py file and load any tasks defined there.
app.autodiscover_tasks()
