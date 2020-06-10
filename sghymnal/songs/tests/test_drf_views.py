import pytest
from django.contrib.auth.models import AnonymousUser
from django.test import RequestFactory

from ..api.views import SongsViewSet
from ..models import Song
from .factories import SongFactory

pytestmark = pytest.mark.django_db


class TestSongViewSet:
    def test_get_queryset(self, rf: RequestFactory):
        song1 = SongFactory()
        song2 = SongFactory()
        view = SongsViewSet()

        request = rf.get("/api/songs/")
        request.user = AnonymousUser()

        view.request = request

        assert song1 in view.get_queryset()
        assert song2 in view.get_queryset()

    def test_get_detail(self, song: Song, rf: RequestFactory):
        song2 = SongFactory()
        view = SongsViewSet()

        request = rf.get(f"/api/songs/{song.uuid}/")
        request.user = AnonymousUser()

        view.request = request

        assert song in view.get_queryset()
        assert song2 not in view.get_queryset()
