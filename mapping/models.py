from django.contrib.gis.db import models

# Create your models here.

class Client(models.Model):
    client = models.AutoField(primary_key=True)
    zone = models.ForeignKey('Zone', models.DO_NOTHING, db_column='zone', blank=True, null=True)
    code = models.CharField(unique=True, max_length=50, blank=True, null=True)
    order = models.IntegerField(blank=True, null=True)
    full_name = models.CharField(max_length=255, blank=True, null=True)
    supply_meter = models.IntegerField(blank=True, null=True)
    id = models.IntegerField(blank=True, null=True)
    is_bulk = models.IntegerField()
    no_deposit = models.IntegerField()
    is_disconnected = models.IntegerField()
    is_refunded = models.IntegerField()
    address = models.CharField(max_length=255, blank=True, null=True)
    plot = models.CharField(max_length=50, blank=True, null=True)
    reg_date = models.DateField(blank=True, null=True)
    deposit = models.FloatField(blank=True, null=True)
    receipt_no = models.CharField(max_length=50, blank=True, null=True)
    is_checked = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'client'

class MobileReadings(models.Model):
    mobile_readings = models.AutoField(primary_key=True)
    code = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    meter = models.CharField(max_length=255, blank=True, null=True)
    mobile = models.CharField(max_length=255, blank=True, null=True)
    date = models.DateField()
    value = models.IntegerField()

    class Meta:
        managed = False
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

    def __str__(self):
        return self.location

    class Meta:
        managed = False
        db_table = 'location'
        unique_together = (('latitude', 'longitude', 'mobile_readings'),)


class Zone(models.Model):
    zone = models.AutoField(primary_key=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    code = models.CharField(unique=True, max_length=50, blank=True, null=True)

    class Meta:
        managed = False
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
        
