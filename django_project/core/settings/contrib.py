# coding=utf-8
"""
core.settings.contrib
"""
from .base import *  # noqa
import locale
from .secret import (
    COMMENTS_DISQUS_API_PUBLIC_KEY,
    COMMENTS_DISQUS_API_SECRET_KEY,
    SOCIAL_AUTH_GITHUB_KEY,
    SOCIAL_AUTH_GITHUB_SECRET,
    COMMENTS_DISQUS_SHORTNAME)

# Store these package names here as they may change in the future since
# at the moment we are using custom forks of them.
PACKAGE_NAME_FILEBROWSER = "filebrowser_safe"
PACKAGE_NAME_GRAPPELLI = "grappelli_safe"
GRAPPELLI_INSTALLED = True

# Extra installed apps - grapelli needs to be added before others
INSTALLED_APPS += (
     # 'raven.contrib.django.raven_compat',  # enable Raven plugin
     PACKAGE_NAME_GRAPPELLI,
     "config",
     "flat_theme",
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
     "mezzanine_references",
     "mezzanine_slides",
     "mdown",  # markdown support in admin
     "mezzanine_agenda",  # we use a local copy as pip misses migrations
     # theme
     "bootstrapform",
     "easy_thumbnails",
     "taggit",
     "reversion",
     "metron",
     "sitetree",
     "pinax_theme_bootstrap",
     "pinax.boxes",
     "account",
     "cartridge.shop",
     "qgis_mezzanine_model",
     "social_django",
     "social_core",

)

MARKDOWNIFY_WHITELIST_TAGS = [
    'a',
    'abbr',
    'acronym',
    'b',
    'blockquote',
    'em',
    'i',
    'li',
    'ol',
    'p',
    'strong',
    'ul'
]

ACCOUNT_OPEN_SIGNUP = True
ACCOUNT_EMAIL_UNIQUE = True
ACCOUNT_EMAIL_CONFIRMATION_REQUIRED = False
ACCOUNT_SIGNUP_REDIRECT_URL = "dashboard"
ACCOUNT_LOGIN_REDIRECT_URL = "dashboard"
ACCOUNT_LOGOUT_REDIRECT_URL = "home"
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 2
ACCOUNT_USE_AUTH_AUTHENTICATE = True
HOOKSET = "pinaxcon_theme.hooks.Foss4GAccountHookset"


AUTHENTICATION_BACKENDS = [
    "account.auth_backends.UsernameAuthenticationBackend",
]
# mezzanine-mdown options
# RICHTEXT_WIDGET_CLASS = "mdown.forms.WmdWidget"
# RICHTEXT_FILTER = "mdown.filters.codehilite"

MIGRATION_MODULES = {'accounts': 'core.migration'}

GRAPPELLI_ADMIN_TITLE = 'Site administration panel'

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
    "cartridge.shop.middleware.ShopMiddleware",
    "mezzanine.pages.middleware.PageMiddleware",
    "mezzanine.core.middleware.FetchFromCacheMiddleware",
)

AUTHENTICATION_BACKENDS = (
    "mezzanine.core.auth_backends.MezzanineBackend",
    "social_core.backends.github.GithubOAuth2",
)


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
# TEMPLATE_CONTEXT_PROCESSORS = (
# )

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

# Front-end inline editing
# Set false for now, because this causing layout error
INLINE_EDITING_ENABLED = False

####################
# MEZZANINE DYNAMIC SETTINGS #
####################

# set_dynamic_settings() will rewrite globals based on what has been
# defined so far, in order to provide some better defaults where
# applicable. We also allow this settings module to be imported
# without Mezzanine installed, as the case may be when using the
# fabfile, where setting the dynamic settings below isn't strictly
# required.
# try:
##    from mezzanine.utils.conf import set_dynamic_settings
# except ImportError:
#    pass
# else:
#    set_dynamic_settings(globals())

####################
# SEARCH BOX SETTINGS #
####################

SEARCH_MODEL_CHOICES = (
    'pages.Page',
    'blog.BlogPost',
)

####################
# FILEBROWSER ALLOWED EXTENSIONS #
####################
FILEBROWSER_EXTENSIONS = {
    'Folder': [''],
    'Image': ['.jpg', '.jpeg', '.gif', '.png', '.tif', '.tiff'],
    'Video': ['.mov', '.wmv', '.mpeg', '.mpg', '.avi', '.rm'],
    'Document': ['.pdf', '.doc', '.rtf', '.txt', '.xls', '.csv', 'zip', 'tar.gz', 'rar'],
    'Audio': ['.mp3', '.mp4', '.wav', '.aiff', '.midi', '.m4p', '.ogg'],
    'Code': ['.html', '.py', '.js', '.css']
}
# We don't want to have dead connections stored on rabbitmq
# BROKER_HEARTBEAT = '?heartbeat=30'
# BROKER_URL += BROKER_HEARTBEAT

BROKER_URL = 'amqp://guest:guest@%s:5672//' % 'rabbitmq'

CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

######################
# CARTRIDGE (ecommerce platform for mezzanine) SETTINGS #
######################

# Cartridge uses locale to determine the number of decimal places for the
# currency. Unfortunately python does not seem to pick up our system
# locale well so we set it here. If you need to change to another locale
# please also see Dockerfile in deployment/docker as it sets up the local
# for en_ZA and you will need to adjust that before your chosen locale works
locale.setlocale(locale.LC_ALL, 'en_ZA.UTF-8')
# The following settings are already defined in cartridge.shop.defaults
# with default values, but are common enough to be put here, commented
# out, for conveniently overriding. Please consult the settings
# documentation for a full list of settings Cartridge implements:
# http://cartridge.jupo.org/configuration.html#default-settings

# Sequence of available credit card types for payment.
SHOP_CARD_TYPES = ("Mastercard", "Visa",)

# Setting to turn on featured images for shop categories. Defaults to False.
# SHOP_CATEGORY_USE_FEATURED_IMAGE = True

# Set an alternative OrderForm class for the checkout process.
# SHOP_CHECKOUT_FORM_CLASS = 'cartridge.shop.forms.OrderForm'

# If True, the checkout process is split into separate
# billing/shipping and payment steps.
# SHOP_CHECKOUT_STEPS_SPLIT = True

# If True, the checkout process has a final confirmation step before
# completion.
SHOP_CHECKOUT_STEPS_CONFIRMATION = True

# Controls the formatting of monetary values accord to the locale
# module in the python standard library. If an empty string is
# used, will fall back to the system's locale.
SHOP_CURRENCY_LOCALE = "en_ZA.UTF-8"

# Dotted package path and name of the function that
# is called on submit of the billing/shipping checkout step. This
# is where shipping calculation can be performed and set using the
# function ``cartridge.shop.utils.set_shipping``.
SHOP_HANDLER_BILLING_SHIPPING = \
    "cartridge.shop.checkout.default_billship_handler"

# Dotted package path and name of the function that
# is called once an order is successful and all of the order
# object's data has been created. This is where any custom order
# processing should be implemented.
SHOP_HANDLER_ORDER = "cartridge.shop.checkout.default_order_handler"

# Dotted package path and name of the function that
# is called on submit of the payment checkout step. This is where
# integration with a payment gateway should be implemented.
SHOP_HANDLER_PAYMENT = "cartridge.shop.checkout.default_payment_handler"

SHOP_HANDLER_TAX = "payment.checkout.vat_tax_handler"
SHOP_HANDLER_TAX_INCLUDE_IN_PRICE = False
SHOP_DEFAULT_SHIPPING_VALUE = 0
SHOP_ORDER_FROM_EMAIL = "secretary@sagta.org.za"

# Sequence of value/name pairs for order statuses.
SHOP_ORDER_STATUS_CHOICES = (
    (1, "Unprocessed"),
    (2, "Processed"),
)

SHOP_PAYMENT_STEP_ENABLED = False

# Sequence of value/name pairs for types of product options,
# eg Size, Colour. NOTE: Increasing the number of these will
# require database migrations!
SHOP_OPTION_TYPE_CHOICES = (
    (1, "Course date"),
    (2, "Course venue"),
)
# Sequence of value/name pairs for payment statuses.
SHOP_PAYMENT_STATUS_CHOICES = (
    (1, "Unchecked"),
    (2, "Checked"),
    (3, "Rejected"),
)

# Sequence of indexes from the SHOP_OPTION_TYPE_CHOICES setting that
# control how the options should be ordered in the admin,
# eg for "Colour" then "Size" given the above:
SHOP_OPTION_ADMIN_ORDER = (1,)