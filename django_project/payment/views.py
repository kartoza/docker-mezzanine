__author__ = 'Irwan Fathurrahman <irwan@kartoza.com>'
__date__ = '08/09/16'
__license__ = "GPL"
__copyright__ = 'kartoza.com'

from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from .forms import PaymentForm


class PaymentCreate(CreateView):
    form_class = PaymentForm
    template_name = 'payment/payment.html'
    success_url = "/payment/success/"


class PaymentSuccess(TemplateView):
    template_name = "payment/success.html"
