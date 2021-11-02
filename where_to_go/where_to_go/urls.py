from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.urls import include

from places.views import get_detailsUrl, index

urlpatterns = [
        path('admin/', admin.site.urls),
        path('', index),
        path('tinymce/', include('tinymce.urls')),
        path('<int:place_id>/', get_detailsUrl, name='get_detailsUrl')
        ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
