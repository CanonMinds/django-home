from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.ListCreateTask.as_view(), name='task_list'),
]

app_name = 'tasks'

# from django.conf.urls import url
# from . import views

# urlpatterns = [
#     url(),
# ]

# app_name = 'tasks'