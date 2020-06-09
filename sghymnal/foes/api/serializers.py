from rest_framework import serializers

from ..models import Foe, FoePlayer


class FoePlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoePlayer
        fields = [
            "id",
            "name",
            "position",
            "squad_number",
        ]


class FoeSerializer(serializers.ModelSerializer):
    players = FoePlayerSerializer(many=True, read_only=True)

    class Meta:
        model = Foe
        fields = [
            "id",
            "uuid",
            "opponent",
            "logo",
            "background_color",
            "accent_color",
            "text_color",
            "season",
            "active",
            "players",
        ]
