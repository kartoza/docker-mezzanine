from django.contrib import admin
from django.conf import settings
from django import forms
from django.forms import ModelForm
from kartoza_project.models import (
    Project,
    ProjectImage,
    Reference,
    ProjectCategory,
    Person,
    Role,
)


class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 3
    verbose_name_plural = 'Project images/screenshots'
    readonly_fields = ['admin_thumb', ]
    fields = ['admin_thumb', 'image', 'caption']


class ReferenceStackedInline(admin.StackedInline):
    model = Reference
    extra = 1


class ProjectAdminForm(ModelForm):
    _order = forms.IntegerField(required=False)

    class Meta:
        model = Project
        exclude = []


class ProjectAdmin(admin.ModelAdmin):
    """
    Admin class for project
    """
    list_display = ['admin_thumb', 'title', 'short_description', 'date_start', 'date_end', '_order']
    list_display_links = ['title', ]
    inlines = [ProjectImageInline, ReferenceStackedInline]
    form = ProjectAdminForm

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ('slug', 'categories')
        return ()

    def get_prepopulated_fields(self, request, obj=None):
        if not obj:
            return {'slug': ('title',)}
        return {}


class ProjectCategoryAdmin(admin.ModelAdmin):
    """
    Admin class for project categories. Hides itself from the admin menu
    unless explicitly specified.
    """

    fieldsets = ((None, {"fields": ("title",)}),)

    def in_menu(self):
        """
        Hide from the admin menu unless explicitly set in ``ADMIN_MENU_ORDER``.
        """
        for (name, items) in settings.ADMIN_MENU_ORDER:
            if "kartoza_project.PersonCategory" in items:
                return True
        return False


class ReferenceAdmin(admin.ModelAdmin):
    """
       Admin class for project reference. Hides itself from the admin menu
       unless explicitly specified.
       """

    fieldsets = ((None, {"fields": ('person', 'role_relation',)}),)


class PersonAdmin(admin.ModelAdmin):
    fieldsets = ((None, {"fields": ('name', 'url', 'description', 'email', 'telephone', 'title')}),)


class RoleAdmin(admin.ModelAdmin):
    fieldsets = ((None, {"fields": ('name', 'description')}),)


admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectCategory, ProjectCategoryAdmin)
admin.site.register(Reference, ReferenceAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(Role, RoleAdmin)
