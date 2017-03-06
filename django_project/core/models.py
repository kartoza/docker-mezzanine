from django.utils.translation import ugettext_lazy as _
from mezzanine.pages.models import Link
from django.utils.translation import ugettext_lazy as _
from django.db import models

import logging

logger = logging.getLogger(__name__)


class AuthLink(Link):
    """Page bucket for media files."""
    is_auth = models.BooleanField(_("Use Authentication"),default=False)
    class Meta:
        verbose_name = _("Link Authentication")
        verbose_name_plural = _("Link Authentications")
