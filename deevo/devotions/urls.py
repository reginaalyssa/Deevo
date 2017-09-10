from django.conf.urls import url

from . import views
from .forms import ReflectionForm

app_name = 'devotions'
urlpatterns = [
    url(r'^reflect/(?P<version_id>[a-z]+)/(?P<book_id>[0-9]+)/(?P<chapter_id>[0-9]+)/(?P<verse_id>[0-9]+)/$', views.reflect, name='reflect')
]