"""frikr URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from photos import views as views_photo
from photos.views import (HomeView,
                          DetailView,
                          CreatePhotoView,
                          ListPhotoView,
                          UserPhotoView,)
from users.views import (LoginView,
                         LogoutView)

urlpatterns = [
    path('admin/', admin.site.urls),
    # Photos
    path('', HomeView.as_view(), name='home'),
    path('photo/<pk>', DetailView.as_view(), name='detail'),
    path('photo/create/', CreatePhotoView.as_view(), name='photo_create'),
    # List photos user
    path('photo/list/', ListPhotoView.as_view(), name='photo_list'),
    path('<username>/misfotos/', UserPhotoView.as_view(), name='user_photos'),
    # User
    path('login/', LoginView.as_view(), name='user_login'),
    path('logout', LogoutView.as_view(), name='user_logout'),
]
