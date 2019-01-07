from django.contrib import admin
from .models import Client, Zone, Reading
from land_features.models import Kiserian_Roads
from leaflet.admin import LeafletGeoAdmin
# Register your models here.

admin.site.register(Kiserian_Roads, LeafletGeoAdmin)
admin.site.register(Client)
admin.site.register(Zone)
admin.site.register(Reading)
