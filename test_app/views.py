from django.shortcuts import render

# Create your views here.
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

from photos.models import Photo
from photos.views import PhotoQuerySet

# API Photos
from photos.api.serializers import (PhotoListSerializer,
                                    PhotoSerializer)
# User permissions
from users.api.permissions import UserPermission
from users.api.views import UserListAPI


class PhotoViewSet(PhotoQuerySet, ModelViewSet):
    queryset = Photo.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        return self.get_photos_queryset(self.request)

    def get_serializer_class(self):
        if self.action == 'list':
            return PhotoListSerializer
        else:
            return PhotoSerializer

    def perform_create(self, serializer):
        """
        Asigna automaticamente la autoria de una foto.
        :param serializer:
        :return:
        """
        serializer.save(owner=self.request.user)

