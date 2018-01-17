from django.contrib.auth.models import User
from django.http import HttpResponse
from django.views.generic import View
from django.shortcuts import get_object_or_404

from users.api.serializers import UserSerializer

from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination


class SampleAPI(View):

    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        serializer_users = serializer.data
        rendered = JSONRenderer()
        json_user = rendered.render(serializer_users)
        return HttpResponse(json_user)


class UserListAPI(APIView):

    def get(self, request):
        # instancio paginador
        paginator = PageNumberPagination()
        users = User.objects.get_queryset().order_by('pk')
        # paginar el queryset
        paginator.paginate_queryset(users, request)
        serializer = UserSerializer(users, many=True)
        serialized_user = serializer.data
        # devolver la respuesta paginada
        return paginator.get_paginated_response(serialized_user)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            new_user = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetailAPI(APIView):

    def get(self, request, username):
        user = get_object_or_404(User, username=username)
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def put(self, request, username):
        user = get_object_or_404(User, username=username)
        serializer = UserSerializer(instance=user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, username):
        user = get_object_or_404(User, username=username)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
