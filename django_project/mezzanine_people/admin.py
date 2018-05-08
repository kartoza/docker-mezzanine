
from copy import deepcopy

from django.contrib import admin

from .models import Person, PersonLink, PersonCategory
from mezzanine.conf import settings
from mezzanine.core.admin import DisplayableAdmin


person_fieldsets = deepcopy(DisplayableAdmin.fieldsets)
person_fieldsets[0][1]["fields"].insert(1, "categories")
person_list_display = ["title", "status", "admin_link"]
person_fieldsets[0][1]["fields"].extend(["first_name", "last_name", "job_title",
                                         "mugshot", "mugshot_hover", "mugshot_credit", "bio", "email",
                                         "order"])
person_list_display.insert(0, "admin_thumb")


class PersonLinkInline(admin.TabularInline):
    model = PersonLink

class PersonAdmin(DisplayableAdmin):
    """
    Admin class for people.
    """

    fieldsets = person_fieldsets
    list_display = person_list_display
    filter_horizontal = ("categories",)
    inlines = [
        PersonLinkInline,
    ]

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
