from django.contrib import admin
from kartoza_theme.models import ProductViewData
# Register your models here.


class ProductViewDataAdmin(admin.ModelAdmin):
    """
    Admin class for project categories. Hides itself from the admin menu
    unless explicitly specified.
    """

    fieldsets = ((None, {"fields": ("category_summary", "category_html",
                                    "product", "category_button_text",
                                    "icon_background_color_hash",
                                    "category_order", "logo_image")}),)


admin.site.register(ProductViewData, ProductViewDataAdmin)
