import pytest
from django.urls import resolve, reverse

from sghymnal.rosters.models import Roster

pytestmark = pytest.mark.django_db


def test_roster_list():
    assert reverse("api:roster-list") == "/api/rosters/"
    assert resolve("/api/rosters/").view_name == "api:roster-list"


def test_roster_detail(roster: Roster):
    assert (
        reverse("api:roster-detail", kwargs={"uuid": roster.uuid})
        == f"/api/rosters/{roster.uuid}/"
    )
    assert resolve(f"/api/rosters/{roster.uuid}/").view_name == "api:roster-detail"
