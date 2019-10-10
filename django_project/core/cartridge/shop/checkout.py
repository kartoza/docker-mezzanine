from __future__ import division, unicode_literals
from cartridge.shop.utils import set_tax
from mezzanine.utils.email import send_mail_template
from django.contrib.messages import info
from django.core.urlresolvers import reverse
from django.template.loader import get_template, TemplateDoesNotExist
from django.shortcuts import  redirect
from django.utils.translation import ugettext as _
from mezzanine.conf import settings
from mezzanine.utils.urls import next_url



__author__ = 'Irwan Fathurrahman <irwan@kartoza.com>'
__date__ = '09/09/16'
__license__ = "GPL"
__copyright__ = 'kartoza.com'

import decimal
from django.utils.translation import ugettext_lazy as _

# TODO : fix this
# tax_value = str(getattr(settings, "CURRENT_VAT", 15)) + "%"
tax_value = '15%'

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
    tax = request.cart.total_price() - (request.cart.total_price() / decimal.Decimal(1 + float(tax_value.strip('%'))/100))
    set_tax(request, _("Vat"), tax)


def order_handler(request, order_form, order):
    """
    Custom order handler to improve control over BCC emails
    """

    if request.method == "POST":

        send_order_email_bcc(request, order)
        msg = _("The order email for order ID %s has been sent") % order.pk
        info(request, msg)
        # Determine the URL to return the user to.
    redirect_to = next_url(request)
    if redirect_to is None:
        if request.user.is_staff:
            redirect_to = reverse("admin:shop_order_change", args=[order.pk])
        else:
            redirect_to = reverse("shop_order_history")
    return redirect(redirect_to)


def send_order_email_bcc(request, order):
    """
    Send order receipt email on successful order.
    """
    settings.use_editable()
    order_context = {"order": order, "request": request,
                     "order_items": order.items.all()}
    order_context.update(order.details_as_dict())
    try:
        get_template("shop/includes/order_details.html")
    except TemplateDoesNotExist:
        receipt_template = "email/order_receipt"
    else:
        receipt_template = "shop/includes/order_details"
        from warnings import warn
        warn("Shop email receipt templates have moved from "
             "templates/shop/email/ to templates/email/")
    order_email_bcc_list = str(settings.SHOP_ORDER_EMAIL_BCC).split(',')
    for email in order_email_bcc_list:
        send_mail_template(settings.SHOP_ORDER_EMAIL_SUBJECT,
                           receipt_template, settings.SHOP_ORDER_FROM_EMAIL,
                           email,
                           context=order_context,
                           addr_bcc=None)


