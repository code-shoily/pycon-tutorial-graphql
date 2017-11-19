import graphene
from graphene import relay
import graphene_django
from django.contrib.auth.models import User
from graphene_django.rest_framework.mutation import SerializerMutation

from .models import *
from .serializers import *


class UserNode(graphene_django.DjangoObjectType):
    class Meta:
        model = User
        interfaces = (relay.Node, )


class UserConnection(relay.Connection):
    class Meta:
        node = UserNode


class ClanNode(graphene_django.DjangoObjectType):
    class Meta:
        model = Clan
        interfaces = (relay.Node, )


class ClanConnection(relay.Connection):
    class Meta:
        node = ClanNode


class AssetTypeNode(graphene_django.DjangoObjectType):
    class Meta:
        model = AssetType
        interfaces = (relay.Node, )


class AssetTypeConnection(relay.Connection):
    class Meta:
        node = AssetTypeNode


class DeviceNode(graphene_django.DjangoObjectType):
    class Meta:
        model = Device
        interfaces = (relay.Node, )


class DeviceConnection(relay.Connection):
    class Meta:
        node = DeviceNode


class AssetNode(graphene_django.DjangoObjectType):
    class Meta:
        model = Asset
        interfaces = (relay.Node, )


class AssetConnection(relay.Connection):
    class Meta:
        node = AssetNode


class LocationNode(graphene_django.DjangoObjectType):
    class Meta:
        model = Location
        interfaces = (relay.Node, )


class LocationConnection(relay.Connection):
    class Meta:
        node = LocationNode


class AppRootQuery(graphene.ObjectType):
    users = relay.ConnectionField(UserConnection)
    clans = relay.ConnectionField(ClanConnection)
    devices = relay.ConnectionField(DeviceConnection)
    asset_types = relay.ConnectionField(AssetTypeConnection)
    assets = relay.ConnectionField(AssetConnection)
    locations = relay.ConnectionField(LocationConnection)

    def resolve_users(self, info, **kwargs):
        return User.objects.all()

    def resolve_clans(self, info, **kwargs):
        return Clan.objects.all()

    def resolve_devices(self, info, **kwargs):
        return Device.objects.all()

    def resolve_asset_types(self, info, **kwargs):
        return AssetType.objects.all()

    def resolve_locations(self, info, **kwargs):
        return Location.objects.all()


class ClanMutation(SerializerMutation):
    class Meta:
        serializer_class = ClanSerializer


class AssetTypeMutation(SerializerMutation):
    class Meta:
        serializer_class = AssetTypeSerializer


class AssetMutation(SerializerMutation):
    class Meta:
        serializer_class = AssetSerializer


class LocationMutation(SerializerMutation):
    class Meta:
        serializer_class = LocationSerializer


class DeviceMutation(SerializerMutation):
    class Meta:
        serializer_class = DeviceSerializer


class AppRootMutation(graphene.ObjectType):
    clan_mutation = ClanMutation.Field()
    asset_type_mutation = AssetTypeMutation.Field()


schema = graphene.Schema(query=AppRootQuery, mutation=AppRootMutation)
