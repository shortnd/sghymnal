import pytest
from django.urls import resolve, reverse

from sghymnal.players.models import Player

pytestmark = pytest.mark.django_db


def test_player_detail(player: Player):
    assert (
        reverse("api:player-detail", kwargs={"uuid": player.uuid})
        == f"/api/players/{player.uuid}/"
    )
    assert resolve(f"/api/players/{player.uuid}/").view_name == "api:player-detail"


def test_player_list():
    assert reverse("api:player-list") == "/api/players/"
    assert resolve("/api/players/").view_name == "api:player-list"
