from django.conf.urls import url

from . import views

app_name = 'bible'
urlpatterns = [
    url(r'^change_version/$', views.change_version_book, name='change_version_book'),
    url(r'^change_version/(?P<book_id>[0-9]+)/(?P<chapter_id>[0-9]+)/$', views.change_version_chapter, name='change_version_chapter'),
    url(r'^change_version/(?P<book_id>[0-9]+)/(?P<chapter_id>[0-9]+)/(?P<verse_id>[0-9]+)/$', views.change_version_verse, name='change_version_verse'),
    url(r'^(?P<version_id>[a-z]+)/$', views.book, name='book'),
    url(r'^(?P<version_id>[a-z]+)/(?P<book_id>[0-9]+)/(?P<chapter_id>[0-9]+)/$', views.chapter, name='chapter'),
    url(r'^(?P<version_id>[a-z]+)/(?P<book_id>[0-9]+)/(?P<chapter_id>[0-9]+)/(?P<verse_id>[0-9]+)/$', views.verse, name='verse')
]