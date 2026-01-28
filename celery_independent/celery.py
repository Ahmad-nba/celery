

from celery import Celery
app = Celery('celery_independent')
app.config_from_object('celery_independent.celeryconfig')

app.conf.imports = ('celery_independent.cworker.tasks',)
app.autodiscover_tasks()