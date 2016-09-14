__author__ = 'Irwan Fathurrahman <irwan@kartoza.com>'
__date__ = '08/09/16'
__license__ = "GPL"
__copyright__ = 'kartoza.com'

from django.contrib import admin
from django.contrib.admin.templatetags.admin_static import static
from django.utils.translation import ugettext_lazy as _

from payment.models import Payment

payment_list_display = ("order_id", "first_name", "status",)


class PaymentAdmin(admin.ModelAdmin):
    class Media:
        css = {"all": (static("cartridge/css/admin/order.css"),)}

    ordering = ("status", "-order_id")
    list_display = payment_list_display
    list_editable = ("status",)
    list_filter = ("status",)
    search_fields = (["order_id", "first_name"])
    radio_fields = {"status": admin.HORIZONTAL}
    fieldsets = (
        (None, {"fields": ("order_id",)}),
        (_("Payment Information"),
         {"fields": ("first_name", "last_name", "status", "additional_info", "additional_document")}),
    )


admin.site.register(Payment, PaymentAdmin)
