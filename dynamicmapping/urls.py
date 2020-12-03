from django.http import HttpResponse
from django.conf.urls import url
from django.urls import path

from . import views

app_name = 'dynamicmapping'

urlpatterns = [
    url(r'^$', views.home, name="dynamicmapping_list"),
]