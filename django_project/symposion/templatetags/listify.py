from django import template

register = template.Library()

@register.filter
def listify(generator):
    return list(generator)

@register.filter
def listify_if_true(generator, attr):
    return [item for item in generator if getattr(item, 'name')]
