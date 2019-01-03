from django.urls import path
from .views import k_roads

app_name = 'land_features'

urlpatterns = [
    path('kiserian_roads_data/', k_roads, name='roads'),
]
