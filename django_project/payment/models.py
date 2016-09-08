__author__ = 'Irwan Fathurrahman <irwan@kartoza.com>'
__date__ = '08/09/16'
__license__ = "GPL"
__copyright__ = 'kartoza.com'
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.db.models import CharField, TextField
from django.utils.translation import ugettext_lazy as _

from mezzanine.conf import settings


@python_2_unicode_compatible
class Payment(models.Model):
    """
    Abstract model representing one of several types of monetary
    reductions, as well as a date range they're applicable for, and
    the products and products in categories that the reduction is
    applicable for.
    """
    order_id = models.IntegerField(_("Order Id"))

    bank_name = CharField(_("Bank Name"), max_length=100)
    bank_account = models.CharField(_("Bank Account"), max_length=100)
    first_name = CharField(_("First name"), max_length=100)
    last_name = CharField(_("Last name"), max_length=100)
    additional_info = TextField(_("Additional Info"), default="", null=True, blank=True)

    status = models.IntegerField(
        _("Status"),
        choices=settings.SHOP_PAYMENT_STATUS_CHOICES,
        default=settings.SHOP_PAYMENT_STATUS_CHOICES[0][0])

    def __str__(self):
        return "order %d : %s" % (self.order_id, self.first_name)
