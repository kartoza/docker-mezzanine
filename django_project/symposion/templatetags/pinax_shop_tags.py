from __future__ import unicode_literals
from future.builtins import str

from decimal import Decimal
import locale
import platform

from django import template

from cartridge.shop.templatetags.shop_tags import _order_totals

register = template.Library()


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