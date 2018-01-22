# -*- coding: utf-8 -*-
from rest_framework.generics import (ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView)
from rest_framework.permissions import IsAuthenticatedOrReadOnly, BasePermission
from rest_framework.viewsets import ModelViewSet

from photos.api.permissions import IsOwnerOrReadOnly
from photos.api.serializers import (PhotoSerializer,
                                    PhotoListSerializer,
                                    PhotoDetailSerializer)
from photos.models import Photo
from photos.views import PhotoQuerySet

# TODO: Refactorizar el codigo. y herencia en PhotoListAPI, PhotoDetailAPI


class PhotoViewSet(PhotoQuerySet, ModelViewSet):
    queryset = Photo.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

    def get_queryset(self):
        return self.get_photos_queryset(self.request)

    def get_serializer_class(self):
        if self.action == 'list':
            return PhotoListSerializer
        else:
            return PhotoSerializer

    def perform_create(self, serializer):
        """
        Asignamos automaticamente el propietario de una foto al usuario autencicado
        :param serializer:
        :return:
        """
        serializer.save(owner=self.request.user)

