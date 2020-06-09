from django.db.models import CharField, TextField, URLField, ForeignKey, SET_NULL
from django.urls import reverse

from sghymnal.models import BaseModel
from sghymnal.players.models import Player


class Song(BaseModel):
    title = CharField("Title", max_length=255)
    instructions = CharField("Instructions", max_length=255)
    lyrics = TextField("Lyrics")
    reference_title = CharField("Reference Link", max_length=255, blank=True)
    reference_link = URLField("Reference URL", max_length=255, blank=True)
    sheet_music_link = URLField("Sheet Music Link", max_length=255, blank=True)
    legend = CharField("Legend", max_length=255, blank=True)
    capo_signal = CharField("Capo Signal", max_length=255, blank=True)
    player = ForeignKey(Player, on_delete=SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("songs:detail", kwargs={"uuid": self.uuid})
