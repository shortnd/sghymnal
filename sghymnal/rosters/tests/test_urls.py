import pytest
from django.urls import resolve, reverse

from sghymnal.rosters.models import Roster

pytestmark = pytest.mark.django_db


def test_list():
    assert reverse("rosters:list") == "/rosters/"
    assert resolve("/rosters/").view_name == "rosters:list"


def test_create():
    assert reverse("rosters:create") == "/rosters/create/"
    assert resolve("/rosters/create/").view_name == "rosters:create"


def test_detail(roster: Roster):
    assert (
        reverse("rosters:detail", kwargs={"uuid": roster.uuid})
        == f"/rosters/{roster.uuid}/"
    )
    assert resolve(f"/rosters/{roster.uuid}/").view_name == "rosters:detail"


def test_update(roster: Roster):
    assert (
        reverse("rosters:update", kwargs={"uuid": roster.uuid})
        == f"/rosters/{roster.uuid}/edit/"
    )
    assert resolve(f"/rosters/{roster.uuid}/edit/").view_name == "rosters:update"


def test_delete(roster: Roster):
    assert (
        reverse("rosters:delete", kwargs={"uuid": roster.uuid})
        == f"/rosters/{roster.uuid}/delete/"
    )
    assert resolve(f"/rosters/{roster.uuid}/delete/").view_name == "roster:delete"
