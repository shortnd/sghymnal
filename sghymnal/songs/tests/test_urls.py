import pytest
from django.urls import resolve, reverse

from ..models import Song

pytestmark = pytest.mark.django_db


def test_songs_list_url():
    assert reverse("songs:list") == "/songs/"
    assert resolve("/songs/").view_name == "songs:list"


def test_songs_create_url():
    assert reverse("songs:create") == "/songs/create/"
    assert resolve("/songs/create/").view_name == "songs:create"


def test_songs_detail_url(song: Song):
    assert reverse("songs:detail", kwargs={"uuid": song.uuid}) == f"/songs/{song.uuid}/"
    assert resolve(f"/songs/{song.uuid}/").view_name == "songs:detail"


def test_songs_update_url(song: Song):
    assert (
        reverse("songs:edit", kwargs={"uuid": song.uuid}) == f"/songs/{song.uuid}/edit/"
    )
    assert resolve(f"/songs/{song.uuid}/edit/").view_name == "songs:edit"


def test_songs_delete_url(song: Song):
    assert (
        reverse("songs:delete", kwargs={"uuid": song.uuid})
        == f"/songs/{song.uuid}/delete/"
    )
    assert resolve(f"/songs/{song.uuid}/delete/").view_name == "songs:delete"
