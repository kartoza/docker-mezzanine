# Based on http://www.jw.pe/blog/post/using-markdown-django-17/ (2016-03-18)
from django import template
import markdown

register = template.Library()

@register.filter
def markdownify(text):
    return markdown.markdown(text, extensions=["linkify"])
