import factory
import factory.fuzzy
from factory import DjangoModelFactory, Faker

from ..constants import Position
from ..models import Player, Bio, PlayerImage


class PlayerBioFactory(DjangoModelFactory):
    lang = factory.fuzzy.FuzzyText()
    bio = Faker("paragraphs")
    # player = factory.SubFactory(PlayerFactory)

    class Meta:
        model = Bio


class PlayerImageFactory(DjangoModelFactory):
    image = Faker("image_url")

    class Meta:
        model = PlayerImage


class PlayerFactory(DjangoModelFactory):

    name = factory.fuzzy.FuzzyText()
    country = factory.Faker("country_code")
    position = factory.fuzzy.FuzzyChoice([x[0] for x in Position.choices])
    squad_number = factory.fuzzy.FuzzyInteger(low=0, high=100)
    thumbnail = Faker("image_url")
    team = factory.fuzzy.FuzzyText()
    twitter = factory.fuzzy.FuzzyText()
    instagram = factory.fuzzy.FuzzyText()
    bios = factory.RelatedFactoryList(PlayerBioFactory, "player")
    images = factory.RelatedFactoryList(PlayerImageFactory, "player")

    class Meta:
        model = Player
