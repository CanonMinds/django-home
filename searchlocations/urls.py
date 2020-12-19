from django.conf.urls import url

from . import views

app_name = 'searchlocations'

urlpatterns = [
    url(r'search_results/', views.SearchResultsView.as_view(), name='search_result_list'),
    url(r'celery/', views.index, name='celery'),
    url(r'^$', views.ProvincePageView.as_view(), name='province_list'),
]   