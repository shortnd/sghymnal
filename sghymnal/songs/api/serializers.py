from rest_framework import serializers

from sghymnal.players.api.serializers import PlayerSerializer

from ..models import Song


class SongSerizlizer(serializers.ModelSerializer):
    player = PlayerSerializer(read_only=True)

    class Meta:
        model = Song
        fields = [
            "id",
            "uuid",
            "title",
            "instructions",
            "lyrics",
            "reference_title",
            "reference_link",
            "sheet_music_link",
            "capo_signal",
            "player",
        ]
