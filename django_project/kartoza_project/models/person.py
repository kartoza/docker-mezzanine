from django.db import models


class Person(models.Model):
    name = models.CharField(
        max_length=300,
        null=False,
        blank=False
    )
    title = models.CharField(
        max_length=10,
        null=True,
        blank=True,
    )
    url = models.URLField(
        null=True,
        blank=True
    )

    description = models.TextField(
        null=True,
        blank=True
    )

    telephone = models.CharField(
        blank=True,
        help_text='Telephone number',
        max_length=16)

    email = models.EmailField(
        null=True,
        blank=True,
        help_text='A contact email address for the reference',
        verbose_name='Email')

    def __unicode__(self):
        return self.name
