import factory
from factory import DjangoModelFactory
from factory.faker import Faker
from factory.fuzzy import FuzzyText

from sghymnal.songs.tests.factories import SongFactory

from ..models import Chapter, Songbook


class SongbookFactory(DjangoModelFactory):
    title = FuzzyText()
    orginization = FuzzyText()
    description = FuzzyText()

    class Meta:
        model = Songbook


class ChapterFactory(DjangoModelFactory):
    title = FuzzyText()
    songs = factory.RelatedFactoryList(SongFactory)
    songbook = factory.SubFactory(SongbookFactory)

    class Meta:
        model = Chapter
