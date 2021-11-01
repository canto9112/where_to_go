from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
# from where_to_go.views import index
from places.views import index, get_place_id

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", index),
    path('places/<int:place_id>/', get_place_id)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
