from django.conf.urls import url

from . import views

app_name = 'bible'
urlpatterns = [
    url(r'^change_version/(?P<book_id>[0-9]+)/(?P<chapter_id>[0-9]+)/$', views.change_version, name='change_version'),
    url(r'^(?P<version_id>[a-z]+)/$', views.BookView.as_view(), name='book'),
    url(r'^(?P<version_id>[a-z]+)/(?P<book_id>[0-9]+)/(?P<chapter_id>[0-9]+)/$', views.chapter, name='chapter'),
    url(r'^(?P<version_id>[a-z]+)/(?P<book_id>[0-9]+)/(?P<chapter_id>[0-9]+)/(?P<verse_id>[0-9]+)/$', views.verse, name='verse')
]