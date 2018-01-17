# -*- coding: utf8- -*-
from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.Serializer):

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

    def validate_username(self, data):
        """
        Valida si existe un usuario con ese username
        :param data:
        :return:
        """
        users = User.objects.filter(username=data)
        # Si estoy creando (no hay instancia) compruebo que no haya usuario con ese nombre
        if not self.instance and len(users) != 0:
            raise serializers.ValidationError('Ya existe un usuario con ese username')
        # Si estoy actulizando, el nuevo username es diferente al de la instancia (estoy cambiendo el username)
        # y existen usuario ya reguistrado con el nuevo username
        elif self.instance and self.instance.username != data and len(users) != 0:
            raise serializers.ValidationError('Ya existe un usuario con ese username')
        else:
            return data
