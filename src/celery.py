from __future__ import absolute_import

from celery import Celery
from src import beat_config

app = Celery(
    'poc-celery-beat',
    broker=beat_config.BROKER_URL,
    backend=beat_config.CELERY_RESULT_BACKEND,
    include=['scr.tasks']
)

app.config_from_object('src.beat_config')
app.log.setup(
    loglevel='DEBUG', 
    redirect_stdouts=True, 
    redirect_level='INFO'
)

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
