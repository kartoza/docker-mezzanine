__author__ = 'Irwan Fathurrahman <irwan@kartoza.com>'
__date__ = '08/09/16'
__license__ = "GPL"
__copyright__ = 'kartoza.com'

from django.forms import ModelForm
from .models import Payment


class PaymentForm(ModelForm):
    class Meta:
        model = Payment
        fields = ['order_id', 'first_name', 'last_name', 'additional_info', 'additional_document']
