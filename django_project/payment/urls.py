from __future__ import unicode_literals

from django.conf.urls import url

from payment.views import PaymentCreate, PaymentSuccess

urlpatterns = [
    url("^confirm", PaymentCreate.as_view(),
        name="payment_confirmation"),
    url("^success", PaymentSuccess.as_view(),
        name="payment_confirmation_success"),
]
