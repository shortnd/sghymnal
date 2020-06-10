import pytest
from django.urls import resolve, reverse

from ..models import Song

pytestmark = pytest.mark.django_db


def test_songs_list():
    assert reverse("api:song-list") == "/api/songs/"
    assert resolve("/api/songs/").view_name == "api:song-list"


def test_song_detail(song: Song):
    assert (
        reverse("api:song-detail", kwargs={"uuid": song.uuid})
        == f"/api/songs/{song.uuid}/"
    )
    assert resolve(f"/api/songs/{song.uuid}/").view_name == "api:song-detail"
