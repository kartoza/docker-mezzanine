from django.db import models
from django.db.models import CharField, TextField, IntegerField
from cartridge.shop.models import Product


class ProductViewData(models.Model):
    category_summary = CharField("Category Page Summary", max_length=255)
    category_html = TextField("Category Page HTML")
    product = models.ForeignKey(
        Product,
        related_name='project_images',
    )
    category_button_text = CharField(
        "Category button text",
        max_length=30,
        null=True)
    icon_background_color_hash = (
        CharField("Icon background color as 6 digit code",
                  max_length=6,
                  default='FFFFFF'))

    category_order = IntegerField(
        "Order the item should displayed on the category page", default=0)

    logo_image = models.ImageField(
        blank=True,
        upload_to='product_image',
        help_text="An image used as this product's logo",
        null=True
    )

    def __unicode__(self):
        return unicode(self.product.title)

    class Meta:
        verbose_name_plural = 'Product View Data'

    def __getitem__(self, item):
        return getattr(self, item)
