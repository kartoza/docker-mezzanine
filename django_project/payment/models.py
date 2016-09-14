__author__ = 'Irwan Fathurrahman <irwan@kartoza.com>'
__date__ = '08/09/16'
__license__ = "GPL"
__copyright__ = 'kartoza.com'
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.db.models import CharField, TextField, FileField
from django.utils.translation import ugettext_lazy as _

from mezzanine.conf import settings
from mezzanine.utils.models import upload_to


@python_2_unicode_compatible
class Payment(models.Model):
    """
    Abstract model representing one of several types of monetary
    reductions, as well as a date range they're applicable for, and
    the products and products in categories that the reduction is
    applicable for.
    """
    order_id = models.IntegerField(_("Order Id"))
    first_name = CharField(_("First name"), max_length=100)
    last_name = CharField(_("Last name"), max_length=100)
    additional_info = TextField(_("Additional Info"), default="", null=True, blank=True)
    additional_document = FileField(verbose_name=_("Additional Document"),
        upload_to=upload_to("payment.file", "document"),
        max_length=255, null=True, blank=True)

    status = models.IntegerField(
        _("Status"),
        choices=settings.SHOP_PAYMENT_STATUS_CHOICES,
        default=settings.SHOP_PAYMENT_STATUS_CHOICES[0][0])

    def __str__(self):
        return "order %d : %s" % (self.order_id, self.first_name)
