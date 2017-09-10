from bible.models import KeyEnglish, BibleVersionKey, TAsv
from django import forms

class VersionForm(forms.Form):
    version = forms.ModelChoiceField(
        queryset=BibleVersionKey.objects.all(),
        required=True,
        initial=1
    )

class BookChapterForm(forms.Form):
    book = forms.ModelChoiceField(
        queryset=KeyEnglish.objects.all(),
        required=True,
        initial=1
    )
    chapter = forms.ModelChoiceField(
        queryset=TAsv.objects.filter(b=1).values_list('c', flat=True).distinct(),
        required=True,
        initial=1
    )
    verse = forms.ChoiceField()