from django import forms
from django.utils.safestring import mark_safe

from .models import MapProposal, TalkProposal, WorkshopProposal


class ProposalForm(forms.ModelForm):
    required_css_class = 'required'

    def clean_description(self):
        value = self.cleaned_data["description"]
        if len(value) > 400:
            raise forms.ValidationError(
                u"The description must be less than 400 characters"
            )
        return value


class TalkProposalForm(ProposalForm):

    class Meta:
        FOOTNOTE = '<sup><a href="#fn1" title="Open source definition">1</a></sup>'

        model = TalkProposal
        fields = [
            "title",
            "abstract",
            "tags",
            "recording_release",
            "foss_is",
            "foss_is_links",
            "foss_contributing",
            "foss_contributing_links",
            "foss_using",
            "foss_using_links",
            "additional_notes",
        ]
        labels = {
            'foss_is': mark_safe(
                "This talk is about a project that is open source{}"
                .format(FOOTNOTE)),
            'foss_contributing': mark_safe(
                "This talk is about a project that is actively contributing "
                "to open source{} projects".format(FOOTNOTE)),
            'foss_using': mark_safe(
                "This talk is about a project that is using open source{}"
                .format(FOOTNOTE)),
        }
        widgets = {
          'abstract': forms.Textarea(attrs={'rows': 13}),
          'additional_notes': forms.Textarea(attrs={'rows': 7}),
          'foss_is_links': forms.Textarea(attrs={'rows': 3}),
          'foss_contributing_links': forms.Textarea(attrs={'rows': 5}),
          'foss_using_links': forms.Textarea(attrs={'rows': 5}),
        }


class WorkshopProposalForm(ProposalForm):

    class Meta:
        model = WorkshopProposal
        fields = [
            "title",
            "abstract",
            "tags",
            "additional_notes",
        ]


class MapProposalForm(ProposalForm):

    def clean_map_image(self):
        image = self.cleaned_data['map_image']
        megabyte_limit = 5
        if image.size > megabyte_limit * 1024 * 1024:
            raise forms.ValidationError(
                "The submitted file was bigger than {}MB.".format(megabyte_limit))
        return image

    class Meta:
        model = MapProposal
        fields = [
            "title",
            "abstract",
            "tags",
            "map_image",
            "map_link",
            "foss_using",
            "open_data_using",
            "additional_notes",
        ]
        widgets = {
          'abstract': forms.Textarea(attrs={'rows': 13}),
          'foss_using': forms.Textarea(attrs={'rows': 4}),
          'open_data_using': forms.Textarea(attrs={'rows': 4}),
          'additional_notes': forms.Textarea(attrs={'rows': 7}),
        }
