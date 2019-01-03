from django.contrib.gis.db import models

# Create your models here.
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.

class Client(models.Model):
    client = models.AutoField(primary_key=True)
    zone = models.ForeignKey('Zone', models.DO_NOTHING, db_column='zone', blank=True, null=True)
    code = models.CharField(unique=True, max_length=255, blank=True, null=True)
    order = models.IntegerField(blank=True, null=True)
    full_name = models.CharField(max_length=255, blank=True, null=True)
    supply_meter = models.ForeignKey('SupplyMeter', models.DO_NOTHING, db_column='supply_meter', blank=True, null=True)
    id = models.IntegerField(blank=True, null=True)
    is_bulk = models.IntegerField()
    no_deposit = models.IntegerField()
    is_disconnected = models.IntegerField()
    is_refunded = models.IntegerField()
    address = models.CharField(max_length=255, blank=True, null=True)
    plot = models.CharField(max_length=255, blank=True, null=True)
    reg_date = models.DateField(blank=True, null=True)
    deposit = models.FloatField(blank=True, null=True)
    receipt_no = models.CharField(max_length=255, blank=True, null=True)
    is_checked = models.IntegerField()
    is_removed = models.IntegerField()

    class Meta:
        db_table = 'client'

    def __str__(self):
        return self.full_name

class ClientConnection(models.Model):
    client_connection = models.AutoField(primary_key=True)
    client = models.ForeignKey(Client, models.DO_NOTHING, db_column='client', blank=True, null=True)
    zone = models.ForeignKey('Zone', models.DO_NOTHING, db_column='zone', blank=True, null=True)
    client_meter = models.ForeignKey('ClientMeter', models.DO_NOTHING, db_column='client_meter', blank=True, null=True)
    meter_serial_no = models.IntegerField(blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    start_reading = models.FloatField(blank=True, null=True)
    end_reading = models.FloatField(blank=True, null=True)

    class Meta:
        db_table = 'client_connection'
        unique_together = (('client', 'end_date'),)

    def __unicode__(self):
        return self.client_connection

class Consumption(models.Model):
    consumption = models.AutoField(primary_key=True)
    client_connection = models.ForeignKey(ClientConnection, models.DO_NOTHING, db_column='client_connection', blank=True, null=True)
    posted_item = models.ForeignKey('PostedItem', models.DO_NOTHING, db_column='posted_item', blank=True, null=True)
    prev_date = models.DateField(blank=True, null=True)
    prev_reading = models.IntegerField(blank=True, null=True)
    curr_date = models.DateField()
    curr_reading = models.IntegerField()
    units = models.FloatField(blank=True, null=True)
    rate = models.IntegerField(blank=True, null=True)
    charge = models.FloatField(blank=True, null=True)

    class Meta:
        db_table = 'consumption'
        unique_together = (('client_connection', 'curr_date'),)

class Reading(models.Model):
    reading = models.AutoField(primary_key=True)
    client_connection = models.ForeignKey(ClientConnection, models.DO_NOTHING, db_column='client_connection', blank=True, null=True)
    consumption = models.ForeignKey(Consumption, models.DO_NOTHING, db_column='consumption', blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    value = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    altitude = models.FloatField(blank=True, null=True)
    accuracy = models.FloatField(blank=True, null=True)
    geom = models.PointField(blank=True, null=True, spatial_index=True, geography=True)

    class Meta:
        db_table = 'reading'
        unique_together = (('date', 'client_connection'),)

    def __unicode__(self):
        return self.reading

class Zone(models.Model):
    zone = models.AutoField(primary_key=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    code = models.CharField(unique=True, max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'zone'

    def __str__(self):
        return self.description


class Adjustment(models.Model):
    adjustment = models.AutoField(primary_key=True)
    posted_item = models.ForeignKey('PostedItem', models.DO_NOTHING, db_column='posted_item', blank=True, null=True)
    client = models.ForeignKey('Client', models.DO_NOTHING, db_column='client', blank=True, null=True)
    purpose = models.CharField(max_length=255, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    debit = models.FloatField(blank=True, null=True)
    credit = models.FloatField(blank=True, null=True)

    class Meta:
        db_table = 'adjustment'
        unique_together = (('client', 'date', 'purpose'),)


class BalanceInitial(models.Model):
    balance_initial = models.AutoField(primary_key=True)
    client = models.ForeignKey('Client', models.DO_NOTHING, db_column='client', blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    debit = models.FloatField(blank=True, null=True)
    credit = models.FloatField(blank=True, null=True)
    is_posted = models.IntegerField()

    class Meta:
        db_table = 'balance_initial'
        unique_together = (('client', 'date'),)


class Change(models.Model):
    change = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    value = models.IntegerField(blank=True, null=True)
    is_bulk = models.IntegerField()

    class Meta:
        db_table = 'change'
        unique_together = (('name', 'end_date'),)



class ClientMeter(models.Model):
    client_meter = models.AutoField(primary_key=True)
    serial_no = models.CharField(unique=True, max_length=255, blank=True, null=True)
    client_start_date = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'client_meter'


class Invoice(models.Model):
    invoice = models.AutoField(primary_key=True)
    client = models.ForeignKey(Client, models.DO_NOTHING, db_column='client', blank=True, null=True)
    period = models.ForeignKey('Period', models.DO_NOTHING, db_column='period', blank=True, null=True)

    class Meta:
        db_table = 'invoice'
        unique_together = (('client', 'period'),)


class Job(models.Model):
    job = models.AutoField(primary_key=True)
    job_name = models.CharField(unique=True, max_length=255)
    class_name = models.CharField(max_length=255)
    method = models.CharField(max_length=255)
    querystring = models.CharField(max_length=255)

    class Meta:
        db_table = 'job'


class Location(models.Model):
    location = models.AutoField(primary_key=True)
    longitude = models.FloatField()
    latitude = models.FloatField()
    accuracy = models.FloatField()
    altitude = models.FloatField()
    mobile_readings = models.ForeignKey('MobileReadings', models.DO_NOTHING, db_column='mobile_readings', blank=True, null=True)

    class Meta:
        db_table = 'location'
        unique_together = (('latitude', 'longitude', 'mobile_readings'),)


class Message(models.Model):
    message = models.AutoField(primary_key=True)
    title = models.CharField(unique=True, max_length=50, blank=True, null=True)
    body = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'message'


class MessageValidation(models.Model):
    message_validation = models.AutoField(primary_key=True)
    mobile = models.ForeignKey('Mobile', models.DO_NOTHING, db_column='mobile', blank=True, null=True)
    message = models.ForeignKey(Message, models.DO_NOTHING, db_column='message', blank=True, null=True)
    is_sent = models.IntegerField(blank=True, null=True)
    date = models.DateField()

    class Meta:
        db_table = 'message_validation'
        unique_together = (('mobile', 'message', 'date'),)


class Mobile(models.Model):
    mobile = models.AutoField(primary_key=True)
    number = models.CharField(unique=True, max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'mobile'


class MobileReadings(models.Model):
    mobile_readings = models.AutoField(primary_key=True)
    code = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    meter = models.CharField(max_length=255, blank=True, null=True)
    mobile = models.CharField(max_length=255, blank=True, null=True)
    date = models.DateField()
    value = models.IntegerField()

    class Meta:
        db_table = 'mobile_readings'
        unique_together = (('code', 'date'),)


class MobileValidation(models.Model):
    mobile_validation = models.AutoField(primary_key=True)
    mobile = models.ForeignKey(Mobile, models.DO_NOTHING, db_column='mobile', blank=True, null=True)
    is_valid = models.IntegerField(blank=True, null=True)
    client = models.ForeignKey(Client, models.DO_NOTHING, db_column='client', blank=True, null=True)

    class Meta:
        db_table = 'mobile_validation'
        unique_together = (('mobile', 'client'),)


class Month(models.Model):
    month = models.AutoField(primary_key=True)
    num = models.IntegerField(unique=True, blank=True, null=True)
    name = models.CharField(unique=True, max_length=255, blank=True, null=True)
    long_name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'month'


class Note(models.Model):
    note = models.AutoField(primary_key=True)
    start_date = models.DateField()
    end_date = models.DateField()
    info = models.CharField(unique=True, max_length=255)

    class Meta:
        db_table = 'note'


class Payment(models.Model):
    payment = models.AutoField(primary_key=True)
    client = models.ForeignKey(Client, models.DO_NOTHING, db_column='client', blank=True, null=True)
    posted_item = models.ForeignKey('PostedItem', models.DO_NOTHING, db_column='posted_item', blank=True, null=True)
    amount = models.FloatField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    ref = models.CharField(unique=True, max_length=255, blank=True, null=True)
    marked = models.IntegerField()

    class Meta:
        db_table = 'payment'


class Period(models.Model):
    period = models.AutoField(primary_key=True)
    month = models.ForeignKey(Month, models.DO_NOTHING, db_column='month', blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    is_current = models.IntegerField()
    is_initial = models.IntegerField()

    class Meta:
        db_table = 'period'
        unique_together = (('year', 'month'),)


class PostedItem(models.Model):
    posted_item = models.AutoField(primary_key=True)
    invoice = models.ForeignKey(Invoice, models.DO_NOTHING, db_column='invoice', blank=True, null=True)
    source = models.ForeignKey('Source', models.DO_NOTHING, db_column='source', blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    code = models.CharField(max_length=255)
    is_posted = models.IntegerField()
    debit = models.FloatField(blank=True, null=True)
    credit = models.FloatField(blank=True, null=True)

    class Meta:
        db_table = 'posted_item'
        unique_together = (('invoice', 'source', 'code'),)


class Source(models.Model):
    source = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=255)
    title = models.CharField(max_length=255)
    sequence = models.IntegerField()

    class Meta:
        db_table = 'source'


class Subscription(models.Model):
    subscription = models.AutoField(primary_key=True)
    client = models.ForeignKey(Client, models.DO_NOTHING, db_column='client', blank=True, null=True)
    service = models.IntegerField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)

    class Meta:
        db_table = 'subscription'
        unique_together = (('client', 'service', 'start_date'),)


class SupplyMeter(models.Model):
    supply_meter = models.AutoField(primary_key=True)
    id = models.CharField(unique=True, max_length=255, blank=True, null=True)
    description = models.CharField(unique=True, max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'supply_meter'


class SupplyReading(models.Model):
    supply_reading = models.AutoField(primary_key=True)
    supply_meter = models.ForeignKey(SupplyMeter, models.DO_NOTHING, db_column='supply_meter', blank=True, null=True)
    reading = models.CharField(max_length=255, blank=True, null=True)
    date = models.DateField(blank=True, null=True)

    class Meta:
        db_table = 'supply_reading'
        unique_together = (('supply_meter', 'date'),)


class ZoneConnection(models.Model):
    zone_connection = models.AutoField(primary_key=True)
    valid = models.IntegerField()
    supply_meter = models.ForeignKey(SupplyMeter, models.DO_NOTHING, db_column='supply_meter', blank=True, null=True)
    zone = models.ForeignKey(Zone, models.DO_NOTHING, db_column='zone', blank=True, null=True)

    class Meta:
        db_table = 'zone_connection'
        unique_together = (('supply_meter', 'valid', 'zone'),)

