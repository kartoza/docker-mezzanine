import operator
from django import forms
from collections import OrderedDict
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect
from mezzanine.pages.page_processors import processor_for
from mezzanine.pages.models import Page
from cartridge.shop.models import Category
from .models import ProductViewData


@processor_for(Category)
def product_view_data(request, page, *args, **kwargs):
    category = Category.objects.get(pk=page.id)
    view_data = {}
    for product in category.product_set.all():
        try:
            product_view_data = ProductViewData.objects.filter(product=product).first()
            if product_view_data:
                view_data[product.id] = product_view_data
        except ObjectDoesNotExist:
            pass
    sorted_view_data = OrderedDict(
        sorted(view_data.iteritems(), key=lambda x: x[1]['category_order'], reverse=False))

    return {"view_data": sorted_view_data}
