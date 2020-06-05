from django.db.models import BooleanField, CharField, ManyToManyField
from django.urls import reverse

from sghymnal.models import BaseModel
from sghymnal.players.models import Player


class Roster(BaseModel):
    title = CharField(max_length=255)
    season = CharField(max_length=255, blank=True)
    active = BooleanField(default=True)
    default = BooleanField(default=False)
    players = ManyToManyField(Player, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("rosters:detail", kwargs={"uuid": self.uuid})
