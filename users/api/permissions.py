# -*- coding: utf-8 -*-
from rest_framework.permissions import BasePermission


class UserPermission(BasePermission):

    def has_permission(self, request, view):
        """
        Define si el usuario autenticado en request.user tiene permiso
        para realizar las acciones (GET, POST, PUT, DELETE)

        :param request:
        :param view:
        :return:
        """
        # Si puede crear un usuario sea quien sea, es decir sea quien sea puede
        if view.action == 'create':
            return True
        # Sin o es un POST, el superuser simpre puede
        elif request.user.is_superuser:
            return True
        # Si es un GET a la vista de detalle, tomo la decisión en has_object_permission
        elif view.action in ['retrieve', 'update', 'destroy']:
            return True
        else:
            # GET a /api/1.0/users/
            False

    def has_object_permission(self, request, view, obj):
        """
        Define si el usuario autenticado en request.user tiene permisso para
        realizar las acciobes (GET, PUT, DELETE) sobre el objeto obj
        :param request:
        :param view:
        :param obj:
        :return:
        """
        return request.user.is_superuser or request.user == obj
