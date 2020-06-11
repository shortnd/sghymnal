from autoslug import AutoSlugField
from django.db.models import CASCADE, CharField, ForeignKey, ManyToManyField
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
    orginization = CharField("Orginization", max_length=255, blank=True)
    description = CharField("Description", max_length=255, blank=True)
    front_cover = ImageField(
        "Front Cover", upload_to=songbook_front_cover_upload_path, blank=True
    )
    back_cover = ImageField(
        "Back Cover", upload_to=songbook_back_cover_upload_path, blank=True
    )

    def __str__(self):
        return self.title


class Chapter(BaseModel):
    title = CharField("Title", max_length=255)
    songs = ManyToManyField(Song)
    songbook = ForeignKey(Songbook, on_delete=CASCADE, related_name="chapters")

    def __str__(self):
        return self.title
