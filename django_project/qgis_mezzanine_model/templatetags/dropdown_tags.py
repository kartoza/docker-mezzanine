from mezzanine import template
from mezzanine.pages.models import Page

register = template.Library()

@register.simple_tag
def qgis_page_menu(page):
    pass
    # if page.content_model == "AuthLink":
    #     return "A"
    # else:
    #     return "B"