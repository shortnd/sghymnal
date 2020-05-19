from django.contrib import admin

from .models import Player

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ["name", "squad_number", "country"]
    seach_fields = ["name"]
