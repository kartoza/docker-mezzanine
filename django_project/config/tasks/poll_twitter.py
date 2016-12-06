__author__ = 'rischan'

from django.core import management
from celery import shared_task
from celery.utils.log import get_task_logger

import logging

logger = logging.getLogger(__name__)


@shared_task(name='tasks.poll_twitter')
def poll_twitter():
    management.call_command('poll_twitter', '--force')
