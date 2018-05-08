from django.db.models import Count

from .models import Person, PersonCategory
from mezzanine import template


register = template.Library()


@register.as_tag
def people_categories(*args):
    """
    Put a list of categories for people into the template context.
    """
    people = Person.objects.published()
    categories = PersonCategory.objects.filter(people__in=people)
    return list(categories.annotate(people_count=Count("people")))


#
# Get Random People (templatetag)
#
class RandomPeople(template.Node):
    def __init__(self, limit, var_name):
        self.limit = limit
        self.var_name = var_name

    def render(self, context):
        random_people = Person.objects.order_by("?")[:int(self.limit)]
        if random_people and (int(self.limit) == 1):
            context[self.var_name] = random_people[0]
        else:
            context[self.var_name] = random_people
        return ""

@register.tag(name='get_random_people')
def do_get_random_people(parser, token):
    """
    Gets any number of people randomly and stores them in a variable.

    Syntax::

        {% get_random_people [limit] as [var_name] %}

    Example usage::

        {% get_random_people 10 as featured_people_list %}

    """
    try:
        tag_name, arg = token.contents.split(None, 1)
    except ValueError:
        raise template.TemplateSyntaxError, "%s tag requires arguments" % token.contents.split()[0]
    m = re.search(r'(.*?) as (\w+)', arg)
    if not m:
        raise template.TemplateSyntaxError, "%s tag had invalid arguments" % tag_name
    format_string, var_name = m.groups()
    return RandomPeople(format_string[0], var_name)
