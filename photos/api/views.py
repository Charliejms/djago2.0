# -*- coding: utf-8 -*-
from rest_framework.views import APIView
from rest_framework.response import Response

from photos.api.serializers import PhotoSerializer
from photos.models import Photo


class PhotoListAPI(APIView):

    def get(self, request):
        photos = Photo.objects.all()
        serializer = PhotoSerializer(photos, many=True)
        return Response(serializer.data)