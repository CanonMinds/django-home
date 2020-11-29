from django.http import HttpResponse
from django.conf.urls import url
from django.urls import path

from . import views

app_name = 'webscraping'

urlpatterns = [
    # url(r'^$', views.ProductsView.as_view(), name='products_list'),
    url(r'^$', views.WebListView.as_view(), name="webscraping_list"),
]