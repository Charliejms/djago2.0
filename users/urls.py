# -*- coding: utf-8 -*-
from django.urls import path
from users.views import (LoginView,
                         LogoutView)

urlpatterns = [
    # User
    path('login/', LoginView.as_view(), name='user_login'),
    path('logout', LogoutView.as_view(), name='user_logout'),
]
