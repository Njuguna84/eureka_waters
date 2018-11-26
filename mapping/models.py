from django.contrib.gis.db import models

# Create your models here.

class ClientMeters(models.Model):
    full_name = models.CharField(max_length=255, blank=True, null=True)
    code = models.CharField(max_length=50, blank=True, null=True)
    zone = models.CharField(max_length=255, blank=True, null=True)
    is_bulk = models.IntegerField(blank=True, null=True)
    is_disconnected = models.IntegerField(blank=True, null=True)
    value = models.IntegerField(blank=True, null=True)
    location = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    accuracy = models.FloatField(blank=True, null=True)
    altitude = models.FloatField(blank=True, null=True)
    geom = models.PointField(blank=True, null=True)

    class Meta:
        db_table = 'client_meters'
    
    def __str__(self):
        return self.full_name


class Client(models.Model):
    client = models.AutoField(primary_key=True)
    zone = models.ForeignKey('Zone', models.DO_NOTHING, db_column='zone', blank=True, null=True)
    code = models.CharField(unique=True, max_length=50, blank=True, null=True)
    full_name = models.CharField(max_length=255, blank=True, null=True)
    is_bulk = models.IntegerField()
    is_disconnected = models.IntegerField()

    class Meta:
        db_table = 'client'

    def __str__(self):
        return self.full_name

class MobileReadings(models.Model):
    mobile_readings = models.AutoField(primary_key=True)
    code = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    meter = models.CharField(max_length=255, blank=True, null=True)
    mobile = models.CharField(max_length=255, blank=True, null=True)
    date = models.DateField()
    value = models.IntegerField()

    def __unicode__(self):
            return self.mobile_readings

    class Meta:
        db_table = 'mobile_readings'
        unique_together = (('code', 'date'),)

class Location(models.Model):
    location = models.AutoField(primary_key=True)
    longitude = models.FloatField()
    latitude = models.FloatField()
    accuracy = models.FloatField()
    altitude = models.FloatField()
    mobile_readings = models.ForeignKey('MobileReadings', models.DO_NOTHING, db_column='mobile_readings', blank=True, null=True)
    geom = models.PointField(blank=True, null=True)

    def __unicode__(self):
        return self.location

    class Meta:
        db_table = 'location'
        unique_together = (('latitude', 'longitude', 'mobile_readings'),)


class Zone(models.Model):
    zone = models.AutoField(primary_key=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    code = models.CharField(unique=True, max_length=50, blank=True, null=True)
    
    def __str__(self):
            return self.description

    class Meta:
        db_table = 'zone'
    

class kiserian_roads(models.Model):
    gid = models.AutoField(primary_key=True)
    id = models.BigIntegerField(blank=True, null=True)
    road_name = models.CharField(max_length=80)
    width = models.BigIntegerField()
    road_class = models.CharField(max_length=10)
    road_type = models.CharField(max_length=10)
    lanes = models.BigIntegerField()
    geom = models.MultiLineStringField(srid=4326)

    def __str__(self):
        return self.road_name
    
    class Meta:
        verbose_name_plural = "Kiserian Roads"
        
