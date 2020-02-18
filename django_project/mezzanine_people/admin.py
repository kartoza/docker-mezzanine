from copy import deepcopy

from django.contrib import admin
from core.admin import OSMGeoAdminSecure

from .models import Person, PersonLink, PersonCategory, Office
from mezzanine.conf import settings
from mezzanine.core.admin import DisplayableAdmin

person_fieldsets = deepcopy(DisplayableAdmin.fieldsets)
person_fieldsets[0][1]["fields"].insert(1, "categories")
person_list_display = ["order", "title", "status", "admin_link"]
person_fieldsets[0][1]["fields"].extend(["first_name", "last_name", "job_title",
                                         "mugshot", "mugshot_hover", "mugshot_credit", "bio", "email",
                                         "user", "location", "order"])
person_list_display.insert(1, "admin_thumb")


class PersonLinkInline(admin.TabularInline):
    model = PersonLink


class PersonAdmin(OSMGeoAdminSecure, DisplayableAdmin):
    """
    Admin class for people.
    """

    fieldsets = person_fieldsets
    list_display = person_list_display
    filter_horizontal = ("categories",)
    inlines = [
        PersonLinkInline,
    ]
    list_editable = ("order",)


class PersonCategoryAdmin(admin.ModelAdmin):
    """
    Admin class for people categories. Hides itself from the admin menu
    unless explicitly specified.
    """

    fieldsets = ((None, {"fields": ("title",)}),)

    def in_menu(self):
        """
        Hide from the admin menu unless explicitly set in ``ADMIN_MENU_ORDER``.
        """
        for (name, items) in settings.ADMIN_MENU_ORDER:
            if "people.PersonCategory" in items:
                return True
        return False


admin.site.register(Person, PersonAdmin)
admin.site.register(PersonCategory, PersonCategoryAdmin)

# OFFICE
office_fieldsets = deepcopy(DisplayableAdmin.fieldsets)
office_list_display = ["order", "title", "status", "telephone"]
office_fieldsets[0][1]["fields"].extend(
    ["address", "telephone", "email", "location", "users", "order"])


class OfficeAdmin(OSMGeoAdminSecure, DisplayableAdmin):
    """
    Admin class for office.
    """

    fieldsets = office_fieldsets
    list_display = office_list_display
    filter_horizontal = ("users",)
    list_editable = ("order",)


admin.site.register(Office, OfficeAdmin)
