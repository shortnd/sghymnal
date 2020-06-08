import pytest

from sghymnal.foes.models import Foe
from sghymnal.foes.tests.factories import FoeFactory
from sghymnal.players.models import Player
from sghymnal.players.tests.factories import PlayerFactory
from sghymnal.rosters.models import Roster
from sghymnal.rosters.tests.factories import RosterFactory
from sghymnal.users.models import User
from sghymnal.users.tests.factories import UserFactory


@pytest.fixture(autouse=True)
def media_storage(settings, tmpdir):
    settings.MEDIA_ROOT = tmpdir.strpath


@pytest.fixture
def user() -> User:
    return UserFactory()


@pytest.fixture
def player() -> Player:
    return PlayerFactory()


@pytest.fixture
def roster() -> Roster:
    return RosterFactory()


@pytest.fixture
def foe() -> Foe:
    return FoeFactory()
