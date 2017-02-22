from django import template
from cartridge.shop.models import Category,Product

register = template.Library()

@register.inclusion_tag("shop/list_product.html")
def pinaxcon_list_products(span,count):
    products = Product.objects.filter(available=True)[0:count]
    return {'span':span,'products':products}