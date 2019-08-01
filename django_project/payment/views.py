__author__ = 'Irwan Fathurrahman <irwan@kartoza.com>'
__date__ = '08/09/16'
__license__ = "GPL"
__copyright__ = 'kartoza.com'


from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from payment.forms import PaymentForm
from payment.models import OrderDetails


class PaymentCreate(CreateView):
    form_class = PaymentForm
    template_name = 'payment/payment.html'
    success_url = "/payment/success/"


class PaymentSuccess(TemplateView):
    template_name = "payment/success.html"


def custom_order_handler(request, order_form, order):
    """
    Default order handler - called when the order is complete and
    contains its final data. Implement your own and specify the path
    to import it from via the setting ``SHOP_HANDLER_ORDER``.
    """
    vat_number = order_form.cleaned_data['billing_detail_vat_number']
    if vat_number:
        OrderDetails.objects.create(order_id=order.id, vat_number=vat_number)
    else:
        pass