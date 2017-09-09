from django.conf.urls import url

from . import views

app_name = 'bible'
urlpatterns = [
    url(r'^$', views.BookView.as_view(), name='book'),
]