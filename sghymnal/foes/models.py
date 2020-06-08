from autoslug import AutoSlugField
from colorfield.fields import ColorField
from django.db.models import CASCADE, BooleanField, CharField, ForeignKey, IntegerField
from django.urls import reverse
from sorl.thumbnail import ImageField

from sghymnal.models import BaseModel
from sghymnal.players.constants import Position


def foe_upload_path(instance, filename):
    file_type = filename.split(".")[1]
    return f"foes/{instance.slug}_logo.{file_type}"


class Foe(BaseModel):
    opponent = CharField("Opponent Name", max_length=255)
    slug = AutoSlugField(
        "Foe Slug", unique=True, always_update=False, populate_from="opponent"
    )
    competition = CharField("Competition", max_length=255, blank=True)
    logo = ImageField("Foe Logo", upload_to=foe_upload_path, blank=True)
    background_color = ColorField("Background Color", default="#FF0000")
    accent_color = ColorField("Accent Color", default="#FFFF00")
    text_color = ColorField("Text Color", default="#FFFFFF")
    season = CharField("Season", max_length=255)
    active = BooleanField("Active", default=True)

    def __str__(self):
        return self.opponent

    def get_absolute_url(self):
        return reverse("foes:detail", kwargs={"uuid": self.uuid})


class FoePlayer(BaseModel):
    name = CharField(max_length=255)
    squad_number = IntegerField(default=0)
    position = CharField(
        "Position", max_length=50, choices=Position.choices, blank=True
    )
    foe = ForeignKey(Foe, on_delete=CASCADE, related_name="players")

    def __str__(self):
        return f"{self.name} - {self.position} - {self.squad_number}"
