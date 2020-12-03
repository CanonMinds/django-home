from django.http import HttpResponse
from django.conf.urls import url
from django.urls import path

from . import views

app_name = 'soaptask'

urlpatterns = [
    url(r'^$', views.home, name="soaptask_index"),
    url(r'^add/$', views.soapclient, name="soaptask_result"),
]