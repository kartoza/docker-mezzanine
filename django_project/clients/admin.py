from copy import deepcopy

from django.contrib import admin
from .models import Client
from mezzanine.core.admin import DisplayableAdmin

__author__ = 'Dimas Ciputra <dimas@kartoza.com>'
__date__ = '07/09/16'

client_fieldsets = deepcopy(DisplayableAdmin.fieldsets)
client_fieldsets[0][1]["fields"].extend([
    "link", "logo"
])
client_list_display = ["title", "status", "admin_link"]


class ClientAdmin(DisplayableAdmin):
    """
    Admin class for client
    """
    fieldsets = client_fieldsets
    list_display = client_list_display

admin.site.register(Client, ClientAdmin)
