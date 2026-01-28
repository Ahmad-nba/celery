# Celery Task Routing with Docker (Django + Redis)

This document describes the **correct, production-safe way** to route Celery tasks to different queues using Docker, Django, and Redis, and the **checks required to verify that routing actually works**.

It also highlights common failure modes discovered during debugging.

---

## 1. Architecture Overview

- **Django service**  
  Acts as the **task producer**.
- **Celery workers**  
  Consume tasks from specific queues.
- **Redis**  
  Message broker.
- **Queues**
  - `queue1` → handled by worker A
  - `queue2` → handled by worker B

**Key rule:**  
> *All workers must agree on task names and queue names, byte-for-byte.*

---

## 2. Celery Configuration in Django (`celery.py`)

Location: `dcelery/celery.py`

```python
import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dcelery.settings")

app = Celery("dcelery")
app.config_from_object("django.conf:settings", namespace="CELERY")

# Task routing
app.conf.task_routes = {
    "cworker.tasks.task1": {"queue": "queue1"},
    "cworker.tasks.task2": {"queue": "queue2"},
}

# Auto-discover tasks from installed apps
app.autodiscover_tasks()
