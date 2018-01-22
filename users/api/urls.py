# -*- coding: utf-8 -*-
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from users.api.views import (UserViewSet,)

# API Router
route = DefaultRouter()
route.register('users', UserViewSet, base_name='users')


urlpatterns = [
    # API
    path('1.0/', include(route.urls)),

]
