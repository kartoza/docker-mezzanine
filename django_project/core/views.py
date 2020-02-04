import json
import requests
from django.core import serializers
from django.http import HttpResponse
from mezzanine.pages.views import page
from mezzanine_people.models import Person, Office
from mezzanine.core.models import CONTENT_STATUS_PUBLISHED
from mezzanine.utils.views import render as mez_render
from django.shortcuts import render
from mezzanine.conf import settings
from clients.models import Client


def get_all_people(request):
    data = serializers.serialize(
        "json",
        Person.objects.filter(status=CONTENT_STATUS_PUBLISHED).order_by('order'))
    return HttpResponse(json.dumps(data), content_type="application/json")


def home(request, slug):
    data_in = list(Client.objects.filter(status=2).order_by('title').values())

    data = {'clients': data_in[:24]}
    return page( request, slug, u"pages/page.html", data)


def about(request):

    template = "about.html"
    settings.use_editable()
    templates = ["kartoza_theme/pages/page.html"]
    people = Person.objects.published()

    context = {"people": people, "category": None}
    templates.append(template)
    return mez_render(request, templates, context)


def contact(request):
    """ Show contact page with person in the page
    """
    template = "pages/contact.html"
    settings.use_editable()
    templates = []
    people = Person.objects.published()
    office = Office.objects.published()

    context = {
        "people": people, "office": office}
    templates.append(template)
    return mez_render(request, templates, context)


def create_web_to_contact(request):
    recaptcha_result = validate_g_recaptcha(request)
    data = request.GET.copy()
    if not recaptcha_result:
        return HttpResponse("<h1>Recaptcha failed</h1>")
    data['email'] = data[u'emails[0].Value']
    data['phone'] = data[u'phones[0].Value']
    del data['g-recaptcha-response']
    del data[u'emails[0].Value']
    del data[u'phones[0].Value']

    new_data = {}
    for key in data:
        new_data[str(key)] = str(data[key])
    return render(request, "includes/contact_us_submit.html", new_data)



def validate_g_recaptcha(request):
    if request.GET['g-recaptcha-response']:
        data = request.GET
        secret_key = settings.RECAPTCHA_SECRET_KEY
        data = {
            'response': data.get('g-recaptcha-response'),
            'secret': secret_key
        }
        resp = requests.post('https://www.google.com/recaptcha/api/siteverify',
                             data=data)
        result_json = resp.json()
        if not result_json.get('success'):
            return False
        else:
            return True
    else:
        return False
