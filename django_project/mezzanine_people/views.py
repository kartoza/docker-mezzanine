from django.http import Http404
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import get_object_or_404
#from django import VERSION

from .models import Person, PersonCategory
from mezzanine.conf import settings
from mezzanine.generic.models import AssignedKeyword, Keyword
from mezzanine.utils.views import render, paginate


def person_list(request, category=None, template="mezzanine_people/person_list.html"):
    """
    Display a list of people that are filtered by category.
    Custom templates are checked for using the name
    ``people/person_list_XXX.html`` where ``XXX`` is the category's slug.
    """
    settings.use_editable()
    templates = []
    people = Person.objects.published()
    if category is not None:
        category = get_object_or_404(PersonCategory, slug=category)
        people = people.filter(categories=category)
        templates.append(u"mezzanine_people/person_list_%s.html" %
                          unicode(category.slug))

    # requires Django VERSION >= (1, 4):
    people = people.prefetch_related("categories")

    people = paginate(people, request.GET.get("page", 1),
                      settings.PEOPLE_PER_PAGE,
                      settings.MAX_PAGING_LINKS)
    context = {"people": people, "category": category}
    templates.append(template)
    return render(request, templates, context)


def person_detail(request, slug,
                  template="mezzanine_people/person_detail.html"):
    """
    Custom templates are checked for using the name
    ``mezzanine_people/person_detail_XXX.html`` where ``XXX`` is the
    person's slug.
    """
    people = Person.objects.published()
    person = get_object_or_404(people, slug=slug)
    context = {"person": person, "editable_obj": person}
    templates = [u"mezzanine_people/person_detail_%s.html" % unicode(slug), template]
    return render(request, templates, context)
