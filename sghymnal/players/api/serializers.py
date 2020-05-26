from rest_framework import serializers

from ..models import Player


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ["uuid", "id", "name", "country", "squad_number"]

        extra_kwargs = {
            "url": {"view_name": "api:player-detail", "lookup_field": "uuid"}
        }
