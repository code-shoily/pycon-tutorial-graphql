from django.db import models


class Clan(models.Model):
    name = models.CharField(max_length=127)
    website = models.URLField(blank=True)
    email = models.EmailField(blank=True)

    def __str__(self):
        return self.name


class ClanMember(models.Model):
    clan = models.ForeignKey(Clan)
    member = models.ForeignKey("auth.User")
    is_leader = models.BooleanField(default=False)


class AssetType(models.Model):
    name = models.CharField(max_length=127)

    def __str__(self):
        return self.name


class Device(models.Model):
    imei = models.CharField(unique=True, max_length=127)
    is_connected = models.BooleanField(default=False)
    added_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.imei


class Asset(models.Model):
    serial_number = models.CharField(unique=True, max_length=127)
    clan = models.ForeignKey(Clan)
    owner = models.ForeignKey("auth.User")
    kind = models.ForeignKey(AssetType)
    connected_device = models.ForeignKey(Device, blank=True, null=True)

    def __str__(self):
        return self.serial_number


class Location(models.Model):
    CHOICES = (
        ('0', 'LOC'),
        ('1', 'HB'),
        ('2', 'ACC'),
        ('3', 'SOS'),
        ('4', 'OFF'),
        ('5', 'ON'),
    )
    when = models.DateTimeField(auto_now=True)
    device = models.ForeignKey(Device)
    lat = models.FloatField()
    lng = models.FloatField()
    speed = models.FloatField()
    event = models.CharField(choices=CHOICES, max_length=127)

    def __str__(self):
        return "({}, {})@{}".format(self.lat, self.lng, self.when)