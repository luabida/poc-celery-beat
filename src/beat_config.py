from __future__ import absolute_import

from datetime import timedelta
import random

beat_schedule = {
    'add-every-30-seconds': {
        'task': 'add',
        'schedule': timedelta(seconds=30),
        'args': (random.randint(0, 9), random.randint(0, 9))
    },
}

broker_url = 'amqp://guest:guest@localhost:5672'

result_backend = 'rpc://guest:guest@localhost:5672'
