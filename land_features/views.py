from django.shortcuts import render
from django.core.serializers import serialize
from django.core import serializers
from .models import Kiserian_Roads
from django.http import HttpResponse


def k_roads(request):
    roads = serializers.serialize("geojson", Kiserian_Roads.objects.all())
    return HttpResponse(roads, content_type='json')
