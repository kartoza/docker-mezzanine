# Based on http://www.jw.pe/blog/post/using-markdown-django-17/ (2016-03-18)
from django import template
import markdown
import bleach
from django.conf import settings

register = template.Library()

@register.filter
def markdownify(text):
    untrusted_text = markdown.markdown(text)
    html = bleach.clean(untrusted_text,
                        tags=settings.MARKDOWNIFY_WHITELIST_TAGS, )
    # html = bleach.linkify(html)
    return untrusted_text
