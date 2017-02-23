from django.conf.urls import patterns, url


urlpatterns = patterns(
    "symposion.proposals.views",
    url(r"^submit/$", "proposal_submit", name="proposal_submit"),
    url(r"^submit/([\w\-]+)/$", "proposal_submit_kind",
        name="proposal_submit_kind"),
    url(r"^(\d+)/$", "proposal_detail", name="proposal_detail"),
    url(r"^(\d+)/export/$", "proposal_export", name="proposal_export"),
    url(r"^(\d+)/edit/$", "proposal_edit", name="proposal_edit"),
    url(r"^(\d+)/speakers/$", "proposal_speaker_manage",
        name="proposal_speaker_manage"),
    url(r"^(\d+)/cancel/$", "proposal_cancel", name="proposal_cancel"),
    url(r"^(\d+)/leave/$", "proposal_leave", name="proposal_leave"),
    url(r"^(\d+)/join/$", "proposal_pending_join", name="proposal_pending_join"),
    url(r"^(\d+)/decline/$", "proposal_pending_decline", name="proposal_pending_decline"),

    url(r"^(\d+)/document/create/$", "document_create", name="proposal_document_create"),
    url(r"^document/(\d+)/delete/$", "document_delete", name="proposal_document_delete"),
    url(r"^document/(\d+)/([^/]+)$", "document_download", name="proposal_document_download"),
    # Export several proposals in one page, given by query parameter `ids`
    url(r"^export/$", "proposal_export", name="proposal_export"),
    url(r"^frab/events$", "proposal_events_export_frab", name="proposal_events_export_frab"),
    url(r"^frab/event_people$", "proposal_event_people_export_frab", name="proposal_event_people_export_frab"),
    url(r"^frab/people$", "proposal_people_export_frab", name="proposal_people_export_frab"),
)
