__author__ = 'Irwan Fathurrahman <irwan@kartoza.com>'
__date__ = '08/09/16'
__license__ = "GPL"
__copyright__ = 'kartoza.com'

from django import forms
from django.forms import ModelForm
from payment.models import Payment
from cartridge.shop.forms import OrderForm
from cartridge.shop.models import Order


class PaymentForm(ModelForm):
    class Meta:
        model = Payment
        fields = ['order_id', 'first_name', 'last_name', 'additional_info', 'additional_document']


class CustomOrderForm(OrderForm):
    class Meta:
        model = Order
        fields = ([f.name for f in Order._meta.fields if
                   f.name.startswith("billing_detail") or
                   f.name.startswith("shipping_detail")
                   ]
                  +
                  ["additional_instructions", "discount_code"])

    # TRUE_FALSE_CHOICES = (
    #     (True, 'Yes'),
    #     (False, 'No')
    # )
    # billing_detail_vat_registered = forms.ChoiceField(
    #     choices=TRUE_FALSE_CHOICES,
    #     label="Are you registered for VAT?",
    #     initial='No',
    #     widget=forms.Select(),
    #     required=False)
    billing_detail_vat_number = forms.CharField(
        label="Your South African registered VAT Tax number (if registered)",
        required=False)

    def __init__(
            self, request, step, data=None, initial=None, errors=None,
            **kwargs):
        # self.fields["vat_registered"].name = "vat_registered"
        res = super(CustomOrderForm, self).__init__(request, step, data, initial, errors, **kwargs)

        #
        # self.fields["billing_detail_vat_registered"].widget = forms.CheckboxInput()

