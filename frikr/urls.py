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
from django.urls import path, include

import followers
from users import urls as users_urls
from users.api import urls as users_urls_api
from photos import urls as photos_urls
from photos.api import urls as photos_urls_api
from followers import urls as follow_urls_api

urlpatterns = [
    path('admin/', admin.site.urls),

    # Users
    path('', include(users_urls)),
    path('api/', include(users_urls_api)),
    # Photos
    path('', include(photos_urls)),
    path('api/', include(photos_urls_api)),

    path('api/1.0/', include(follow_urls_api)),

]
