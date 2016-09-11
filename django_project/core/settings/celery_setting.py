from datetime import timedelta

# call poll twitter every 10 mins
CELERYBEAT_SCHEDULE = {
    'poll_twitter': {
        'task': 'tasks.poll_twitter',
        'schedule': timedelta(minutes=10),
    },
}

CELERY_TIMEZONE = 'UTC'
