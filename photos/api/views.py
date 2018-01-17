# -*- coding: utf-8 -*-
from rest_framework.generics import (ListCreateAPIView, RetrieveUpdateDestroyAPIView)

from photos.api.serializers import PhotoSerializer
from photos.models import Photo


class PhotoListAPI(ListCreateAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer


class PhotoDetailAPI(RetrieveUpdateDestroyAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
