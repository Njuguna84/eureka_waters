import os
from django.contrib.gis.utils import LayerMapping
from .models import Kiserian_Roads

kiserian_roads_mapping = {
    'id': 'id',
    'road_name': 'road_name',
    'width': 'Width',
    'road_class': 'road_class',
    'road_type': 'road_type',
    'lanes': 'Lanes',
    'geom': 'MULTILINESTRING',
}

kiserian_roads_shp = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__), 'data', 'Kiserian_roads.shp'
    ),
)


def run(verbose=True):
    lm = LayerMapping(
        Kiserian_Roads, kiserian_roads_shp, kiserian_roads_mapping,
        transform=False, encoding='utf-8',
    )
    lm.save(strict=True, verbose=verbose)
