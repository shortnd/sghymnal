from django.contrib import admin

from .models import Foe, FoePlayer


class FoePlayerInline(admin.StackedInline):
    model = FoePlayer


class FoeAdmin(admin.ModelAdmin):
    inlines = [FoePlayerInline]

    class Meta:
        model = Foe


admin.site.register(Foe, FoeAdmin)
