import pytest

from ..models import Foe

from django.urls import reverse, resolve


class TestFoesUrls:
    def test_foes_list(self):
        assert reverse("foes:list") == "/foes/"
        assert resolve("/foes/").view_name == "foes:list"

    def test_foes_create(self):
        assert reverse("foes:create") == "/foes/create"
        assert resolve("/foes/create/").view_name == "foes:create"

    def test_foes_detail(self, foe: Foe):
        assert reverse("foes:detail", kwargs={"uuid": foe.uuid}) == f"/foes/{foe.uuid}/"
        assert resolve(f"/foes/{foe.uuid}/").view_name == "foes:detail"

    def test_foes_edit(self, foe: Foe):
        assert (
            reverse("foes:edit", kwargs={"uuid": foe.uuid}) == f"/foes/{foe.uuid}/edit/"
        )
        assert resolve(f"/foes/{foe.uuid}/edit/").view_name == "foes:edit"

    def test_foes_delete(self, foe: Foe):
        assert (
            reverse("foes:delete", kwargs={"uuid": foe.uuid})
            == f"/foes/{foe.uuid}/delete/"
        )
        assert resolve(f"/foes/{foe.uuid}/delete/").view_name == "foes:delete"
