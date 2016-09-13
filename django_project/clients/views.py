import json
from mezzanine.utils.views import render
from .models import Client
from django.core import serializers
from django.http import HttpResponse

__author__ = 'Dimas Ciputra <dimas@kartoza.com>'
__date__ = '07/09/16'


def client_detail(request, slug,
                  template="clients/client_detail.html"):
    clients = Client.objects.published()
    context = {"client": clients}
    templates = [u"clients/client_detail_%s.html" % unicode(slug), template]
    return render(request, templates, context)


def get_all_clients(request):
    data = serializers.serialize("json", Client.objects.all().order_by('title'))
    return HttpResponse(json.dumps(data), content_type="application/json")
