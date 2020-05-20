from django.db.models import CharField, Model, ForeignKey, CASCADE, IntegerField, TextField
from django.urls import reverse

from autoslug import AutoSlugField
from django_countries.fields import CountryField
from sorl.thumbnail import ImageField

from sghymnal.models import BaseModel
from .constants import Position

def thumnail_upload_path(instance, filename):
    return f'players/{instance.slug}/thumbnail/{filename}'

def image_upload_path(instance, filename):
    return f'players/{instance.slug}/images/{filename}'

class Player(BaseModel):

    name = CharField("Player Name", max_length=255)
    slug = AutoSlugField("Player Slug", unique=True, always_update=False, populate_from="name")
    country = CountryField("Player Country", blank=True)
    position = CharField("Position", max_length=50, choices=Position.choices, blank=True)
    squad_number = IntegerField("Players Number", blank=True)
    team = CharField("Player's Team", max_length=255, blank=True, null=True)
    twitter = CharField("Twitter", max_length=255, blank=True)
    instagram = CharField("Instagram", max_length=255, blank=True)
    thumbnail = ImageField("Player Thumbnail", upload_to=thumnail_upload_path, blank=True)


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("players:detail", kwargs={"uuid": self.uuid})



class PlayerImage(Model):
    image = ImageField("Player Image", upload_to=image_upload_path)
    player = ForeignKey(
        Player,
        on_delete=CASCADE,
        related_name='images'
    )


class Bio(Model):
    lang = CharField("Bio Language", max_length=50)
    bio = TextField("Bio")
    player = ForeignKey(
        Player,
        on_delete=CASCADE,
        related_name='bios'
    )
