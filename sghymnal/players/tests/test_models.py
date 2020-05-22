import pytest

from ..models import Player, image_upload_path, thumnail_upload_path

pytestmark = pytest.mark.django_db


def test_player_thumbnail_upload_path(player: Player):
    assert (
        thumnail_upload_path(player, "image.png")
        == f"players/{player.slug}/thumbnail/image.png"
    )


def test_player_upload_path(player: Player):
    assert (
        image_upload_path(player, "image.png")
        == f"players/{player.slug}/images/image.png"
    )


def test_player_get_absolute_url(player: Player):
    assert player.get_absolute_url() == f"/players/{player.uuid}/"


def test_player__str__(player: Player):
    assert player.__str__() == player.name
