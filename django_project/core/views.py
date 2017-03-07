# Create your views here.
from django.core.exceptions import ImproperlyConfigured
from django.http import HttpResponse, Http404
from django.template.response import TemplateResponse

from mezzanine.utils.urls import home_slug
from mezzanine.pages.models import Page
from urlparse import urlparse

def page(request, slug, template=u"pages/page.html", extra_context=None):
    """
    Select a template for a page and render it. The request
    object should have a ``page`` attribute that's added via
    ``mezzanine.pages.middleware.PageMiddleware``. The page is loaded
    earlier via middleware to perform various other functions.
    The urlpattern that maps to this view is a catch-all pattern, in
    which case the page attribute won't exist, so raise a 404 then.
    For template selection, a list of possible templates is built up
    based on the current page. This list is order from most granular
    match, starting with a custom template for the exact page, then
    adding templates based on the page's parent page, that could be
    used for sections of a site (eg all children of the parent).
    Finally at the broadest level, a template for the page's content
    type (it's model class) is checked for, and then if none of these
    templates match, the default pages/page.html is used.
    """

    from mezzanine.pages.middleware import PageMiddleware
    if not PageMiddleware.installed():
        raise ImproperlyConfigured("mezzanine.pages.middleware.PageMiddleware "
                                   "(or a subclass of it) is missing from " +
                                   "settings.MIDDLEWARE_CLASSES or " +
                                   "settings.MIDDLEWARE")

    if not hasattr(request, "page") or request.page.slug != slug:
        raise Http404

    # Check for a template name matching the page's slug. If the homepage
    # is configured as a page instance, the template "pages/index.html" is
    # used, since the slug "/" won't match a template name.
    # template_name = str(slug) if slug != home_slug() else "index"
    if slug == home_slug():
        #if host contains staging,https and port, then remove it
        host = request.get_host().split("//")[-1].split("/")[0].split(":")[0].replace("staging.","")
        pages = Page.objects.with_ascendants_for_slug(host,
                                                      for_user=request.user,
                                                      include_login_required=True)
        template_name = host
        # if pages:
        #     home_page = pages[0]
        #     setattr(request, "page", home_page)
        # else:
        #     template_name = "index"

    else:
        template_name = str(slug)

    templates = [u"pages/%s.html" % template_name]
    method_template = request.page.get_content_model().get_template_name()
    if method_template:
        templates.insert(0, method_template)
    if request.page.content_model is not None:
        templates.append(u"pages/%s/%s.html" % (template_name,
            request.page.content_model))
    for parent in request.page.get_ascendants(for_user=request.user):
        parent_template_name = str(parent.slug)
        # Check for a template matching the page's content model.
        if request.page.content_model is not None:
            templates.append(u"pages/%s/%s.html" % (parent_template_name,
                request.page.content_model))
    # Check for a template matching the page's content model.
    if request.page.content_model is not None:
        templates.append(u"pages/%s.html" % request.page.content_model)
    templates.append(template)
    return TemplateResponse(request, templates, extra_context or {})