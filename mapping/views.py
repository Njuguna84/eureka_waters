from django.shortcuts import render
from django.core.serializers import serialize
from django.core import serializers
from django.http import HttpResponse
from django.views.generic import (TemplateView)
from .models import (kiserian_roads, Client,
                     Location, Zone, MobileReadings)
# Create your views here.


class homeView(TemplateView):
    template_name = "index.html"

def k_roads(request):
    roads = serializers.serialize("geojson", kiserian_roads.objects.all())
    return HttpResponse(roads, content_type = 'json')


def client_meters(request):
    meters = serializers.serialize('geojson', Location.objects.all())
    return HttpResponse(meters, content_type='json')