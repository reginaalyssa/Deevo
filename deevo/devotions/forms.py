from crispy_forms.helper import FormHelper
from django import forms

from bible.models import BibleVersionKey, KeyEnglish

class ReflectionForm(forms.Form):
    title = forms.CharField(max_length=100)
    reflection = forms.CharField(widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super(ReflectionForm, self).__init__(*args, **kwargs)
        self.fields['title'].required = False
        self.fields['reflection'].required = False

    helper = FormHelper()

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

    helper = FormHelper()
