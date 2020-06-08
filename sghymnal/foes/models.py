from django.db.models import CharField, BooleanField, IntegerField, ForeignKey, CASCADE

from sghymnal.players.constants import Position
from sghymnal.models import BaseModel
from sorl.thumbnail import ImageField
from autoslug import AutoSlugField


def foe_upload_path(instance):
    return f"foes/{instance.slug}_logo"


class Foe(BaseModel):
    opponent = CharField("Opponent Name", max_length=255)
    slug = AutoSlugField(
        "Foe Slug", unique=True, always_update=False, populate_from="opponent"
    )
    competition = CharField("Competition", max_length=255, blank=True)
    logo = ImageField("Foe Logo", path=foe_upload_path, blank=True)
    background_color = CharField("Background Color", max_length=255)
    accent_color = CharField("Accent Color", max_length=255)
    text_color = CharField("Text Color", max_length=255)
    season = CharField("Season", max_length=255)
    active = BooleanField("Active", default=True)

    def __str__(self):
        return self.opponent


class FoePlayer(BaseModel):
    name = CharField(max_length=255)
    squad_number = IntegerField(default=0)
    position = CharField(max_length=50, choices=Position, blank=True)
    foe = ForeignKey(Foe, on_delete=CASCADE, related_name="players")

    def __str__(self):
        return f"{self.name} - {self.position} - {self.squad_number}"
