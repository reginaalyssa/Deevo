from django.conf.urls import url

from .forms import ChooseVerseForm, ReflectionForm
from .views import NewDevotionWizard

app_name = 'devotions'
urlpatterns = [
    url(r'^new/$', NewDevotionWizard.as_view([ChooseVerseForm, ReflectionForm]))
]