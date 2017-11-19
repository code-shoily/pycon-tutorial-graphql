from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User

from .models import *


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        exclude = ('id', )


class ClanSerializer(ModelSerializer):
    class Meta:
        model = Clan
        fields = ('name', 'website', 'email')


class AssetTypeSerializer(ModelSerializer):
    class Meta:
        model = AssetType
        fields = ('name', )


class DeviceSerializer(ModelSerializer):
    class Meta:
        model = Device
        fields = ('imei', 'is_connected', )


class AssetSerializer(ModelSerializer):
    class Meta:
        model = Asset
        fields = ('serial_number', 'clan', 'owner', 'kind',
                  'connected_device', )


class LocationSerializer(ModelSerializer):
    class Meta:
        model = Location
        fields = ('when', 'device', 'lat', 'lng', 'speed', 'event', )
