import pytest
from django.contrib.auth.models import AnonymousUser
from django.test import RequestFactory
from django.urls import reverse
from pytest_django.asserts import assertContains

from sghymnal.users.tests.factories import UserFactory

from ..models import Roster
from ..views import (
    roster_create_view,
    roster_delete_view,
    roster_detail_view,
    roster_list_view,
    roster_update_view,
)
from .factories import RosterFactory, RosterPlayerFactory

pytestmark = pytest.mark.django_db


class TestRostersListView:
    def test_list_view_redirects(self, rf: RequestFactory):
        request = rf.get(reverse("rosters:list"))
        request.user = AnonymousUser()
        response = roster_list_view(request)
        assert response.status_code == 302
        assert response.url == "/accounts/login/?next=/rosters/"

    def test_list_view_expanded(self, rf: RequestFactory):
        request = rf.get(reverse("rosters:list"))
        request.user = UserFactory()
        response = roster_list_view(request)
        assertContains(response, "All Rosters")

    def test_list_view_show_no_rosters(self, rf: RequestFactory):
        request = rf.get(reverse("rosters:list"))
        request.user = UserFactory()
        response = roster_list_view(request)
        assertContains(response, "No Rosters")

    def test_list_view_contains_rosters(self, rf: RequestFactory):
        roster1 = RosterFactory()
        request = rf.get(reverse("rosters:list"))
        request.user = UserFactory()
        response = roster_list_view(request)
        assertContains(response, roster1.title)

    def test_list_view_contains_rosters_with_player_count(self, rf: RequestFactory):
        roster_with_player = RosterPlayerFactory()
        request = rf.get(reverse("rosters:list"))
        request.user = UserFactory()
        response = roster_list_view(request)
        assertContains(response, f"- {roster_with_player.players.count()}")

    def test_list_view_has_add_roster_button(self, rf: RequestFactory):
        request = rf.get(reverse("rosters:list"))
        request.user = UserFactory()
        response = roster_list_view(request)
        assertContains(response, "Add Roster")


class TestRostersCreateView:
    def test_create_view_redirects(self, rf: RequestFactory):
        request = rf.get(reverse("rosters:create"))
        request.user = AnonymousUser()
        response = roster_create_view(request)
        assert response.status_code == 302
        assert response.url == "/accounts/login/?next=/rosters/create/"

    def test_create_view_expanded(self, rf: RequestFactory):
        request = rf.get(reverse("rosters:create"))
        request.user = UserFactory()
        response = roster_create_view(request)
        assertContains(response, "Create Roster")


class TestRosterDetailView:
    def test_detail_view_redirects(self, roster: Roster, rf: RequestFactory):
        request = rf.get(reverse("rosters:detail", kwargs={"uuid": roster.uuid}))
        request.user = AnonymousUser()
        response = roster_detail_view(request, uuid=roster.uuid)
        assert response.status_code == 302
        assert response.url == f"/accounts/login/?next=/rosters/{roster.uuid}/"

    def test_detail_view_expanded(self, roster: Roster, rf: RequestFactory):
        request = rf.get(reverse("rosters:detail", kwargs={"uuid": roster.uuid}))
        request.user = UserFactory()
        response = roster_detail_view(request, uuid=roster.uuid)
        assertContains(response, roster.title)

    def test_detail_view_show_correct_infomation(
        self, roster: Roster, rf: RequestFactory
    ):
        request = rf.get(reverse("rosters:detail", kwargs={"uuid": roster.uuid}))
        request.user = UserFactory()
        response = roster_detail_view(request, uuid=roster.uuid)
        assertContains(response, roster.title)
        assertContains(response, roster.season)
        assertContains(response, roster.active)
        assertContains(response, roster.default)


class TestRosterUpdateView:
    def test_update_view_redirects(self, roster: Roster, rf: RequestFactory):
        request = rf.get(reverse("rosters:edit", kwargs={"uuid": roster.uuid}))
        request.user = AnonymousUser()
        response = roster_update_view(request, uuid=roster.uuid)
        assert response.status_code == 302
        assert response.url == f"/accounts/login/?next=/rosters/{roster.uuid}/edit/"

    def test_update_view_expanded(self, roster: Roster, rf: RequestFactory):
        request = rf.get(reverse("rosters:edit", kwargs={"uuid": roster.uuid}))
        request.user = UserFactory()
        response = roster_update_view(request, uuid=roster.uuid)
        assertContains(response, "Update Roster")


class TestRosterDeleteView:
    def test_delete_view_redirects(self, roster: Roster, rf: RequestFactory):
        request = rf.get(reverse("rosters:delete", kwargs={"uuid": roster.uuid}))
        request.user = AnonymousUser()
        response = roster_delete_view(request, uuid=roster.uuid)
        assert response.status_code == 302
        assert response.url == f"/accounts/login/?next=/rosters/{roster.uuid}/delete/"

    def test_delete_view_expanded(self, roster: Roster, rf: RequestFactory):
        request = rf.get(reverse("rosters:delete", kwargs={"uuid": roster.uuid}))
        request.user = UserFactory()
        response = roster_delete_view(request, uuid=roster.uuid)
        assertContains(response, f"Delete {roster.title}")
