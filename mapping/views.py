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


def client_meters(request):
    # the readings tables is first filtered to get data of the date greater than the set one and for non-null values
        # the does a join operation from the readings(models/table) to Client_Connection and then to
            # Client and finally to the Zone model
                # the queryset is then stored in the variable client_meters_reading
                    # Remember querysets are lazy

    client_meters_reading = Reading.objects.filter(date__gte=datetime.date(
        2018, 10, 31)).filter(geom__isnull=False).select_related('client_connection__client__zone').all()

    # we initialize the data list to the leaflet json
    data = [
        {
            "type": "Feature",
            "properties": {
                "Reading_Value": obj.value,
                "client_name": obj.client_connection.client.full_name,
                "client_code": obj.client_connection.client.code,
                "is_connected": obj.client_connection.client.is_disconnected,
                "is_bulk": obj.client_connection.client.is_bulk,
                "eureka_zones": obj.client_connection.client.zone.description,

            },
            "geometry": {'type': 'Point', 'coordinates': [obj.longitude, obj.latitude]}

        } for obj in client_meters_reading]

    context = {
        "type": "FeatureCollection",
        "features": data}

    return HttpResponse(json.dumps(context), content_type='application/json')
