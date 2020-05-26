import tempfile

from django.core.files.uploadedfile import SimpleUploadedFile
import factory
import factory.fuzzy
from factory import DjangoModelFactory, Faker
from PIL import Image

from ..constants import Position
from ..models import Bio, Player, PlayerImage
from random import randint
from base64 import b64decode
from django.core.files.base import ContentFile


def create_image():
    with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as f:
        image = Image.new("RGB", (200, 200), "white")
        image.save(f, "PNG")
    return open(f.name, mode="rb")


image_data = b64decode("R0lGODlhAQABAIABAP8AAP///yH5BAEAAAEALAAAAAABAAEAAAICRAEAOw==")
image_file = ContentFile(image_data, "one.png")


def test_image():
    return SimpleUploadedFile(
        image_file.name, image_file.read(), content_type="image/png"
    )


class PlayerBioFactory(DjangoModelFactory):
    lang = factory.fuzzy.FuzzyText()
    bio = Faker("paragraphs")

    class Meta:
        model = Bio


class PlayerImageFactory(DjangoModelFactory):
    image = SimpleUploadedFile(
        image_file.name, image_file.read(), content_type="image/png"
    )

    class Meta:
        model = PlayerImage


class PlayerFactory(DjangoModelFactory):

    name = factory.fuzzy.FuzzyText()
    country = factory.Faker("country_code")
    position = factory.fuzzy.FuzzyChoice([x[0] for x in Position.choices])
    squad_number = randint(0, 100)
    thumbnail = SimpleUploadedFile(
        image_file.name, image_file.read(), content_type="image/png"
    )
    team = factory.fuzzy.FuzzyText()
    twitter = factory.fuzzy.FuzzyText()
    instagram = factory.fuzzy.FuzzyText()
    images = factory.RelatedFactory(PlayerImageFactory, "player")
    bios = factory.RelatedFactoryList(PlayerBioFactory, "player")

    class Meta:
        model = Player
