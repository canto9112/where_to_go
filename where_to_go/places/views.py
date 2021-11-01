from django.shortcuts import render
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
            "detailsUrl": ""
          }
        }]
    }


def index(request):
    all_places = Place.objects.all()
    context = {
        'all_places': [serialize_place(place) for place in all_places]
    }
    return render(request, "index.html", context)


def get_place_id(request, place_id):
    current_place = Place.objects.get(pk=place_id)
    context = {
        'current_place': current_place
    }
    return render(request, "place.html", context)
