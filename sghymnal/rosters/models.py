from django.db.models import CharField, BooleanField, ManyToManyField

from sghymnal.models import BaseModel
from sghymnal.players.models import Player


class Roster(BaseModel):
    title = CharField(max_length=255)
    season = CharField(max_length=255, blank=True)
    active = BooleanField(default=True)
    default = BooleanField(default=False)
    players = ManyToManyField(Player)
