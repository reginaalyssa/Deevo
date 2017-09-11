from bible.models import BibleVersionKey
from django import forms

class VersionForm(forms.Form):
    version = forms.ModelChoiceField(
        queryset=BibleVersionKey.objects.all(),
        required=True,
        initial=1
    )