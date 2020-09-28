from django.http import HttpResponse
from django.conf.urls import url
from django.urls import path

from . import views

app_name = 'products'

urlpatterns = [
    # url(r'^$', views.ProductsView.as_view(), name='products_list'),
    url(r'^$', views.store, name="products_list"),
    url(r'^cart/$', views.cart, name="cart"),
    url(r'^checkout/$', views.checkout, name="checkout"),
    url(r'^update_item/$', views.updateItem, name="update_item"),
    url(r'^process_order/$', views.processOrder, name="process_order"),
]