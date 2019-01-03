from django.shortcuts import render

# Create your views here.


def k_roads(request):
    roads = serializers.serialize("geojson", kiserian_roads.objects.all())
    return HttpResponse(roads, content_type='json')
