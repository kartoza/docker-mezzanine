from django.db import models


class Role(models.Model):
    name = models.CharField(
        max_length=300,
        null=False,
        blank=False
    )

    description = models.TextField(
        null=True,
        blank=True
    )

    def __unicode__(self):
        return self.name
