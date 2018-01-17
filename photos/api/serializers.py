# -*- coding: utf-8 -*-
from rest_framework import serializers

from photos.models import Photo


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = '__all__'


class PhotoListSerializer(PhotoSerializer):
    class Meta(PhotoSerializer.Meta):
        fields = [
            'id',
            'name',
            'url',
        ]


class PhotoDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = [
            'id',
            'name',
            'url',
            'created_at',
            'modified_at',
            'license',
            'visibility',
        ]




