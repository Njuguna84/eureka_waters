from django.urls import path
from .views import client_meters, k_roads

app_name='eureka_maps'

urlpatterns = [
    path('kiserian_roads_data/', k_roads, name='roads'),
    path('client_meters/', client_meters, name='c_meters'),

]