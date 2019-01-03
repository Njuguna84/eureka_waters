from django.shortcuts import render
import datetime
from django.core.serializers import serialize
from django.core import serializers
from django.http import HttpResponse
from django.views.generic import (TemplateView)
from .models import Client, ClientConnection, Reading, Zone
from django.db import connection
import json
from django.contrib.gis.geos import Point
from shapely.geometry.geo import mapping, shape
# Create your views here.


def index(request):
    return render(request, 'mapping/index.html')


def client_meters1(request):
    # meters = serializers.serialize('geojson', Reading.objects.all())
    meters = serializers.serialize('geojson', Reading.objects.filter(date__gte=datetime.date(
        2018, 10, 31)).filter(geom__isnull=False).select_related('client_connection__client__zone')[:2])

    return HttpResponse(meters, content_type='application/json')


def client_meters(request):
    client_meters_reading = Reading.objects.filter(date__gte=datetime.date(
        2018, 10, 31)).filter(geom__isnull=False).select_related('client_connection__client__zone').all()

    # data = []

    # for reading in client_meters_reading:
    #     data = [{
    #         "type": "Feature",
    #         "properties": {
    #             "client name": reading.client_connection.client.full_name,
    #             "is connected": reading.client_connection.client.is_disconnected,
    #             "is bulk": reading.client_connection.client.is_bulk,
    #             "zone": reading.client_connection.client.zone.description
    #         },
    #         "geometry": mapping(shape({'type': 'Point', 'coordinates': [reading.longitude, reading.latitude]}))
    #     }]

    data = [
        {
            "type": "Feature",
            "properties": {
                "client_name": obj.client_connection.client.full_name,
                "client_code": obj.client_connection.client.code,
                "is_connected": obj.client_connection.client.is_disconnected,
                "is_bulk": obj.client_connection.client.is_bulk,
                "zone": obj.client_connection.client.zone.description
            },
            "geometry": {'type': 'Point', 'coordinates': [obj.longitude, obj.latitude]}

        } for obj in client_meters_reading]

    context = {
        "type": "FeatureCollection",
        "features": data}

    return HttpResponse(json.dumps(context), content_type='application/json')
