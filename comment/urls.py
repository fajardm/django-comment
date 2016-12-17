from django.conf.urls import url
from . import views

app_name = 'comment'
urlpatterns = [
    url(r'^$', views.index, name='list'),
    url(r'^create/$', views.create, name='create'),
    url(r'^(?P<pk>[0-9]+)/edit/', views.edit, name='edit'),
    url(r'^(?P<pk>[0-9]+)/delete/$', views.delete, name='delete'),
]
