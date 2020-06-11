import pytest
from django.contrib.auth.models import AnonymousUser
from django.test import RequestFactory
from pytest_django.asserts import assertContains, assertNotContains

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
        view = SongsViewSet.as_view(actions={"get": "retrieve"}, detail=True)

        request = rf.get(f"/api/songs/{song.uuid}/")
        request.user = AnonymousUser()
        response = view(request, uuid=song.uuid)

        assertContains(response, song)
        assertNotContains(response, song2)
