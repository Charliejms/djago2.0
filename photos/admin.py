from django.contrib import admin
from photos.models import Photo


class PhotoAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'license']
    list_display_links = ['name']
    search_fields = ['name']

    class Meta:
        model = Photo


admin.site.register(Photo, PhotoAdmin)
