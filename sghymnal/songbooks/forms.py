from django.forms import ModelForm

from .models import Songbook


class SongbookForm(ModelForm):
    class Meta:
        model = Songbook
        fields = ["title", "orginization", "front_cover", "back_cover"]
