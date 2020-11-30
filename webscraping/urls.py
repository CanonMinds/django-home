from django.http import HttpResponse
from django.conf.urls import url
from django.urls import path

from . import views

app_name = 'webscraper'

urlpatterns = [
    # url(r'^$', views.ProductsView.as_view(), name='products_list'),
    url(r'^$', views.home, name="webscraping_list"),
    url(r'^module1/$', views.module1, name="module1_list"),
    url(r'^module2/$', views.module2, name="module2_list"),
    url(r'^module3/$', views.module3, name="module3_list"),
]