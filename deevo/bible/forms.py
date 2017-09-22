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
        super(ChapterForm, self).__init__(*args, **kwargs)
        self.fields['chapter'] = forms.ModelChoiceField(
            queryset=model.objects.filter(b=book_id).values_list('c', flat=True).distinct(),
            required=True,
            empty_label=None
        )

class VerseForm(forms.Form):
    def __init__(self, *args, **kwargs):
        model = kwargs.pop('model')
        book_id = kwargs.pop('book_id')
        chapter_id = kwargs.pop('chapter_id')
        super(VerseForm, self).__init__(*args, **kwargs)
        self.fields['verse'] = forms.ModelChoiceField(
            queryset=model.objects.filter(b=book_id, c=chapter_id),
            required=True,
            empty_label=None
        )