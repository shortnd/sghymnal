import factory
import factory.fuzzy
from factory import DjangoModelFactory

from sghymnal.players.tests.factories import PlayerFactory

from ..models import Roster


class RosterFactory(DjangoModelFactory):
    title = factory.fuzzy.FuzzyText()
    season = factory.fuzzy.FuzzyText()
    active = factory.fuzzy.FuzzyInteger(0, 1)
    default = factory.fuzzy.FuzzyInteger(0, 1)

    class Meta:
        model = Roster


class RosterPlayerFactory(DjangoModelFactory):
    title = factory.fuzzy.FuzzyText()
    season = factory.fuzzy.FuzzyText()
    active = factory.fuzzy.FuzzyInteger(0, 1)
    default = factory.fuzzy.FuzzyInteger(0, 1)
    players = factory.RelatedFactoryList(PlayerFactory)

    class Meta:
        model = Roster
