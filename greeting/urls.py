from django.conf.urls import url

from . import views

app_name = 'greeting'

urlpatterns = [
    url(r'^$', views.greeting, name='home'),
]   