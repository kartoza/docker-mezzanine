from mezzanine.conf import settings
from cartridge.shop.utils import set_tax

__author__ = 'Irwan Fathurrahman <irwan@kartoza.com>'
__date__ = '09/09/16'
__license__ = "GPL"
__copyright__ = 'kartoza.com'

import decimal
from django.utils.translation import ugettext_lazy as _

tax_value = "0%"


def vat_tax_handler(request, order_form):
    """
    Default tax handler - called immediately after the handler defined
    by ``SHOP_HANDLER_BILLING_SHIPPING``. Implement your own and
    specify the path to import it from via the setting
    ``SHOP_HANDLER_TAX``. This function will typically contain any tax
    calculation where the tax amount can then be set using the function
    ``cartridge.shop.utils.set_tax``. The Cart object is also
    accessible via ``request.cart``
    """
    settings.use_editable()
    tax = 0
    # set_tax(request, _("Vat"), tax)
