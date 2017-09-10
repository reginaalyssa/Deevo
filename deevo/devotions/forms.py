from django import forms

class ReflectionForm(forms.Form):
    title = forms.CharField(max_length=100)
    reflection = forms.CharField(widget=forms.Textarea)