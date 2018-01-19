# -*- coding: utf-8 -*-
from rest_framework.generics import (ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView)
from rest_framework.permissions import IsAuthenticatedOrReadOnly, BasePermission

from photos.api.permissions import IsOwnerOrReadOnly
from photos.api.serializers import (PhotoSerializer,
                                    PhotoListSerializer,
                                    PhotoDetailSerializer)
from photos.models import Photo
from photos.views import PhotoQuerySet

# TODO: Refactorizar el codigo. y herencia en PhotoListAPI, PhotoDetailAPI


class PhotoListAPI(PhotoQuerySet, ListCreateAPIView):
    queryset = Photo.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_serializer_class(self):
        return PhotoSerializer if self.request.method == 'POST' else PhotoListSerializer

    def get_queryset(self):
        return self.get_photos_queryset(self.request)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PhotoDetailAPI(PhotoQuerySet, RetrieveUpdateDestroyAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)

    def get_queryset(self):
        return self.get_photos_queryset(self.request)
