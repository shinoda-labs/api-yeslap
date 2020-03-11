from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from user.api.viewsets import UserViewset

routers = routers.DefaultRouter(trailing_slash=False)
routers.register(r'user', UserViewset, basename='user')

urlpatterns = [
    path('', include(routers.urls)),
    url(r'^admin/', admin.site.urls),
]
