"""
WSGI config for core project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
from django.core.wsgi import get_wsgi_application
_application = get_wsgi_application()

import django.core.handlers.wsgi  # noqa

def application(environ, start_response):
    """Factory for the application instance.

    :param environ: os environment passed in by web server.
    :type environ: dict

    :param start_response: ?
    :type start_response: ?

    Places env vars defined in apache conf into a context accessible by django.
    """
    return _application(environ, start_response)

