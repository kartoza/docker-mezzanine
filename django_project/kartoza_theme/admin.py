from django.contrib import admin
from kartoza_theme.models import ProductViewData
# Register your models here.


class ProductViewDataAdmin(admin.ModelAdmin):
    """
    Admin class for project categories. Hides itself from the admin menu
    unless explicitly specified.
    """

    fieldsets = ((None, {"fields": ("category_summary",)}),)


admin.site.register(ProductViewData, ProductViewDataAdmin)