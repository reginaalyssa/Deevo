from django.conf.urls import url

from . import views

app_name = 'bible'
urlpatterns = [
    url(r'^$', views.BookView.as_view(), name='book'),
    url(r'^(?P<book_id>[0-9]+)/(?P<chapter_id>[0-9]+)/$', views.chapter, name='chapter'),
    url(r'^(?P<book_id>[0-9]+)/(?P<chapter_id>[0-9]+)/(?P<verse_id>[0-9]+)/$', views.verse, name='verse')
]