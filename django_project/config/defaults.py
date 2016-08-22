__author__ = 'Irwan Fathurrahman <irwan@kartoza.com>'
__date__ = '22/08/16'
__license__ = "GPL"
__copyright__ = 'kartoza.com'

from mezzanine.conf import register_setting

# Number of recent post in front page
register_setting(
    name="FRONT_PAGE_RECENT_POST",
    label="Recent posts in front page",
    description="The number of recent posts to show in front page.",
    editable=True,
    default=5,
)

register_setting(
    name="TEMPLATE_ACCESSIBLE_SETTINGS",
    default=("FRONT_PAGE_RECENT_POST",),
    append=True,
)
