from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Place


def serialize_place(place):
    return {
        "type": "FeatureCollection",
        "features": [
            {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [place.lng, place.lat]
                },
                "properties": {
                    "title": place.title,
                    "placeId": place.pk,
                    "detailsUrl": reverse('get_detailsUrl', args=[place.pk])
                }
            }]
    }


def index(request):
    all_places = Place.objects.all()
    context = {
        'all_places': [serialize_place(place) for place in all_places]
    }
    return render(request, "index.html", context)


def get_detailsUrl(request, place_id):
    current_place = get_object_or_404(Place, pk=place_id)
    image_place = current_place.images.all()
    image_urls = [place_image.image.url for place_image in image_place]

    response_data = {
        'title': current_place.title,
        'imgs': image_urls,
        'lat': current_place.lat,
        'description_short': current_place.description_short,
        'description_long': current_place.description_long,
        'coordinates': {
            'lat': current_place.lat,
            'lng': current_place.lng
        }
    }
    return JsonResponse(response_data, safe=False, json_dumps_params={'ensure_ascii': False,
                                                                      'indent': 2})
