import pytest
from pytest_django.asserts import assertContains

from django.contrib.auth.models import AnonymousUser
from django.http.response import Http404
from django.test import RequestFactory
from django.urls import reverse

from sghymnal.users.tests.factories import UserFactory
from ..models import Player
from .factories import PlayerFactory
from ..views import players_list_view, player_create_view, player_detail_view, player_update_view, player_delete_view

pytestmark = pytest.mark.django_db


# class PlayersListViewTests:
def test_list_view_redirects(rf: RequestFactory):
    request = rf.get(reverse("players:list"))
    request.user = AnonymousUser()
    response = players_list_view(request)
    assert response.status_code == 302
    assert response.url == "/accounts/login/?next=/players/"

def test_list_view_expanded(rf: RequestFactory):
    request = rf.get(reverse("players:list"))
    request.user = UserFactory()
    response = players_list_view(request)
    assertContains(response, "All Players")

def test_list_view_show_now_players(rf: RequestFactory):
    request = rf.get(reverse("players:list"))
    request.user = UserFactory()
    response = players_list_view(request)
    assertContains(response, "No Players")

# class PlayerCreateViewTests:
def test_create_view_redirects(rf: RequestFactory):
    request = rf.get(reverse("players:create"))
    request.user = AnonymousUser()
    response = player_create_view(request)
    assert response.status_code == 302
    assert response.url == "/accounts/login/?next=/players/create/"

def test_create_view_expanded(rf: RequestFactory):
    request = rf.get(reverse("players:create"))
    request.user = UserFactory()
    response = player_create_view(request)
    assertContains(response, "Create Player")


# class PlayerDetailViewTests:
def test_detail_view_redirects(player: Player, rf: RequestFactory):
    request = rf.get(reverse("players:detail", kwargs={'uuid': player.uuid}))
    request.user = AnonymousUser()
    response = player_detail_view(request, uuid=player.uuid)
    assert response.status_code == 302
    assert response.url == f"/accounts/login/?next=/players/{player.uuid}/"

def test_detail_view_expanded(player: Player, rf: RequestFactory):
    request = rf.get(reverse("players:detail", kwargs={"uuid": player.uuid}))
    request.user = UserFactory()
    response = player_detail_view(request, uuid=player.uuid)
    assertContains(response, f"{player.name}")


# class PlayerUpdateViewTests:
def test_update_view_redirects(player: Player, rf: RequestFactory):
    request = rf.get(reverse("players:update", kwargs={"uuid": player.uuid}))
    request.user = AnonymousUser()
    response = player_update_view(request, uuid=player.uuid)
    assert response.status_code == 302
    assert response.url == f"/accounts/login/?next=/players/{player.uuid}/edit/"

def test_update_view_expanded(player: Player, rf: RequestFactory):
    request = rf.get(reverse("players:update", kwargs={"uuid": player.uuid}))
    request.user = UserFactory()
    response = player_update_view(request, uuid=player.uuid)
    assertContains(response, f"Update Player")

# class PlayerDeleteViewTests:
def test_delete_view_redirects(player: Player, rf: RequestFactory):
    request = rf.get(reverse("players:delete", kwargs={"uuid": player.uuid}))
    request.user = AnonymousUser()
    response = player_delete_view(request, uuid=player.uuid)
    assert response.status_code == 302
    assert response.url == f"/accounts/login/?next=/players/{player.uuid}/delete/"

def test_delete_view_expanded(player: Player, rf: RequestFactory):
    request = rf.get(reverse("players:delete", kwargs={"uuid": player.uuid}))
    request.user = UserFactory()
    response = player_delete_view(request, uuid=player.uuid)
    assertContains(response, f"Delete {player.name}")
