from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

# Create your views here.
from photos.models import Photo, PUBLIC


def home(request):
    photos = Photo.objects.all().filter(visibility=PUBLIC).order_by('-created_at')
    context = {
        'photos_list': photos[:5]
    }
    return render(request, 'photos/home.html', context)


def detail(request, pk):
    """
    Carga la página de detalle de una foto
    :param request: HttpRequest
    :param pk: id de la foto
    :return: HttpResponse
    """
    posible_photos = Photo.objects.filter(pk=pk)
    photo = posible_photos[0] if len(posible_photos) == 1 else None
    if photo is not None:
        context = {
            'photo': photo
        }
        return render(request, 'photos/detail.html', context)
    else:
        return HttpResponseNotFound()
