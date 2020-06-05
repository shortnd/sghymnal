import factory
import factory.fuzzy
from factory import DjangoModelFactory, Faker

from ..models import Roster


class RosterFactory(DjangoModelFactory):
    title = factory.fuzzy.FuzzyText()

    class Meta:
        model = Roster
