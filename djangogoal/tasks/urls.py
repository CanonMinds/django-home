from django.conf.urls import url

from . import views

app_name = 'tasks'

urlpatterns = [
    url(r'^$', views.ListCreateTask.as_view(), name='task_list'),
    url(r'(?P<pk>\d+)/$', views.RetrieveUpdateDestroyTask.as_view(), name ='task_detail'),
    url(r'(?P<task_pk>\d+)/reviews/$', views.ListCreateReview.as_view(), name ='review_list'),
    url(r'(?P<task_pk>\d+)/reviews/(?P<pk>)/$', views.RetrieveUpdateDestroyReview.as_view(), name ='review_detail'),
]

 #Mag-eerror kapag wala nito due.
# Possible Error: 
# '''
# django.core.exceptions.ImproperlyConfigured: Specifying a namespace in include() without providing an app_name is not supported. Set the app_name attribute in the included module, or pass a 2-tuple containing the list of patterns 
# and app_name instead.
# '''

# from django.conf.urls import url
# from . import views

# urlpatterns = [
#     url(),
# ]

# app_name = 'tasks'