from __future__ import unicode_literals
from django import forms

from symposion.speakers.models import Speaker


class SpeakerForm(forms.ModelForm):
    required_css_class = 'required'

    class Meta:
        model = Speaker
        fields = [
            "name",
            "company",
            "biography",
        ]
