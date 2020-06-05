import pytest

from ..models import Roster

pytestmark = pytest.mark.django_db


def test_roster_get_absolute_url(roster: Roster):
    assert roster.get_absolute_url() == f"/rosters/{roster.uuid}/"


def test_roster__str__(roster: Roster):
    assert roster.__str__() == roster.title
