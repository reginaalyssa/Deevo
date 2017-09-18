from django.conf.urls import url

from .forms import ChooseVerseForm, ReflectionForm
from .views import DevotionDetailView, DevotionListView, NewDevotionWizardView, UpdateDevotionView
from . import views

app_name = 'devotions'
urlpatterns = [
    url(r'^new/$', NewDevotionWizardView.as_view([ChooseVerseForm, ReflectionForm]), name='new'),
    url(r'^$', DevotionListView.as_view(), name='view_devotions'),
    url(r'^(?P<pk>[0-9]+)$', DevotionDetailView.as_view(), name='view_specific'),
    url(r'^(?P<pk>[0-9]+)/edit/$', UpdateDevotionView.as_view(), name='edit'),
    url(r'^(?P<version_id>[a-z]+)/(?P<book_id>[0-9]+)/(?P<chapter_id>[0-9]+)/(?P<verse_id>[0-9]+)/reflect/$', views.reflect, name='reflect')

]