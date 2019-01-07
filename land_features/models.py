from django.contrib.gis.db import models

# Create your models here.


class Kiserian_Roads(models.Model):
    id = models.IntegerField(primary_key=True)
    road_name = models.CharField(max_length=80)
    width = models.BigIntegerField()
    road_class = models.CharField(max_length=10)
    road_type = models.CharField(max_length=10)
    lanes = models.BigIntegerField()
    geom = models.MultiLineStringField(srid=4326)

    def __str__(self):
        return self.road_name
