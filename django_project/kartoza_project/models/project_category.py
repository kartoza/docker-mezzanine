from django.db import models
from mezzanine.core.models import Slugged


class ProjectCategory(Slugged):
    """
    A category for grouping people.
    """

    class Meta:
        verbose_name = 'Project Category'
        verbose_name_plural = 'Project Categories'

    @models.permalink
    def get_absolute_url(self):
        return ("project_list_category", (), {"slug": self.slug})
