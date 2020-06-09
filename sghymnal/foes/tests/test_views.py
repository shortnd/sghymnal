import pytest
from django.contrib.auth.models import AnonymousUser
from django.test import RequestFactory
from django.urls import reverse
from pytest_django.asserts import assertContains

from sghymnal.foes.models import Foe
from sghymnal.foes.tests.factories import FoeFactory
from sghymnal.foes.views import (
    foe_create_view,
    foe_delete_view,
    foe_detail_view,
    foe_update_view,
    foes_list_view,
)
from sghymnal.users.tests.factories import UserFactory

pytestmark = pytest.mark.django_db


class TestFoesListView:
    def test_foe_list_view_redirects(self, rf: RequestFactory):
        request = rf.get(reverse("foes:list"))
        request.user = AnonymousUser()
        response = foes_list_view(request)
        assert response.status_code == 302
        assert response.url == "/accounts/login/?next=/foes/"

    def test_foe_list_view_expanded(self, rf: RequestFactory):
        request = rf.get(reverse("foes:list"))
        request.user = UserFactory()
        response = foes_list_view(request)
        assertContains(response, "All Foes")

    def test_foe_list_view_contains_no_foes(self, rf: RequestFactory):
        request = rf.get(reverse("foes:list"))
        request.user = UserFactory()
        response = foes_list_view(request)
        assertContains(response, "No Foes")

    def test_foe_list_contains_foes(self, rf: RequestFactory):
        foe1 = FoeFactory()
        foe2 = FoeFactory()
        request = rf.get(reverse("foes:list"))
        request.user = UserFactory()
        response = foes_list_view(request)
        assertContains(response, foe1.opponent)
        assertContains(response, foe1.get_absolute_url())
        assertContains(response, foe2.opponent)
        assertContains(response, foe2.get_absolute_url())

    def test_foe_list_view_has_add_foe_button(self, rf: RequestFactory):
        request = rf.get(reverse("foes:list"))
        request.user = UserFactory()
        response = foes_list_view(request)
        assertContains(response, "Create Foe")


class TestFoeCreateView:
    def test_create_view_redirects(self, rf: RequestFactory):
        request = rf.get(reverse("foes:create"))
        request.user = AnonymousUser()
        response = foe_create_view(request)
        assert response.status_code == 302
        assert response.url == "/accounts/login/?next=/foes/create/"

    def test_create_view_expanded(self, rf: RequestFactory):
        request = rf.get(reverse("foes:create"))
        request.user = UserFactory()
        response = foe_create_view(request)
        assertContains(response, "Create Foe")

    def test_create_view_contains_players(self, rf: RequestFactory):
        request = rf.get(reverse("foes:create"))
        request.user = UserFactory()
        response = foe_create_view(request)
        assertContains(response, "Players")
        assert response.context_data["players"]

    def test_create_view_post(self, rf: RequestFactory):
        form_data = {
            "opponent": "Random Name",
            "competition": "",
            "background_color": "#FF0000",
            "accent_color": "#FFFF00",
            "text_color": "#FFFFFF",
            "season": "2020",
            "active": 1,
            "players-TOTAL_FORMS": 2,
            "players-INITIAL_FORMS": 0,
            "players-MIN_NUM_FORMS": 0,
            "players-MAX_NUM_FORMS": 1000,
            # "players-0-id": "",
            # "players-0-foe": "",
            # "players-0-name": "Test Player",
            # "players-0-position": "Goalkeeper",
            # "players-0-squad_number": 13,
        }
        request = rf.post(reverse("foes:create"), form_data)
        request.user = UserFactory()
        response = foe_create_view(request)
        assert response.status_code == 302


class TestFoeDetailView:
    def test_detail_view_redirects(self, foe: Foe, rf: RequestFactory):
        request = rf.get(reverse("foes:detail", kwargs={"uuid": foe.uuid}))
        request.user = AnonymousUser()
        response = foe_detail_view(request, uuid=foe.uuid)
        assert response.status_code == 302
        assert response.url == f"/accounts/login/?next=/foes/{foe.uuid}/"

    def test_detail_view_expanded(self, foe: Foe, rf: RequestFactory):
        request = rf.get(reverse("foes:detail", kwargs={"uuid": foe.uuid}))
        request.user = UserFactory()
        response = foe_detail_view(request, uuid=foe.uuid)
        assertContains(response, foe.opponent)

    def test_detail_view_show_correct_infomation(self, foe: Foe, rf: RequestFactory):
        request = rf.get(reverse("foes:detail", kwargs={"uuid": foe.uuid}))
        request.user = UserFactory()
        response = foe_detail_view(request, uuid=foe.uuid)
        assertContains(response, f"{foe.opponent}")
        assertContains(response, f"Competition: {foe.competition}")
        assertContains(response, foe.logo)
        assertContains(response, foe.background_color)
        assertContains(response, foe.accent_color)
        assertContains(response, foe.text_color)
        assertContains(response, f"Season: {foe.season}")
        assertContains(response, f"Active: {bool(foe.active)}")

    def test_detail_view_shows_foes_players(self, foe: Foe, rf: RequestFactory):
        request = rf.get(reverse("foes:detail", kwargs={"uuid": foe.uuid}))
        request.user = UserFactory()
        response = foe_detail_view(request, uuid=foe.uuid)
        assertContains(response, foe.players.all()[0].name)

    def test_detail_contains_edit_link(self, foe: Foe, rf: RequestFactory):
        request = rf.get(reverse("foes:detail", kwargs={"uuid": foe.uuid}))
        request.user = UserFactory()
        response = foe_detail_view(request, uuid=foe.uuid)
        assertContains(response, reverse("foes:edit", kwargs={"uuid": foe.uuid}))
        assertContains(response, "Edit Foe")

    def test_detail_contains_delete_link(self, foe: Foe, rf: RequestFactory):
        request = rf.get(reverse("foes:delete", kwargs={"uuid": foe.uuid}))
        request.user = UserFactory()
        response = foe_detail_view(request, uuid=foe.uuid)
        assertContains(response, reverse("foes:delete", kwargs={"uuid": foe.uuid}))
        assertContains(response, "Delete Foe")


class TestFoeUpdateView:
    def test_update_view_redirects(self, foe: Foe, rf: RequestFactory):
        request = rf.get(reverse("foes:edit", kwargs={"uuid": foe.uuid}))
        request.user = AnonymousUser()
        response = foe_update_view(request, uuid=foe.uuid)
        assert response.status_code == 302
        assert response.url == f"/accounts/login/?next=/foes/{foe.uuid}/edit/"

    def test_update_view_expanded(self, foe: Foe, rf: RequestFactory):
        request = rf.get(reverse("foes:edit", kwargs={"uuid": foe.uuid}))
        request.user = UserFactory()
        response = foe_update_view(request, uuid=foe.uuid)
        assertContains(response, "Update Foe")

    def test_update_view_contains_players(self, foe: Foe, rf: RequestFactory):
        request = rf.get(reverse("foes:edit", kwargs={"uuid": foe.uuid}))
        request.user = UserFactory()
        response = foe_update_view(request, uuid=foe.uuid)
        assert response.context_data["players"]

    def test_update_view_post(self, foe: Foe, rf: RequestFactory):
        form_data = {
            "opponent": "Random Name",
            "competition": "",
            "background_color": "#FF0000",
            "accent_color": "#FFFF00",
            "text_color": "#FFFFFF",
            "season": "2020",
            "active": 1,
            "players-TOTAL_FORMS": 2,
            "players-INITIAL_FORMS": 0,
            "players-MIN_NUM_FORMS": 0,
            "players-MAX_NUM_FORMS": 1000,
        }
        request = rf.post(reverse("foes:edit", kwargs={"uuid": foe.uuid}), form_data)
        request.user = UserFactory()
        response = foe_update_view(request, uuid=foe.uuid)
        assert response.status_code == 302
        assert response.url == f"/foes/{foe.uuid}/"


class TestFoeDeleteView:
    def test_delete_view_redirects(self, foe: Foe, rf: RequestFactory):
        request = rf.get(reverse("foes:delete", kwargs={"uuid": foe.uuid}))
        request.user = AnonymousUser()
        response = foe_delete_view(request, uuid=foe.uuid)
        assert response.status_code == 302
        assert response.url == f"/accounts/login/?next=/foes/{foe.uuid}/delete/"

    def test_delete_view_expanded(self, foe: Foe, rf: RequestFactory):
        request = rf.get(reverse("foes:delete", kwargs={"uuid": foe.uuid}))
        request.user = UserFactory()
        response = foe_delete_view(request, uuid=foe.uuid)
        assertContains(response, f"Delete {foe.opponent}")
