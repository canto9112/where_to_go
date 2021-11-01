from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from places.views import get_detailsUrl, index

urlpatterns = [path('', index),
               path('<int:place_id>/', get_detailsUrl, name='get_detailsUrl')
               ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
