from mezzanine.core.models import ContentTyped
from mezzanine.pages.models import Page
from django.utils.translation import ugettext_lazy as _
from django.db import models

import logging

logger = logging.getLogger(__name__)


class AuthLink(Page):
    """Page bucket for media files."""
    # is_auth = models.BooleanField(_("Use Authentication"),default=False)
    show_before_login = models.BooleanField(_("Show Before Login"),default=True)
    show_after_login = models.BooleanField(_("Show After Login"), default=True)
    class Meta:
        verbose_name = _("Link Authentication")
        verbose_name_plural = _("Link Authentications")
