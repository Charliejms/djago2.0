from django.urls import path

from photos.views import (HomeView,
                          DetailView,
                          CreatePhotoView,
                          ListPhotoView,
                          UserPhotoView,)

urlpatterns = [

    # Photos
    path('', HomeView.as_view(), name='home'),
    path('photo/<pk>', DetailView.as_view(), name='detail'),
    path('photo/create/', CreatePhotoView.as_view(), name='photo_create'),
    path('photo/list/', ListPhotoView.as_view(), name='photo_list'),
    path('<username>/my_photos/', UserPhotoView.as_view(), name='user_photos'),

]
