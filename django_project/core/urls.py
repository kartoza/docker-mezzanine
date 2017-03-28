# from django.conf.urls import patterns, include, url
#
# from django.contrib import admin
# admin.autodiscover()
#
# urlpatterns = patterns('',
#    # Examples:
#    # url(r'^$', 'django_project.views.home', name='home'),
#    # url(r'^blog/', include('blog.urls')),
#
#    url(r'^admin/', include(admin.site.urls)),
# )
from __future__ import unicode_literals

from django.conf.urls import patterns, include, url
from django.conf.urls.i18n import i18n_patterns, urlpatterns
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from mezzanine.core.views import direct_to_template
import symposion.views
from core.settings.utils import absolute_path

from cartridge.shop.views import order_history

admin.autodiscover()

# Add the urlpatterns for any custom Django applications here.
# You can also change the ``home`` view to add your own functionality
# to the project's homepage.

urlpatterns = i18n_patterns(
    '',
    # Change the admin prefix here to use an alternate URL for the
    # admin interface, which would be marginally more secure.
    ("^admin/", include(admin.site.urls)),
    url(r"^dashboard/", symposion.views.dashboard, name="dashboard"),
    url("^speaker/", include("symposion.speakers.urls")),
    url("^conference/", include("symposion.conference.urls")),
    url(r"^account/", include("account.urls")),
    url(r"^sponsors/", include("symposion.sponsorship.urls")),
    url(r"^proposals/", include("symposion.proposals.urls")),
    url(r"^boxes/", include("pinax.boxes.urls")),
    url(r"^sponsors/", include("symposion.sponsorship.urls")),
    url(r"^reviews/", include("symposion.reviews.urls")),
    url(r"^schedule/", include("symposion.schedule.urls")),
    url("^shop/", include("cartridge.shop.urls")),
    url("^account/orders/$", order_history, name="shop_order_history"),
    url("^social/", include('social_django.urls', namespace='social')),
    url("^payment/", include("payment.urls")),
    url(r"^teams/", include("symposion.teams.urls")),

    # For mezzanine-people
    ("^people/", include('mezzanine_people.urls')),

    # For mezzanine-agenda
    ("^%s/" % settings.EVENT_SLUG, include("mezzanine_agenda.urls")),

    # We don't want to presume how your homepage works, so here are a
    # few patterns you can use to set it up.

    # HOMEPAGE AS STATIC TEMPLATE
    # ---------------------------
    # This pattern simply loads the index.html template. It isn't
    # commented out like the others, so it's the default. You only need
    # one homepage pattern, so if you use a different one, comment this
    # one out.

    # url("^$", direct_to_template, {"template": "index.html"}, name="home"),

    # HOMEPAGE AS AN EDITABLE PAGE IN THE PAGE TREE
    # ---------------------------------------------
    # This pattern gives us a normal ``Page`` object, so that your
    # homepage can be managed via the page tree in the admin. If you
    # use this pattern, you'll need to create a page in the page tree,
    # and specify its URL (in the Meta Data section) as "/", which
    # is the value used below in the ``{"slug": "/"}`` part.
    # Also note that the normal rule of adding a custom
    # template per page with the template name using the page's slug
    # doesn't apply here, since we can't have a template called
    # "/.html" - so for this case, the template "pages/index.html"
    # should be used if you want to customize the homepage's template.


    #overriding mezzanine pages management
    #for custom data (rich text), add a page with name foss4g-home
    url("^$", "core.views.page", {"slug": "/"}, name="home"),

    # TEMPLATE HOMEPAGE FOR FOSS4G
    # ---------------------------
    # This pattern simply loads the index.html template.

    # HOMEPAGE FOR A BLOG-ONLY SITE
    # -----------------------------
    # This pattern points the homepage to the blog post listing page,
    # and is useful for sites that are primarily blogs. If you use this
    # pattern, you'll also need to set BLOG_SLUG = "" in your
    # ``settings/contrib.py`` module, and delete the blog page object from the
    # page tree in the admin if it was installed.

    # url("^$", "mezzanine.blog.views.blog_post_list", name="home"),

    # MEZZANINE'S URLS
    # ----------------
    # ADD YOUR OWN URLPATTERNS *ABOVE* THE LINE BELOW.
    # ``mezzanine.urls`` INCLUDES A *CATCH ALL* PATTERN
    # FOR PAGES, SO URLPATTERNS ADDED BELOW ``mezzanine.urls``
    # WILL NEVER BE MATCHED!

    # If you'd like more granular control over the patterns in
    # ``mezzanine.urls``, go right ahead and take the parts you want
    # from it, and use them directly below instead of using
    # ``mezzanine.urls``.
    ("^", include("mezzanine.urls")),

    # MOUNTING MEZZANINE UNDER A PREFIX
    # ---------------------------------
    # You can also mount all of Mezzanine's urlpatterns under a
    # URL prefix if desired. When doing this, you need to define the
    # ``SITE_PREFIX`` setting, which will contain the prefix. Eg:
    # SITE_PREFIX = "my/site/prefix"
    # For convenience, and to avoid repeating the prefix, use the
    # commented out pattern below (commenting out the one above of course)
    # which will make use of the ``SITE_PREFIX`` setting. Make sure to
    # add the import ``from django.conf import settings`` to the top
    # of this file as well.
    # Note that for any of the various homepage patterns above, you'll
    # need to use the ``SITE_PREFIX`` setting as well.

    # ("^%s/" % settings.SITE_PREFIX, include("mezzanine.urls"))

    # For mezzanine-agenda
    ("^%s/" % settings.EVENT_SLUG, include("mezzanine_agenda.urls")),
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.SYMPOSION_STATIC_URL, document_root=absolute_path("symposion","site_media"))
urlpatterns += (

)

urlpatterns += [
    # Cartridge URLs.

]

# Adds ``STATIC_URL`` to the context of error pages, so that error
# pages can use JS, CSS and images.
handler404 = "mezzanine.core.views.page_not_found"
handler500 = "mezzanine.core.views.server_error"
