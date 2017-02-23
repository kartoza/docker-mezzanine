# coding=utf-8

"""Project level settings."""
from .project import *  # noqa
from .secret import SENTRY_DSN

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
# Localhost:9000 for vagrant
# Changes for live site
# ['*'] for testing but not for production

ALLOWED_HOSTS = [
    'localhost:63300',]

# Comment if you are not running behind proxy
USE_X_FORWARDED_HOST = True

# Set debug to false for production
DEBUG = TEMPLATE_DEBUG = False
TESTING = DEBUG

SERVER_EMAIL = 'tim@kartoza.com'
EMAIL_HOST = 'kartoza.com'
DEFAULT_FROM_EMAIL = 'tim@kartoza.com'


STATICFILES_FINDERS += (
    'compressor.finders.CompressorFinder',
)

# Logging
if 'raven.contrib.django.raven_compat' in INSTALLED_APPS:
    # noinspection PyUnresolvedReferences
    import raven  # noqa

    RAVEN_CONFIG = {
        # sentry url
        'dsn': SENTRY_DSN,
        # If you are using git, you can also automatically configure the
        # release based on the git info.
        # Note from Tim: This won't work since we don't mount the root
        # of the git project into the docker container...
        # 'release': raven.fetch_git_sha(os.path.dirname(__file__)),
    }

    MIDDLEWARE_CLASSES = (
        # We recommend putting this as high in the chain as possible
        # see http://raven.readthedocs.org/en/latest/integrations/  ...
        # ... django.html#message-references
        # This will add a client unique id in messages
        'raven.contrib.django.raven_compat.middleware.'
        'SentryResponseErrorIdMiddleware',
    ) + MIDDLEWARE_CLASSES

    # Sentry settings - logs exceptions to a database
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': True,
        'root': {
            'level': 'WARNING',
            'handlers': ['sentry'],
        },
        'formatters': {
            'verbose': {
                'format': '%(levelname)s %(asctime)s %(module)s '
                          '%(process)d %(thread)d %(message)s'
            },
        },
        'handlers': {
            'sentry': {
                'level': 'ERROR',
                'class':
                    'raven.contrib.django.raven_compat.handlers.SentryHandler',
            },
            'console': {
                'level': 'DEBUG',
                'class': 'logging.StreamHandler',
                'formatter': 'verbose'
            }
        },
        'loggers': {
            'django.db.backends': {
                'level': 'ERROR',
                'handlers': ['console'],
                'propagate': False,
            },
            'raven': {
                'level': 'DEBUG',
                'handlers': ['console'],
                'propagate': False,
            },
            'sentry.errors': {
                'level': 'DEBUG',
                'handlers': ['console'],
                'propagate': False,
            },
        },
    }
