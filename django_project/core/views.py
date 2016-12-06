# Create your views here.
import json
from django.core import serializers
from django.http import HttpResponse
from mezzanine_people.models import Person
from mezzanine.core.models import CONTENT_STATUS_PUBLISHED


def get_all_people(request):
    data = serializers.serialize(
        "json",
        Person.objects.filter(status=CONTENT_STATUS_PUBLISHED).order_by('order'))
    return HttpResponse(json.dumps(data), content_type="application/json")
