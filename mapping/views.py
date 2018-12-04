from django.shortcuts import render
from django.core.serializers import serialize
from django.core import serializers
from django.http import HttpResponse
from django.views.generic import (TemplateView)
from .models import (kiserian_roads, Client, ClientMeters, Location, Zone, MobileReadings)
from django.db import connection
# Create your views here.


class homeView(TemplateView):
    template_name = "index.html"


def k_roads(request):
    roads = serializers.serialize("geojson", kiserian_roads.objects.all())
    return HttpResponse(roads, content_type = 'json')


def client_meters(request):
    meters = serializers.serialize('geojson', ClientMeters.objects.all())
    return HttpResponse(meters, content_type='json')


# connected = 0 and disconneted = 1
# def disconneted_clients(request):
#     meters = serializers.serialize('geojson', ClientMeters.objects.filter(is_disconnected='1'))
#     return HttpResponse(meters, content_type='json')


def disconneted_clients(request):
    q= ClientMeters.objects.filter(is_disconnected='1')
    meters = serializers.serialize('geojson',q)
    return HttpResponse(meters, content_type='json')



def multi_query(request):
    with connection.cursor() as cursor:
        q=cursor.execute("SELECT client.full_name,client.code,zone.description,client.is_bulk,client.is_disconnected,mobile_readings.value, location.location,location.longitude,location.latitude,location.accuracy,location.altitude  FROM public.client, public.location, public.mobile_readings,public.zone WHERE client.zone = zone.zone AND client.code = mobile_readings.code AND location.mobile_readings = mobile_readings.mobile_readings"
       )
    clients = serializers.serialize('geojson', q)
    return HttpResponse(clients, content_type='json')
   
