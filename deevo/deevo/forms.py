from crispy_forms.helper import FormHelper
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):

    def __init__(self, *args, **kargs):
        super(SignUpForm, self).__init__(*args, **kargs)
        del self.fields['password2']

        for fieldname in ['username', 'password1']:
            self.fields[fieldname].help_text = None

    email = forms.EmailField(max_length=254, help_text='We take privacy very seriously and promise not to '
                                                       'share your email address with anyone.')
    helper = FormHelper()

    class Meta:
        model = User
        fields = ('username', 'email', 'password1',)