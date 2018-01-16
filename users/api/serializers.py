# -*- coding: utf8- -*-
from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializers(serializers.Serializer):

    id = serializers.ReadOnlyField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()

    def create(self, validated_data):
        """
        Crea una instancia de User a par de los datos de validated_data que
        contiene los valores deserializados
        :param validated_data: Disccionario de datos de usuario
        :return: objeto User
        """
        instance = User()
        return self.update(instance, validated_data)

    def update(self, instance, validated_data):
        """
        Actualiza una instancia del User a partir de los datos de diccionario
        validated_data que contiene valores deserializados
        :param instance:  objeto User a actualizar
        :param validated_data: diccionario con los nuevos valos para el User
        :return: objeto actualizado
        """
        instance.first_name = validated_data.get('first_name')
        instance.last_name = validated_data.get('last_name')
        instance.username = validated_data.get('username')
        instance.email = validated_data.get('email')
        instance.set_password(validated_data.get('password'))
        instance.save()
        return instance
