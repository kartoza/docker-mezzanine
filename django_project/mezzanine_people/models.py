from django.db import models
from django.utils.translation import ugettext_lazy as _
from mezzanine.core.models import Displayable, RichText, Slugged
from mezzanine.utils.models import AdminThumbMixin
from mezzanine.core.fields import RichTextField, FileField



class Person(Displayable, RichText, AdminThumbMixin):
    """
    A person.
    """

    categories = models.ManyToManyField("PersonCategory",
                                        verbose_name=_("Categories"),
                                        blank=True, related_name="people")
    first_name = models.CharField(_("first name"), blank=True, max_length=100)
    last_name = models.CharField(_("last name"), blank=True, max_length=100)
    mugshot = FileField(verbose_name=_("Profile photo"),
                        upload_to="people", format="Image",
                        max_length=255, null=True, blank=True)
    mugshot_hover = FileField(verbose_name=_("Hover Profile photo"),
                              upload_to="people", format="Image",
                              max_length=255, null=True, blank=True)
    mugshot_credit = models.CharField(_("Profile photo credit"), blank=True, max_length=200)
    email = models.EmailField(_("e-mail address"), blank=True)
    bio = RichTextField(_("biography"),
                          help_text=_("This field can contain HTML and should contain a few paragraphs describing the background of the person."),
                          default="", blank=True)
    job_title = models.CharField(_("job title"), max_length=60, blank=True, help_text=_("Example: First Grade Teacher"))
    order = models.PositiveSmallIntegerField(default=0)
    admin_thumb_field = "mugshot"
    search_fields = {"first_name", "last_name", "bio", "job_title",}

    class Meta:
        verbose_name = _("Person")
        verbose_name_plural = _("People")
        ordering = ("order", "last_name", "first_name",)

    @property
    def full_name(self):
        return u'%s %s' % (self.first_name, self.last_name)

    @models.permalink
    def get_absolute_url(self):
        return ("person_detail", (), {"slug": self.slug})


class PersonLink(models.Model):
    """
    A link to a person's interesting URLs, such as Twitter or Facebook
    """
    name = models.CharField(_("link name"), max_length=50, help_text=_("Friendly name of the link. E.g. Twitter"))
    url = models.URLField(_("URL"))
    person = models.ForeignKey(Person)

    class Meta:
        ordering = ('name',)


class PersonCategory(Slugged):
    """
    A category for grouping people.
    """

    class Meta:
        verbose_name = _("Person Category")
        verbose_name_plural = _("Person Categories")

    @models.permalink
    def get_absolute_url(self):
        return ("person_list_category", (), {"slug": self.slug})
