from django.db import models
from django.utils.translation import ugettext_lazy as _
from mezzanine.core.fields import RichTextField, FileField
from mezzanine.core.models import Displayable, RichText, Slugged
from mezzanine.utils.models import AdminThumbMixin

__author__ = 'Dimas Ciputra <dimas@kartoza.com>'
__date__ = '07/09/16'


class Client(Displayable, RichText, AdminThumbMixin):
    """A client model"""
    name = models.CharField(
        help_text=_('Name of the client.'),
        max_length=255,
        null=False,
        blank=False,
    )

    link = models.URLField(
        help_text=_('Client company site link'),
        max_length=255,
        blank=False,
        null=False,
    )

    logo = FileField(
        verbose_name=_("Client logo image"),
        upload_to="client",
        format="Image",
        max_length=255,
        null=False
    )

    class Meta:
        """Meta class for client."""
        verbose_name = _("Clients")
        verbose_name_plural = _("Client")
        ordering = ("name", "link", "logo", "description")

    @models.permalink
    def get_absolute_url(self):
        return "client_detail", (), {"slug": self.slug}
