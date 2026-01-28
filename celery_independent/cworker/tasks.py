
from celery import shared_task


@shared_task(name="cworker.tasks.task1")
def add(x, y):
    return x + y

@shared_task(name="cworker.tasks.task2")
def multiply(x, y):
    return x * y