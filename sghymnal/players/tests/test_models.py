import pytest

from ..models import Player, thumnail_upload_path, image_upload_path

pytestmark = pytest.mark.django_db

def test_player_thumbnail_upload_path(player: Player):
    assert thumnail_upload_path(player, "image.png") == f"players/{player.slug}/thumbnail/image.png"

def test_player_upload_path(player: Player):
    assert image_upload_path(player, "image.png") == f"players/{player.slug}/images/image.png"
