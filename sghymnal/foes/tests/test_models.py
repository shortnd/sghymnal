import pytest

from ..models import Foe

pytestmark = pytest.mark.django_db


class TestFoeModel:
    def test__str__(self, foe: Foe):
        assert foe.__str__() == f"{foe.opponent}"

    def test_get_absolute_url(self, foe: Foe):
        assert foe.get_absolute_url() == f"/foes/{foe.uuid}/"


class TestFoePlayerModel:
    def test__str__(self, foe: Foe):
        players = foe.players.all()
        print(players)
        assert (
            players[0].__str__()
            == f"{players[0].name} - {players[0].position} - {players[0].squad_number}"
        )
