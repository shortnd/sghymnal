import pytest
from django.urls import resolve, reverse

from ..models import Foe

pytestmark = pytest.mark.django_db


def test_foes_list():
    assert reverse("api:foe-list") == "/api/foes/"
    assert resolve("/api/foes/").view_name == "api:foe-list"


def test_foe_detail(foe: Foe):
    assert (
        reverse("api:foe-detail", kwargs={"uuid": foe.uuid}) == f"/api/foes/{foe.uuid}/"
    )
    assert resolve(f"/api/foes/{foe.uuid}/").view_name == "api:foe-detail"
