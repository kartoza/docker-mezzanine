# Create your views here.
import json
from django.core import serializers
from django.http import HttpResponse
from django.forms.models import model_to_dict
from mezzanine.pages.views import page
from mezzanine_people.models import Person
from mezzanine.core.models import CONTENT_STATUS_PUBLISHED
from mezzanine.utils.views import render
from mezzanine.conf import settings
from clients.models import Client


def get_all_people(request):
    data = serializers.serialize(
        "json",
        Person.objects.filter(status=CONTENT_STATUS_PUBLISHED).order_by('order'))
    return HttpResponse(json.dumps(data), content_type="application/json")


def home(request, slug):
    n = 3
    data_in = list(Client.objects.filter(status=2).order_by('title').values())
    data_in_split = [data_in[i * n:(i + 1) * n] for i in range((len(data_in) + n - 1) // n)]

    data = {'clients': data_in_split}
    return page( request, slug, u"pages/page.html", data)


def about(request):

    template = "mezzanine_people/person_list.html"
    settings.use_editable()
    templates = ["kartoza_theme/pages/page.html"]
    people = Person.objects.published()

    context = {"people": people, "category": None}
    templates.append(template)
    return render(request, templates, context)
