from autoslug import AutoSlugField
from django.db.models import CASCADE, CharField, ForeignKey, ManyToManyField
from django.urls import reverse
from sorl.thumbnail import ImageField

from sghymnal.models import BaseModel
from sghymnal.songs.models import Song


def songbook_front_cover_upload_path(instance, filename):
    return f"/{instance.slug}/front_cover_{filename}"


def songbook_back_cover_upload_path(instance, filename):
    return f"/{instance.slug}/back_cover_{filename}"


class Songbook(BaseModel):
    title = CharField("Title", max_length=255)
    slug = AutoSlugField(
        "Songbook Slug", unique=True, always_update=False, populate_from="title"
    )
    organization = CharField("Organization", max_length=255, blank=True)
    description = CharField("Description", max_length=255, blank=True)
    front_cover = ImageField(
        "Front Cover", upload_to=songbook_front_cover_upload_path, blank=True
    )
    back_cover = ImageField(
        "Back Cover", upload_to=songbook_back_cover_upload_path, blank=True
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("songbooks:detail", kwargs={"uuid": self.uuid})


class Chapter(BaseModel):
    title = CharField("Title", max_length=255)
    songs = ManyToManyField(Song)
    songbook = ForeignKey(Songbook, on_delete=CASCADE, related_name="chapters")

    def __str__(self):
        return self.title
