from django.conf.urls import patterns, url


# People patterns.
urlpatterns = patterns('kartoza_project.views',
    url("^category/(?P<category>.*)/$", "project_list", name="project_list_category"),
    url("^detail/(?P<slug>[-\w]+)/$", "project_detail", name="project_detail"),
    url("^ongoing/$", "project_list_ongoing", name="project_list_ongoing"),
    url("^$", "project_list", name="project_list"),
    url("^view/(?P<project_id>.*)/$",
        "view_project",
        name="view_project"),
    url("^get_reference/$",
        "get_reference",
        name="get_reference"),
    url("^gallery/$",
        "project_gallery",
        name="project_gallery"),
    # url("^list/$",
    #     "project_gallery",
    #     name="project_list")
)
