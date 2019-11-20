from django.db import models
from django.db.models import CharField, TextField
from cartridge.shop.models import Product


class ProductViewData(models.Model):
    category_summary = CharField("Category Page Summary", max_length=255)
    category_html = TextField("Category Page HTML")
    product = models.ForeignKey(
        Product,
        related_name='project_images',
    )
