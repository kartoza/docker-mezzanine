from __future__ import unicode_literals
from future.builtins import str

from decimal import Decimal
from datetime import datetime
import locale
import platform

from django import template

from cartridge.shop.utils import set_locale
from mezzanine.conf import settings
from core.cartridge.shop.checkout import tax_value

register = template.Library()


@register.filter
def currency(value):
    """
    Format a value as currency according to locale.
    """
    set_locale()
    if not value:
        value = 0
    value = locale.currency(Decimal(value), grouping=True)
    if platform.system() == 'Windows':
        try:
            value = str(value, encoding=locale.getpreferredencoding())
        except TypeError:
            pass
    return value


def _order_totals(context):
    """
    Add shipping/tax/discount/order types and totals to the template
    context. Use the context's completed order object for email
    receipts, or the cart object for checkout.
    """
    fields = ["shipping_type", "shipping_total", "discount_total",
              "tax_type", "tax_total"]
    template_vars = {}
    global tax_value

    if "order" in context:
        for field in fields + ["item_total", "total"]:
            template_vars[field] = getattr(context["order"], field)
        template_vars["order_total"] = template_vars.get("total", None)
        if template_vars.get("discount_total", None) is not None:
            template_vars["order_total_before_discount"] = template_vars["order_total"] + Decimal(
                str(template_vars["discount_total"]))
        # checks whether a current VAT takes into effect after the transaction date
        # if so, replace tax_value with old vat value
        trans_date = context["order"].time.date()
        new_vat_applied = datetime.strptime(getattr(settings,  "CURRENT_VAT_STARTED"), "%d/%m/%Y").date()
        if trans_date < new_vat_applied:
            tax_value = str(getattr(settings, "OLD_VAT")) + "%"
    else:
        template_vars["item_total"] = context["request"].cart.total_price()
        if template_vars["item_total"] == 0:
            # Ignore session if cart has no items, as cart may have
            # expired sooner than the session.
            template_vars["tax_total"] = 0
            template_vars["discount_total"] = 0
            template_vars["shipping_total"] = 0
        else:
            for field in fields:
                template_vars[field] = context["request"].session.get(
                    field, None)

    template_vars["order_total"] = template_vars.get("item_total", None)
    # checking tax total
    if template_vars.get("tax_total", None) is not None:
        try:
            if "%" in tax_value:
                template_vars["tax_type"] += " (" + tax_value + ") "
        except TypeError:
            pass

        if not settings.SHOP_HANDLER_TAX_INCLUDE_IN_PRICE:
            template_vars["order_total"] += Decimal(
                str(template_vars["tax_total"]))
        else:
            template_vars["item_total"] -= Decimal(
                str(template_vars["tax_total"]))

    if template_vars.get("shipping_total", None) is not None:
        template_vars["order_total"] += Decimal(
            str(template_vars["shipping_total"]))

    if template_vars.get("discount_total", None) is not None:
        template_vars["order_total"] -= Decimal(
            str(template_vars["discount_total"]))
    return template_vars


@register.inclusion_tag("shop/includes/order_totals.html", takes_context=True)
def order_totals(context):
    """
    HTML version of order_totals.
    """
    return _order_totals(context)


@register.inclusion_tag("shop/includes/order_totals_in_table.html", takes_context=True)
def order_totals_in_table(context):
    """
    HTML version of order_totals.
    """
    return _order_totals(context)


@register.inclusion_tag("shop/includes/order_totals.txt", takes_context=True)
def order_totals_text(context):
    """
    Text version of order_totals.
    """
    return _order_totals(context)
