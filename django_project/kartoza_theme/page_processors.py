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
    sorted_view_data = ProductViewData.objects.filter(
        product__in=category.product_set.all()).order_by('category_order')
    return {"view_data": sorted_view_data}
