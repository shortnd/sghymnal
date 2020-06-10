from factory import DjangoModelFactory, Faker
from factory.fuzzy import FuzzyText

from ..models import Song


class SongFactory(DjangoModelFactory):
    title = FuzzyText()
    instructions = FuzzyText()
    lyrics = Faker("paragraph")
    reference_title = FuzzyText()
    reference_link = Faker("url")
    sheet_music_link = Faker("url")
    legend = FuzzyText()
    capo_signal = FuzzyText()

    class Meta:
        model = Song
