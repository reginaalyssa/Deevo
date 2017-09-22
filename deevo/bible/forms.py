from bible.models import BibleVersionKey
from django import forms

from .models import *

class VersionForm(forms.Form):
    version = forms.ModelChoiceField(
        queryset=BibleVersionKey.objects.all(),
        required=True,
        initial=1
    )

class ChapterForm(forms.Form):
    def __init__(self, *args, **kwargs):
        model = kwargs.pop('model')
        book_id = kwargs.pop('book_id')
        print(book_id)
        super(ChapterForm, self).__init__(*args, **kwargs)
        self.fields['chapter'] = forms.ModelChoiceField(
            queryset=model.objects.filter(b=book_id['book_id']).values_list('c', flat=True).distinct(),
            required=True,
            empty_label=None
        )

    chapter = forms.ModelChoiceField(
        queryset=TAsv.objects.filter(b=1).values_list('c', flat=True).distinct(),
        required=True,
        empty_label=None
    )