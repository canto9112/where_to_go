from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

{{ all_places|json_script:"places-geojson" }}


