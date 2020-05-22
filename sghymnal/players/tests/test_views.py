import pytest
from django.contrib.auth.models import AnonymousUser
from django.test import RequestFactory
from django.urls import reverse
from pytest_django.asserts import assertContains

from sghymnal.users.tests.factories import UserFactory

from ..models import Player
from ..views import (
    player_create_view,
    player_delete_view,
    player_detail_view,
    player_update_view,
    players_list_view,
)
from .factories import PlayerFactory

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


def test_list_view_contains_players(rf: RequestFactory):
    player1 = PlayerFactory()
    player2 = PlayerFactory()
    request = rf.get(reverse("players:list"))
    request.user = UserFactory()
    response = players_list_view(request)
    assertContains(response, player1.name)
    assertContains(response, player1.squad_number)
    assertContains(response, player1.position)
    assertContains(response, player2.name)


def test_list_view_has_add_user_button(rf: RequestFactory):
    request = rf.get(reverse("players:list"))
    request.user = UserFactory()
    response = players_list_view(request)
    assertContains(response, "Add Player")


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


def test_create_view_contains_images(rf: RequestFactory):
    request = rf.get(reverse("players:create"))
    request.user = UserFactory()
    response = player_create_view(request)
    assertContains(response, "Images")
    assert response.context_data["images"]


def test_create_view_contains_bios(rf: RequestFactory):
    request = rf.get(reverse("players:create"))
    request.user = UserFactory()
    response = player_create_view(request)
    assertContains(response, "Bios")
    assert response.context_data["bios"]


# class PlayerDetailViewTests:
def test_detail_view_redirects(player: Player, rf: RequestFactory):
    request = rf.get(reverse("players:detail", kwargs={"uuid": player.uuid}))
    request.user = AnonymousUser()
    response = player_detail_view(request, uuid=player.uuid)
    assert response.status_code == 302
    assert response.url == f"/accounts/login/?next=/players/{player.uuid}/"


def test_detail_view_expanded(player: Player, rf: RequestFactory):
    request = rf.get(reverse("players:detail", kwargs={"uuid": player.uuid}))
    request.user = UserFactory()
    response = player_detail_view(request, uuid=player.uuid)
    assertContains(response, f"{player.name}")


def test_detail_view_show_correct_infomation(player: Player, rf: RequestFactory):
    request = rf.get(reverse("players:detail", kwargs={"uuid": player.uuid}))
    request.user = UserFactory()
    response = player_detail_view(request, uuid=player.uuid)
    assertContains(response, player.name)
    assertContains(response, player.position)
    assertContains(response, player.squad_number)
    assertContains(response, f"{player.country.name} - {player.country.flag}")
    assertContains(response, player.team)
    assertContains(response, player.twitter)
    assertContains(response, player.instagram)
    assertContains(response, player.thumbnail)
    assertContains(response, "Edit Player")
    assertContains(response, "Delete Player")


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
    assertContains(response, "Update Player")


def test_update_contains_images_edit(player: Player, rf: RequestFactory):
    request = rf.get(reverse("players:update", kwargs={"uuid": player.uuid}))
    request.user = UserFactory()
    response = player_update_view(request, uuid=player.uuid)
    assert response.context_data["images"]


def test_update_contains_bios_edit(player: Player, rf: RequestFactory):
    request = rf.get(reverse("players:update", kwargs={"uuid": player.uuid}))
    request.user = UserFactory()
    response = player_update_view(request, uuid=player.uuid)
    assert response.context_data["bios"]


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
