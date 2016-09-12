from django.conf.urls import patterns, url

__author__ = 'Dimas Ciputra <dimas@kartoza.com>'
__date__ = '07/09/16'

urlpatterns = patterns(
    "clients.views",
    url("^client/(?P<slug>.*)/$",
        "client_detail",
        name="client_detail"),
    url("^all/$",
        "get_all_clients",
        name="get_all_clients")
)
