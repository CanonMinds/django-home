"""djangogoal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path


#Shopping Store imports
from django.conf.urls.static import static
from django.conf import settings


#Rest New imports
from rest_framework import routers

from tasks import views as task_views
from . import views as team_views
from products import views as products_views

router = routers.SimpleRouter()
router.register(r'tasks', task_views.TaskViewSet)
router.register(r'reviews', task_views.ReviewViewSet)

urlpatterns = [
    url(r'admin/', admin.site.urls, name="admin"),
    # url(r'^auth/', include('newauth.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/v1/tasks/', include(('tasks.urls','tasks'), namespace='tasks')),
    url(r'^api/v2/', include((router.urls, 'tasks'))),

    url(r'^$', team_views.HomeView.as_view(), name='home'),
    url(r'^hello/$', team_views.HelloWorldView.as_view(), name='hello'),
    url(r'teams/', include(('teams.urls', 'teams'), namespace='teams')),
    url(r'products/', include(('products.urls', 'products', namespace='products'))),

    # url(r'tasks/', include('tasks.urls', namespace='tasks')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)