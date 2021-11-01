from django.contrib import admin
from .models import Place, Image
from django.utils.safestring import mark_safe


class ImageInstanceInline(admin.TabularInline):
    model = Image
    readonly_fields = ["preview"]

    def preview(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" style="max-height: 200px;">')


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):

    inlines = [ImageInstanceInline]

class ImageAdmin(admin.ModelAdmin):

    readonly_fields = ["preview"]

    def preview(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" style="max-height: 200px;">')


admin.site.register(Image, ImageAdmin)

