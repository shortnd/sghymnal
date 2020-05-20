from django.forms import ModelForm

from .models import Player

class PlayerForm(ModelForm):
    class Meta:
        model = Player
        fields = [
            "name",
            "country",
            "position",
            "squad_number",
            "team",
            "twitter",
            "instagram",
            "thumbnail"
        ]
