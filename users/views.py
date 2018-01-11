# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.contrib.auth import logout as django_logout, login as django_login, authenticate


# Create your views here.


def login(request):
    error_message =[]
    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('pwd')
        user = authenticate(username=username, password=password)
        if user is None:
            error_message.append('Nombre de usuraio o contraseña incorrecta')
        else:
            if user.is_active:
                django_login(request, user)
                return redirect('home')
            else:
                error_message.append('El usuario no esta activo')
    context = {
        'errors': error_message
    }

    return render(request, 'users/login.html', context)


def logout(request):
    if request.user.is_authenticated:
        django_logout(request)
    return redirect('home')
