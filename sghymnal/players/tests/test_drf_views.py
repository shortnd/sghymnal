import pytest
from django.contrib.auth.models import AnonymousUser
from django.test import RequestFactory

from sghymnal.players.api.views import PlayersViewSet
from sghymnal.players.models import Player

pytestmark = pytest.mark.django_db


class TestPlayerViewSet:
    def test_get_queryset(self, player: Player, rf: RequestFactory):
        view = PlayersViewSet()
        request = rf.get("/api/players/")
        request.user = AnonymousUser()

        view.request = request

        assert player in view.get_queryset()

    def test_get_detail(self, player: Player, rf: RequestFactory):
        view = PlayersViewSet()
        request = rf.get(f"/api/players/{player.uuid}/")
        request.user = AnonymousUser()

        view.request = request

        assert player in view.get_queryset()
