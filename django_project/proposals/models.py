import re

from django.core.exceptions import ValidationError
from django.db import models
from django.utils.deconstruct import deconstructible
from django.utils.safestring import mark_safe
from taggit.managers import TaggableManager

from symposion.proposals.models import ProposalBase


@deconstructible
class MaxMarkdownWordValidator(object):
    charachter_re = re.compile('[a-zA-Z0-9]')

    def __init__(self, maximum):
        self.maximum = maximum
        self.message = 'The text has more than maximum of {} words.'.format(
            maximum)

    def __call__(self, value):
        words = value.split()
        words = [word for word in words
                 if self.charachter_re.search(word) is not None]
        if len(words) > self.maximum:
            raise ValidationError(self.message)
        else:
            return True

    def __eq__(self, other):
        return (
            isinstance(other, MaxWordValidator) and
            (self.maximum == other.maximum)
        )


class Proposal(ProposalBase):
    tags = TaggableManager(blank=True)

    class Meta:
        abstract = True

Proposal._meta.get_field('abstract').verbose_name = 'Abstract'
Proposal._meta.get_field('abstract').help_text = (
    "Will be made public if your proposal is accepted. "
    "Please aim for 125-175 words, 250 words is the maximum. Edit using "
    "<a href='http://daringfireball.net/projects/markdown/basics' "
    "target='_blank'>Markdown</a>.")
Proposal._meta.get_field('abstract').validators = [MaxMarkdownWordValidator(250)]


class TalkProposal(Proposal):

    recording_release = models.BooleanField(
        default=True,
        help_text="By submitting your proposal, you agree to give permission to the conference organizers to record, edit, and release audio and/or video of your presentation. If you do not agree to this, please uncheck this box."
    )

    foss_is = models.BooleanField(
        default=False,
    )
    foss_is_links = models.TextField(
        verbose_name="Link to project",
        help_text="Please add a link to the source code of your open source project",
        blank=True
    )
    foss_contributing = models.BooleanField(
        default=False,
    )
    foss_contributing_links = models.TextField(
        verbose_name="Link to contributions",
        help_text="Please add links some of the contributions you've made",
        blank=True
    )
    foss_using = models.BooleanField(
        default=False,
    )
    foss_using_links = models.TextField(
        verbose_name="Link to projects",
        help_text="Please add links some of the projects you use",
        blank=True
    )

    class Meta:
        verbose_name = "talk proposal"


class WorkshopProposal(Proposal):

    class Meta:
        verbose_name = "workshop proposal"


class MapProposal(Proposal):
    FOOTNOTE = '<sup><a href="#fn1" title="Open source definition">1</a></sup>'
    FOOTNOTE2 = '<sup><a href="#fn2" title="Open data definition">2</a></sup>'

    class Meta:
        verbose_name = "map proposal"

    map_image = models.ImageField(
        upload_to="maps",
        verbose_name="Map",
        help_text=("Please upload an image of the map. "
                   "It will be made public on the website. "
                   "If it's an interactive map, please create a screenshot. "
                   "The size is limited to 5MB."))

    map_link = models.URLField(
        verbose_name="Link to Map",
        help_text=("This link will be used to link the image on our website "
                   "to your map. It could be a link to a "
                   "high resolution version, a webpage with further details "
                   "or to your interactive map."),
        blank=True)

    foss_using = models.TextField(
        verbose_name="FOSS software used",
        help_text=mark_safe(
            "Please list the Free and open-source software{} "
            "that you've used for creating the map."
            .format(FOOTNOTE)),
        blank=True)

    open_data_using = models.TextField(
        verbose_name="Open data used",
        help_text=mark_safe(
            "Please list the open data{} sources "
            "that you've used for creating the map."
            .format(FOOTNOTE2)),
        blank=True)
