import pytest
from django.urls import resolve, reverse

from sghymnal.players.models import Player

pytestmark = pytest.mark.django_db


# def test_players_list():
#     assert reverse("api:player-list") == "/api/players/"
#     assert resolve("/api/players/").view_name == "api:player-list"


def test_player_detail(player: Player):
    assert (
        reverse("player-api:player-detail", kwargs={"uuid": player.uuid})
        == f"/api/players/{player.uuid}/"
    )
    assert (
        resolve(f"/api/players/{player.uuid}/").view_name == "player-api:player-detail"
    )


def test_player_list():
    assert reverse("player-api:player-list") == "/api/players/"
    assert resolve("/api/players/").view_name == "player-api:player-list"
