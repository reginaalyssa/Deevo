from django import forms

from bible.models import BibleVersionKey, KeyEnglish

class ReflectionForm(forms.Form):
    title = forms.CharField(max_length=100)
    reflection = forms.CharField(widget=forms.Textarea)

class ChooseVerseForm(forms.Form):
    book = forms.ModelChoiceField(
        queryset=KeyEnglish.objects.all(),
        required=True,
        initial=1
    )
    # chapter = forms.ModelChoiceField(
    #     queryset=TAsv.objects.filter(b=1).values_list('c', flat=True).distinct(),
    #     required=True,
    #     initial=1
    # )
    chapter = forms.IntegerField()
    verse = forms.IntegerField()
    version = forms.ModelChoiceField(
        queryset=BibleVersionKey.objects.all(),
        required=True,
        initial=1
    )