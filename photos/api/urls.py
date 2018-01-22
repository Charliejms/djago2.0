from django.urls import path, include
from rest_framework.routers import DefaultRouter
from photos.api.views import PhotoViewSet

# API ROUTER
route = DefaultRouter()
route.register('photos', PhotoViewSet)

urlpatterns = [
    # API
    path('1.0/', include(route.urls)),

]
