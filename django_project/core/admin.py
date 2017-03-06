from copy import deepcopy
from django.contrib import admin
from mezzanine.pages.models import Link
from mezzanine.pages.admin import LinkAdmin

link_fieldsets = deepcopy(LinkAdmin.fieldsets)
link_fieldsets[0][1]["fields"].insert(-2, "is_auth")

class CoreLinkAdmin(LinkAdmin):
    fieldsets = link_fieldsets

admin.site.unregister(Link)
admin.site.register(Link,CoreLinkAdmin)