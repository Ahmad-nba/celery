# make the celery app accessible across the project
from .celery import app as celery_app   
__all__ = ("celery_app",)