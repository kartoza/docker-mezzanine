from django.contrib import admin

import reversion

from symposion.teams.models import Team, Membership

class TeamAdmin(admin.ModelAdmin):

    class Media:
        css = {'all': ('/static/admin/css/widgets.css',)}

    prepopulated_fields = {"slug": ("name",)}
    filter_vertical = ('permissions', 'manager_permissions',)

admin.site.register(Team, TeamAdmin)


class MembershipAdmin(reversion.VersionAdmin):
    list_display = ["team", "user", "state"]
    list_filter = ["team"]
    search_fields = ["user__username"]

admin.site.register(Membership, MembershipAdmin)
