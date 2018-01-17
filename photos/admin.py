from django.contrib import admin
from photos.models import Photo


class PhotoAdmin(admin.ModelAdmin):
    list_display = ['name', 'owner_name', 'visibility', 'description', 'license']
    list_display_links = ['name']
    list_filter = ['license', 'visibility']
    search_fields = ['name']

    def owner_name(self, obj):
        return obj.owner.first_name + obj.owner.last_name

    owner_name.short_description = 'Owner'
    owner_name.admin_order_field = 'owner'

    fieldsets = (
        (None, {
            'fields': ('name',),
            'classes': ('wide',)
        }),
        ('Description & Author', {
            'fields': ('description', 'owner'),
            'classes': ('wide',)
        }),
        ('Extra', {
            'fields': ('url', 'license', 'visibility'),
            'classes': ('wide', 'collapse',)
        }),
    )

    class Meta:
        model = Photo


admin.site.register(Photo, PhotoAdmin)
