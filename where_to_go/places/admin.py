from django.contrib import admin
from .models import Place, Image


class ImageInstanceInline(admin.TabularInline):
    model = Image


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [ImageInstanceInline]


admin.site.register(Image)

