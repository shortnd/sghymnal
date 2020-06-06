from rest_framework import serializers

from sghymnal.players.api.serializers import PlayerSerializer
from sghymnal.rosters.models import Roster


class RosterSerializer(serializers.ModelSerializer):
    players = PlayerSerializer(many=True, read_only=True)

    class Meta:
        model = Roster
        fields = ["uuid", "id", "title", "season", "active", "default", "players"]
