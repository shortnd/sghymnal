import pytest

from sghymnal.users.models import User
from sghymnal.players.models import Player
from sghymnal.users.tests.factories import UserFactory
from sghymnal.players.tests.factories import PlayerFactory


@pytest.fixture(autouse=True)
def media_storage(settings, tmpdir):
    settings.MEDIA_ROOT = tmpdir.strpath


@pytest.fixture
def user() -> User:
    return UserFactory()

@pytest.fixture
def player() -> Player:
    return PlayerFactory()
