from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import View, ListView
from django.db.models import Q
# Create your views here.
from photos.form import PhotoForm
from photos.models import Photo, PUBLIC

# import generic classes

from django.contrib.auth.mixins import LoginRequiredMixin


class PhotoQuerySet(object):

    def get_photos_queryset(self, request):
        if not request.user.is_authenticated:
            photos = Photo.objects.filter(visibility=PUBLIC)
        elif request.user.is_superuser:
            photos = Photo.objects.all()
        else:
            photos = Photo.objects.filter(Q(owner=request.user) |
                                          Q(visibility=PUBLIC))
        return photos


class HomeView(View):
    @staticmethod
    def get(request):
        photos = Photo.objects.all().filter(visibility=PUBLIC).order_by('-created_at')
        context = {
            'photos_list': photos[:5]
        }
        return render(request, 'photos/home.html', context)


class DetailView(View, PhotoQuerySet):
    def get(self, request, pk):
        """
        Carga la página de detalle de una foto
        :param request: HttpRequest
        :param pk: id de la foto
        :return: HttpResponse
        """
        posible_photos = self.get_photos_queryset(request).filter(pk=pk).select_related('owner')
        photo = posible_photos[0] if len(posible_photos) >= 1 else None
        if photo is not None:
            context = {
                'photo': photo
            }
            return render(request, 'photos/detail.html', context)
        else:
            return HttpResponseNotFound('No existe la foto')


class OnlyAuthenticatedView(View):

    def get(self, request):
        if request.user.is_authenticated():
            return super(OnlyAuthenticatedView, self).get(request)
        else:
            # TODO: Creación del metodo para no utilizar decoradores.
            pass


class CreatePhotoView(View):

    @method_decorator(login_required())
    def get(self, request):
        """
        Muestra un formualario para crear una foto
        :param request: HttpRequest
        :return: HttpResponse
        """
        success_message = ''
        form = PhotoForm()

        context = {
            'photo_form': form,
        }
        return render(request, 'photos/create.html', context)

    @method_decorator(login_required())
    def post(self, request):
        """
        Crea una foto en base a la información del POST
        :param request: HttpRequest
        :return: HttpResponse
        """
        success_message = ''
        photo_with_owner = Photo()
        photo_with_owner.owner = request.user
        form = PhotoForm(request.POST, instance=photo_with_owner)
        if form.is_valid():
            new_photo = form.save()  # Guarda el objeto y me lo devuelves
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


class ListPhotoView(View, PhotoQuerySet):

    def get(self, request):
        """
        Devuelve:
        - Las fotos públicas si el usurio no está autenticado
        - Las fotos del usuario autenticado o las públicas de otros
        - Si el usuario es superadministrador, todas las fotos
        :param request: HttpRequest
        :return: HttpResponse
        """

        context = {
            'photos': self.get_photos_queryset(request)
        }
        return render(request, 'photos/list.html', context)


class UserPhotoView(LoginRequiredMixin, ListView):
    model = Photo
    template_name = 'photos/user_photos.html'

    def get_queryset(self):
        query_set = super(UserPhotoView, self).get_queryset()
        return query_set.filter(owner=self.request.user)


    # def get_context_data(self, *, object_list=None, **kwargs):
    #     photos = Photo
    #     # TODO añadir articulos relacionados //baners -etc
    #     context = super(UserPhotoView, self).get_context_data(**kwargs)
    #     context['list_related'] = Photo.objects.filter(owner='2')
    #     return context

