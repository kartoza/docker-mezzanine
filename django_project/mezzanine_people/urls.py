
from django.conf.urls import patterns, include, url

# People patterns.
urlpatterns = patterns("mezzanine_people.views",
    url("^category/(?P<category>.*)/$", "person_list", name="person_list_category"),
    url("^person/(?P<slug>[-\w]+)/$", "person_detail", name="person_detail"),
    url("^$", "person_list", name="person_list"),
)
