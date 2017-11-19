from django.contrib import admin

from .models import *


class ClanMemberInline(admin.TabularInline):
    model = ClanMember
    extra = 3


@admin.register(Clan)
class ClanAdmin(admin.ModelAdmin):
    inlines = [
        ClanMemberInline,
    ]


@admin.register(AssetType)
class AssetTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    pass


@admin.register(Asset)
class AssetAdmin(admin.ModelAdmin):
    pass


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    pass
