from django.conf import settings

def recaptcha_v3_context(request):
    context = {'site_key': settings.RECAPTCHA_SITE_KEY}
    return context