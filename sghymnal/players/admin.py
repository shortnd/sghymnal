from django.contrib import admin
from django.contrib.admin import ModelAdmin, TabularInline, StackedInline

from .models import Player, PlayerImage, Bio

class PlayerImageAdmin(TabularInline):
    model = PlayerImage
    fields = ['image']


class PlayerBioAdmin(StackedInline):
    model = Bio
    excludes = ()

@admin.register(Player)
class PlayerAdmin(ModelAdmin):
    list_display = ["name", "squad_number", "country"]
    seach_fields = ["name"]
    inlines = [
        PlayerImageAdmin,
        PlayerBioAdmin
    ]
