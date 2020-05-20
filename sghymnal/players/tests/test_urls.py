import pytest
from django.urls import resolve, reverse

from sghymnal.players.models import Player

pytestmark = pytest.mark.django_db


def test_list():
    assert reverse("players:list") == "/players/"
    assert resolve("/players/").view_name == "players:list"


def test_create():
    assert reverse("players:create") == "/players/create/"
    assert resolve("/players/create/").view_name == "players:create"


def test_detail(player: Player):
    assert (
        reverse("players:detail", kwargs={"uuid": player.uuid})
        == f"/players/{player.uuid}/"
    )
    assert resolve(f"/players/{player.uuid}/").view_name == "players:detail"


def test_update(player: Player):
    assert (
        reverse("players:update", kwargs={"uuid": player.uuid})
        == f"/players/{player.uuid}/edit/"
    )
    assert resolve(f"/players/{player.uuid}/edit/").view_name == "players:update"


def test_delete(player: Player):
    assert (
        reverse("players:delete", kwargs={"uuid": player.uuid})
        == f"/players/{player.uuid}/delete/"
    )
    assert resolve(f"/players/{player.uuid}/delete/").view_name == "players:delete"
