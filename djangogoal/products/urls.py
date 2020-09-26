from django.http import HttpResponse
from django.conf.urls import url
from django.urls import path

from . import views

app_name = 'products'

urlpatterns = [
    # url(r'^$', views.ProductsView.as_view(), name='products_list'),
    url('', views.store, name="products_list"),
    url('cart/', views.cart, name="cart"),
    url('checkout/', views.checkout, name="checkout"),
]