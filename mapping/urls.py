from django.urls import path
#from .views import k_roads, client_meters, disconneted_clients, multi_query
from .views import client_meters


app_name = 'eureka_maps'

urlpatterns = [
    path('client_meters/', client_meters, name='c_meters'),
    # path('disconnected_clients', disconneted_clients, name='disconnected'),
    # path('multi_query', multi_query, name="multi"),
]
