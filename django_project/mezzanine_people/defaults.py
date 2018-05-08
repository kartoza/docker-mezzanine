"""
Default settings for the ``mezzanine_people`` app. Each of these can be
overridden in your project's settings module, just like regular
Django settings. The ``editable`` argument for each controls whether
the setting is editable via Django's admin.

Thought should be given to how a setting is actually used before
making it editable, as it may be inappropriate - for example settings
that are only read during startup shouldn't be editable, since changing
them would require an application reload.
"""

from django.utils.translation import ugettext_lazy as _

from mezzanine.conf import register_setting


register_setting(
    name="PEOPLE_PER_PAGE",
    label=_("People per page"),
    description=_("Max number of people shown on a people listing page."),
    editable=True,
    default=10,
)
