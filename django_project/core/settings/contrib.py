# coding=utf-8
"""
core.settings.contrib
"""
from .base import *  # noqa
from .secret import (
    COMMENTS_DISQUS_API_PUBLIC_KEY,
    COMMENTS_DISQUS_API_SECRET_KEY,
    COMMENTS_DISQUS_SHORTNAME)

# Store these package names here as they may change in the future since
# at the moment we are using custom forks of them.
PACKAGE_NAME_FILEBROWSER = "filebrowser_safe"
PACKAGE_NAME_GRAPPELLI = "grappelli_safe"
GRAPPELLI_INSTALLED = True

# Extra installed apps - grapelli needs to be added before others
INSTALLED_APPS += (
     PACKAGE_NAME_GRAPPELLI,
     "config",
     "kartoza_theme",
     "mezzanine",
     "django_comments",
     "compressor",
     PACKAGE_NAME_FILEBROWSER,
     "mezzanine.boot",
     "mezzanine.conf",
     "mezzanine.core",
     "mezzanine.generic",
     "mezzanine.blog",
     "mezzanine.forms",
     "mezzanine.pages",
     "mezzanine.galleries",
     "mezzanine.twitter",
     #"mezzanine.accounts",
     #"mezzanine.mobile",
     # Extra apps picked out by Tim
     "mezzanine_people",
     "mezzanine_references",
     "mdown",  # markdown support in admin
     "mezzanine_agenda",  # we use a local copy as pip misses migrations
     "careers",
)

# mezzanine-mdown options
# RICHTEXT_WIDGET_CLASS = "mdown.forms.WmdWidget"
# RICHTEXT_FILTER = "mdown.filters.codehilite"

MIGRATION_MODULES = {'accounts': 'core.migration'}

GRAPPELLI_ADMIN_TITLE = 'Site administration panel'

PEOPLE_PER_PAGE = 20

EVENT_USE_FEATURED_IMAGE = True
# This one must occur before django provided middleware
MIDDLEWARE_CLASSES = (
    "mezzanine.core.middleware.UpdateCacheMiddleware",
) + MIDDLEWARE_CLASSES
# And these after django provided middleware
MIDDLEWARE_CLASSES += (
    "mezzanine.core.request.CurrentRequestMiddleware",
    "mezzanine.core.middleware.RedirectFallbackMiddleware",
    "mezzanine.core.middleware.TemplateForDeviceMiddleware",
    "mezzanine.core.middleware.TemplateForHostMiddleware",
    "mezzanine.core.middleware.AdminLoginInterfaceSelectorMiddleware",
    "mezzanine.core.middleware.SitePermissionMiddleware",
    # Uncomment the following if using any of the SSL settings:
    # "mezzanine.core.middleware.SSLRedirectMiddleware",
    "mezzanine.pages.middleware.PageMiddleware",
    "mezzanine.core.middleware.FetchFromCacheMiddleware",
)

AUTHENTICATION_BACKENDS = ("mezzanine.core.auth_backends.MezzanineBackend",)

ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = True
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_SIGNUP_FORM_CLASS = 'base.forms.SignupForm'
ACCOUNT_AUTHENTICATION_METHOD = 'username_email'

######################
# Mezzanine agenda settings : https://github.com/jpells/mezzanine-agenda
######################

EVENT_SLUG = u"events"


######################
# MEZZANINE SETTINGS #
######################

COMMENT_FORM_CLASS = 'mezzanine.generic.forms.ThreadedCommentForm'

# Whether a user's session cookie expires when the Web browser is closed.
SESSION_EXPIRE_AT_BROWSER_CLOSE = True

# List of processors used by RequestContext to populate the context.
# Each one should be a callable that takes the request object as its
# only parameter and returns a dictionary to add to the context.
# Implemented in base.py as a dirty hack for now
#TEMPLATE_CONTEXT_PROCESSORS = (
#)

# The following settings are already defined with default values in
# the ``defaults.py`` module within each of Mezzanine's apps, but are
# common enough to be put here, commented out, for convenient
# overriding. Please consult the settings documentation for a full list
# of settings Mezzanine implements:
# http://mezzanine.jupo.org/docs/configuration.html#default-settings

# Controls the ordering and grouping of the admin menu.
#
ADMIN_MENU_ORDER = (
    ("Content", ("pages.Page", "blog.BlogPost",
       "generic.ThreadedComment", ("Media Library", "fb_browse"),)),
    ("Site", ("sites.Site", "redirects.Redirect", "conf.Setting")),
    ("Users", ("auth.User", "auth.Group",)),
)

# A three item sequence, each containing a sequence of template tags
# used to render the admin dashboard.
#
DASHBOARD_TAGS = (
    ("blog_tags.quick_blog", "mezzanine_tags.app_list"),
    ("comment_tags.recent_comments",),
    ("mezzanine_tags.recent_actions",),
)

# A sequence of templates used by the ``page_menu`` template tag. Each
# item in the sequence is a three item sequence, containing a unique ID
# for the template, a label for the template, and the template path.
# These templates are then available for selection when editing which
# menus a page should appear in. Note that if a menu template is used
# that doesn't appear in this setting, all pages will appear in it.

PAGE_MENU_TEMPLATES = (
    (1, "Top navigation bar", "pages/menus/dropdown.html"),
    (2, "Left-hand tree", "pages/menus/tree.html"),
    (3, "Footer", "pages/menus/footer.html"),
)

# A sequence of fields that will be injected into Mezzanine's (or any
# library's) models. Each item in the sequence is a four item sequence.
# The first two items are the dotted path to the model and its field
# name to be added, and the dotted path to the field class to use for
# the field. The third and fourth items are a sequence of positional
# args and a dictionary of keyword args, to use when creating the
# field instance. When specifying the field class, the path
# ``django.models.db.`` can be omitted for regular Django model fields.
#
# EXTRA_MODEL_FIELDS = (
#     (
#         # Dotted path to field.
#         "mezzanine.blog.models.BlogPost.image",
#         # Dotted path to field class.
#         "somelib.fields.ImageField",
#         # Positional args for field class.
#         ("Image",),
#         # Keyword args for field class.
#         {"blank": True, "upload_to": "blog"},
#     ),
#     # Example of adding a field to *all* of Mezzanine's content types:
#     (
#         "mezzanine.pages.models.Page.another_field",
#         "IntegerField", # 'django.db.models.' is implied if path is omitted.
#         ("Another name",),
#         {"blank": True, "default": 1},
#     ),
# )

# Setting to turn on featured images for blog posts. Defaults to False.
#
# BLOG_USE_FEATURED_IMAGE = True


####################
# MEZZANINE DYNAMIC SETTINGS #
####################

# set_dynamic_settings() will rewrite globals based on what has been
# defined so far, in order to provide some better defaults where
# applicable. We also allow this settings module to be imported
# without Mezzanine installed, as the case may be when using the
# fabfile, where setting the dynamic settings below isn't strictly
# required.
#try:
##    from mezzanine.utils.conf import set_dynamic_settings
#except ImportError:
#    pass
#else:
#    set_dynamic_settings(globals())

####################
# MEZZANINE CAREERS SETTINGS #
####################

CAREERS_PER_PAGE = 5

####################
# SEARCH BOX SETTINGS #
####################

SEARCH_MODEL_CHOICES = (
    'pages.Page',
    'blog.BlogPost',
    'mezzanine_people.Person',
    'careers.JobPost',
)
