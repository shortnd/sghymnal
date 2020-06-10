from django.forms import ModelForm

from .models import Song


class SongForm(ModelForm):
    class Meta:
        model = Song
        fields = [
            "title",
            "instructions",
            "lyrics",
            "reference_title",
            "reference_link",
            "sheet_music_link",
            "legend",
            "capo_signal",
            "player",
        ]
