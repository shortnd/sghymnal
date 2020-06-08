import factory
import factory.fuzzy
from factory import DjangoModelFactory

from sghymnal.players.constants import Position
from ..models import Foe, FoePlayer


class FoeFactory(DjangoModelFactory):
    opponent = factory.fuzzy.FuzzyText()
    competition = factory.fuzzy.FuzzyText()
    # ADD LOGO
    # ADD BACKGROUND_COLOR
    # ADD ACCENT COLOR
    # ADD TEXT_COLOR
    season = factory.fuzzy.FuzzyText()
    active = factory.fuzzy.FuzzyInteger(min=0, max=1)

    class Meta:
        model = Foe
