#!/bin/bash

exec celery --workdir src/ --config beat_config -A tasks worker -B --loglevel=DEBUG
