from django.conf.urls import url

from .forms import ChooseVerseForm, ReflectionForm
from .views import NewDevotionWizard
from . import views

app_name = 'devotions'
urlpatterns = [
    url(r'^new/$', NewDevotionWizard.as_view([ChooseVerseForm, ReflectionForm]), name='new'),
    url(r'^view/$', views.DevotionView.as_view(), name='view_devotions'),
]