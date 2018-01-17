# -*- coding: utf-8 -*-
from rest_framework.generics import (ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView)
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from photos.api.serializers import (PhotoSerializer,
                                    PhotoListSerializer,
                                    PhotoDetailSerializer)
from photos.models import Photo


class PhotoListAPI(ListCreateAPIView):
    queryset = Photo.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_serializer_class(self):
        return PhotoSerializer if self.request.method == 'POST' else PhotoListSerializer


class PhotoDetailAPI(RetrieveUpdateDestroyAPIView):
    queryset = Photo.objects.all()

    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = PhotoDetailSerializer
