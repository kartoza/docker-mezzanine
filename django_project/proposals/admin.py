from django.contrib import admin

from .models import TalkProposal
from .models import MapProposal
from .models import WorkshopProposal


admin.site.register(TalkProposal)
admin.site.register(MapProposal)
admin.site.register(WorkshopProposal)
