from copy import deepcopy
from django.contrib import admin
from mezzanine.pages.models import Link
from mezzanine.pages.admin import LinkAdmin
from models import AuthLink

link_fieldsets = deepcopy(LinkAdmin.fieldsets)
link_fieldsets[0][1]["fields"].insert(-2, "show_before_login")
link_fieldsets[0][1]["fields"].insert(-3, "show_after_login")

class CoreLinkAdmin(LinkAdmin):
    fieldsets = link_fieldsets

admin.site.unregister(Link)
admin.site.register(AuthLink,CoreLinkAdmin)