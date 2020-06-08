import tempfile
from base64 import b64decode
from random import randint

import factory
import factory.fuzzy
from django.core.files.base import ContentFile
from django.core.files.uploadedfile import SimpleUploadedFile
from factory import DjangoModelFactory
from PIL import Image

from sghymnal.players.constants import Position

from ..models import Foe, FoePlayer


def create_image():
    with tempfile.NamedTemporaryFile(suffix=".jpg", delete=False) as f:
        image = Image.new("RGB", (200, 200), "white")
        image.save()
    return open(f.name, mode="rb")


image_data = b64decode("R0lGODlhAQABAIABAP8AAP///yH5BAEAAAEALAAAAAABAAEAAAICRAEAOw==")
image_file = ContentFile(image_data, "one.png")


def test_image():
    return SimpleUploadedFile(
        image_file.name, image_file.read(), content_type="image/jpg"
    )


def random_hex_color():
    random_number = randint(0, 16777215)
    hex_number = format(random_number, "x")
    return f"#{hex_number}"


class FoePlayerFactory(DjangoModelFactory):
    name = factory.fuzzy.FuzzyText()
    position = factory.fuzzy.FuzzyChoice(x[0] for x in Position.choices)
    squad_number = factory.fuzzy.FuzzyInteger(low=0, high=99)

    class Meta:
        model = FoePlayer


class FoeFactory(DjangoModelFactory):
    opponent = factory.fuzzy.FuzzyText()
    competition = factory.fuzzy.FuzzyText()
    logo = SimpleUploadedFile(
        image_file.name, image_file.read(), content_type="image/jpg"
    )
    background_color = random_hex_color()
    accent_color = random_hex_color()
    text_color = random_hex_color()
    season = factory.fuzzy.FuzzyText()
    active = factory.fuzzy.FuzzyInteger(low=0, high=1)
    players = factory.RelatedFactoryList(FoePlayerFactory, "foe")

    class Meta:
        model = Foe
