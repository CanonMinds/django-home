from django.conf.urls import url
from django.urls import path

from . import views

app_name = 'greetings'

urlpatterns = [
    path('<str:username>/', views.flashword, name='flashword'),
    path('', views.home, name='home'),
]   