from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
from photos.form import PhotoForm
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
    posible_photos = Photo.objects.filter(pk=pk).select_related('owner')
    photo = posible_photos[0] if len(posible_photos) == 1 else None
    if photo is not None:
        context = {
            'photo': photo
        }
        return render(request, 'photos/detail.html', context)
    else:
        return HttpResponseNotFound()


@login_required()
def create(request):
    """
    Muestra un formualario para crear una foto y lo muetra si es POST
    :param request: HttpRequest
    :return: HttpResponse
    """
    success_message = ''
    if request.method == 'GET':
        form = PhotoForm()
    else:
        photo_with_owner = Photo()
        photo_with_owner.owner = request.user
        form = PhotoForm(request.POST, instance=photo_with_owner)
        if form.is_valid():
            new_photo = form.save() # Guarda el objeto y me lo devuelves
            form = PhotoForm()
            success_message = 'Guardado con éxito!'
            success_message += '<a href="{0}">'.format(reverse('detail', args=[new_photo.pk]))
            success_message += 'Ver foto'
            success_message += '</a>'

    context = {
        'photo_form': form,
        'success_message': success_message,

    }
    return render(request, 'photos/create.html', context)
