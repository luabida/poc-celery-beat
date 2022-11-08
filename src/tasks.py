from __future__ import absolute_import

from celery import Celery
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)

app = Celery('poc-celery-beat')

@app.task(name="add")
def sum(x, y):
    logger.info(f"[add] initiated. ({x} + {y})")
    return x + y
