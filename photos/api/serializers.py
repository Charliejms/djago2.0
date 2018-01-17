# -*- coding: utf-8 -*-
from rest_framework import serializers

from photos.models import Photo


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = [
            'owner',
            'name',
            'url',
            'description',
            'created_at',
            'modified_at',
            'license',
            'visibility',


        ]
