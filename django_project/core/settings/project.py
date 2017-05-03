# coding=utf-8

"""Project level settings.

Adjust these values as needed but don't commit passwords etc. to any public
repository!
"""

import os  # noqa
from django.utils.translation import ugettext_lazy as _
from .utils import absolute_path
from .contrib import *  # noqa

# Project apps
INSTALLED_APPS += (
    # Add any additional project apps here
    # symposion
    "symposion",
    "symposion.conference",
    "symposion.proposals",
    "symposion.reviews",
    "symposion.schedule",
    "symposion.speakers",
    "symposion.sponsorship",
    "symposion.teams",
    "proposals",
    "payment",
    "pinaxcon_theme",
)

# Due to profile page does not available,
# this will redirect to home page after login
LOGIN_REDIRECT_URL = '/'

# How many versions to list in each project box
PROJECT_VERSION_LIST_SIZE = 10

# Set debug to false for production
DEBUG = TEMPLATE_DEBUG = False

SOUTH_TESTS_MIGRATE = False


# Set languages which want to be translated
LANGUAGES = (
    ('en', _('English')),
    ('af', _('Afrikaans')),
    ('id', _('Indonesian')),
    ('ko', _('Korean')),
)

# Set storage path for the translation files
LOCALE_PATHS = (absolute_path('locale'),)


MIDDLEWARE_CLASSES = (
    # Add any additional middleware classes here
) + MIDDLEWARE_CLASSES

DATABASES = {}

####################
# DYNAMIC SETTINGS #
####################

# set_dynamic_settings() will rewrite globals based on what has been
# defined so far, in order to provide some better defaults where
# applicable. We also allow this settings module to be imported
# without Mezzanine installed, as the case may be when using the
# fabfile, where setting the dynamic settings below isn't strictly
# required.
try:
    from mezzanine.utils.conf import set_dynamic_settings
except ImportError:
    pass
else:
    set_dynamic_settings(globals())

from .celery_setting import *  # noqa

CONFERENCE_ID=2
PROPOSAL_FORMS = {
    "talk": "proposals.forms.TalkProposalForm",
    "workshop": "proposals.forms.WorkshopProposalForm",
    "map": "proposals.forms.MapProposalForm",
    "academic-presentation" : "proposals.forms.TalkProposalForm",
    "sagta-workshops" : "proposals.forms.WorkshopProposalForm",
    "foss4g-general-presentation" : "proposals.forms.TalkProposalForm",
    "foss4g-workshops" : "proposals.forms.WorkshopProposalForm",
    "sagta-general-presentation" : "proposals.forms.TalkProposalForm",
}

# FIXTURE_DIRS = (
#     absolute_path("symposion","fixtures"),
# )

SHOP_CURRENCY_LOCALE = "en_ZA.UTF-8"

ACCOUNT_HOOKSET = "core.adapter.PinaxAccountHookset"
CONFERENCE_DOMAIN = "https://foss4g-africa.org"

LOGIN_URL = '/account/login/'