# this are the settings that were shared in settings.py where celery shared the same settings with django

# Celery configuration
import os


broker_url = os.getenv("CELERY_BROKER_URL", "redis://redis:6379/0")
result_backend = os.getenv("CELERY_RESULT_BACKEND", "redis://redis:6379/0")
