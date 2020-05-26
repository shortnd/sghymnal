import pytest
from random import randint

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
from .factories import PlayerFactory, create_image

pytestmark = pytest.mark.django_db


class TestPlayersListView:
    def test_list_view_redirects(self, rf: RequestFactory):
        request = rf.get(reverse("players:list"))
        request.user = AnonymousUser()
        response = players_list_view(request)
        assert response.status_code == 302
        assert response.url == "/accounts/login/?next=/players/"

    def test_list_view_expanded(self, rf: RequestFactory):
        request = rf.get(reverse("players:list"))
        request.user = UserFactory()
        response = players_list_view(request)
        assertContains(response, "All Players")

    def test_list_view_show_now_players(self, rf: RequestFactory):
        request = rf.get(reverse("players:list"))
        request.user = UserFactory()
        response = players_list_view(request)
        assertContains(response, "No Players")

    def test_list_view_contains_players(self, rf: RequestFactory):
        player1 = PlayerFactory()
        player2 = PlayerFactory()
        request = rf.get(reverse("players:list"))
        request.user = UserFactory()
        response = players_list_view(request)
        assertContains(response, player1.name)
        assertContains(response, player1.squad_number)
        assertContains(response, player1.position)
        assertContains(response, player2.name)

    def test_list_view_has_add_user_button(self, rf: RequestFactory):
        request = rf.get(reverse("players:list"))
        request.user = UserFactory()
        response = players_list_view(request)
        assertContains(response, "Add Player")


class TestPlayerCreateView:
    def test_create_view_redirects(self, rf: RequestFactory):
        request = rf.get(reverse("players:create"))
        request.user = AnonymousUser()
        response = player_create_view(request)
        assert response.status_code == 302
        assert response.url == "/accounts/login/?next=/players/create/"

    def test_create_view_expanded(self, rf: RequestFactory):
        request = rf.get(reverse("players:create"))
        request.user = UserFactory()
        response = player_create_view(request)
        assertContains(response, "Create Player")

    def test_create_view_contains_images(self, rf: RequestFactory):
        request = rf.get(reverse("players:create"))
        request.user = UserFactory()
        response = player_create_view(request)
        assertContains(response, "Images")
        assert response.context_data["images"]

    def test_create_view_contains_bios(self, rf: RequestFactory):
        request = rf.get(reverse("players:create"))
        request.user = UserFactory()
        response = player_create_view(request)
        assertContains(response, "Bios")
        assert response.context_data["bios"]

    def test_update_view_post(self, rf: RequestFactory):
        form_data = {
            "name": "Random Name",
            "squad_number": randint(0, 100),
            "images-TOTAL_FORMS": 2,
            "images-INITIAL_FORMS": 0,
            "images-MIN_NUM_FORMS": 0,
            "images-MAX_NUM_FORMS": 1000,
            "bios-TOTAL_FORMS": 2,
            "bios-INITIAL_FORMS": 0,
            "bios-MIN_NUM_FORMS": 0,
            "bios-MAX_NUM_FORMS": 1000,
        }
        request = rf.post(reverse("players:create"), form_data)
        request.user = UserFactory()
        response = player_create_view(request)
        assert response.status_code == 302

    # def test_create_view_post(self, rf: RequestFactory):
    #     proto_player = PlayerFactory()
    #     player_image = create_image()
    #     form_data = {
    #         "name": proto_player.name,
    #         "country": proto_player.country,
    #         "position": proto_player.position,
    #         "squad_number": proto_player.squad_number,
    #         "team": proto_player.team,
    #         "twitter": proto_player.twitter,
    #         "instagram": proto_player.instagram,
    #         "thumbnail": proto_player.thumbnail,
    #         "images-TOTAL_FORMS": 2,
    #         "images-INITIAL_FORMS": 0,
    #         "images-MIN_NUM_FORMS": 0,
    #         "images-MAX_NUM_FORMS": 1000,
    #         # "images-0-id": 0,
    #         # "images-0-player": 0,
    #         # "images-0-image": player_image,
    #         "bios-TOTAL_FORMS": 2,
    #         "bios-INITIAL_FORMS": 0,
    #         "bios-MIN_NUM_FORMS": 0,
    #         "bios-MAX_NUM_FORMS": 1000,
    #         # "bios-0-id": 0,
    #         # "bios-0-player": 0,
    #         # "bios-0-lang": "en",
    #         # "bios-0-bio": "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
    #         # "Nunc hendrerit neque quis sapien vehicula cursus. Vestibulum faucibus"
    #         # "tincidunt felis a laoreet. Sed nec orci sit amet justo sollicitudin commodo."
    #         # "Vivamus facilisis rhoncus arcu, nec feugiat ipsum consequat non. Nullam"
    #         # " id urna tortor. Donec quis enim vel diam rhoncus vehicula ut ac metus. "
    #         # "Sed sed massa vitae mauris euismod laoreet. Praesent porttitor blandit metus,"
    #         # " sed semper leo pellentesque sit amet. Nullam eleifend quam sit amet tortor "
    #         # "volutpat, id pulvinar nulla elementum. Nulla et erat metus.",
    #     }
    #     request = rf.post(reverse("players:create"), form_data)
    #     request.user = UserFactory()
    #     response = player_create_view(request)
    #     assert response.status_code == 302


class TestPlayerDetailView:
    def test_detail_view_redirects(self, player: Player, rf: RequestFactory):
        request = rf.get(reverse("players:detail", kwargs={"uuid": player.uuid}))
        request.user = AnonymousUser()
        response = player_detail_view(request, uuid=player.uuid)
        assert response.status_code == 302
        assert response.url == f"/accounts/login/?next=/players/{player.uuid}/"

    def test_detail_view_expanded(self, player: Player, rf: RequestFactory):
        request = rf.get(reverse("players:detail", kwargs={"uuid": player.uuid}))
        request.user = UserFactory()
        response = player_detail_view(request, uuid=player.uuid)
        assertContains(response, f"{player.name}")

    def test_detail_view_show_correct_infomation(
        self, player: Player, rf: RequestFactory
    ):
        request = rf.get(reverse("players:detail", kwargs={"uuid": player.uuid}))
        request.user = UserFactory()
        response = player_detail_view(request, uuid=player.uuid)
        assertContains(response, player.name)
        assertContains(response, player.position)
        assertContains(response, player.squad_number)
        assertContains(
            response, f'{player.country.name} - <img src="{player.country.flag}" />'
        )
        assertContains(response, player.team)
        assertContains(response, player.twitter)
        assertContains(response, player.instagram)
        assertContains(response, player.thumbnail)
        assertContains(response, "Edit Player")
        assertContains(response, "Delete Player")


class TestPlayerUpdateView:
    def test_update_view_redirects(self, player: Player, rf: RequestFactory):
        request = rf.get(reverse("players:update", kwargs={"uuid": player.uuid}))
        request.user = AnonymousUser()
        response = player_update_view(request, uuid=player.uuid)
        assert response.status_code == 302
        assert response.url == f"/accounts/login/?next=/players/{player.uuid}/edit/"

    def test_update_view_expanded(self, player: Player, rf: RequestFactory):
        request = rf.get(reverse("players:update", kwargs={"uuid": player.uuid}))
        request.user = UserFactory()
        response = player_update_view(request, uuid=player.uuid)
        assertContains(response, "Update Player")

    def test_update_contains_images_edit(self, player: Player, rf: RequestFactory):
        request = rf.get(reverse("players:update", kwargs={"uuid": player.uuid}))
        request.user = UserFactory()
        response = player_update_view(request, uuid=player.uuid)
        assert response.context_data["images"]

    def test_update_contains_bios_edit(self, player: Player, rf: RequestFactory):
        request = rf.get(reverse("players:update", kwargs={"uuid": player.uuid}))
        request.user = UserFactory()
        response = player_update_view(request, uuid=player.uuid)
        assert response.context_data["bios"]

    def test_update_view_post(self, player: Player, rf: RequestFactory):
        form_data = {
            "name": "Random Name",
            "squad_number": randint(0, 100),
            "images-TOTAL_FORMS": 2,
            "images-INITIAL_FORMS": 0,
            "images-MIN_NUM_FORMS": 0,
            "images-MAX_NUM_FORMS": 1000,
            "bios-TOTAL_FORMS": 2,
            "bios-INITIAL_FORMS": 0,
            "bios-MIN_NUM_FORMS": 0,
            "bios-MAX_NUM_FORMS": 1000,
        }
        request = rf.post(
            reverse("players:update", kwargs={"uuid": player.uuid}), form_data
        )
        request.user = UserFactory()
        response = player_update_view(request, uuid=player.uuid)
        assert response.status_code == 302
        assert response.url == f"/players/{player.uuid}/"


class TestPlayerDeleteView:
    def test_delete_view_redirects(self, player: Player, rf: RequestFactory):
        request = rf.get(reverse("players:delete", kwargs={"uuid": player.uuid}))
        request.user = AnonymousUser()
        response = player_delete_view(request, uuid=player.uuid)
        assert response.status_code == 302
        assert response.url == f"/accounts/login/?next=/players/{player.uuid}/delete/"

    def test_delete_view_expanded(self, player: Player, rf: RequestFactory):
        request = rf.get(reverse("players:delete", kwargs={"uuid": player.uuid}))
        request.user = UserFactory()
        response = player_delete_view(request, uuid=player.uuid)
        assertContains(response, f"Delete {player.name}")
