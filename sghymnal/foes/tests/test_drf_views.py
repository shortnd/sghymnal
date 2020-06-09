import pytest
from django.contrib.auth.models import AnonymousUser
from django.test import RequestFactory

from ..api.views import FoesViewSet
from ..models import Foe

pytestmark = pytest.mark.django_db


class TestFoeViewSet:
    def test_get_queryset(self, foe: Foe, rf: RequestFactory):
        view = FoesViewSet()
        request = rf.get("/api/foes/")
        request.user = AnonymousUser()

        view.request = request

        assert foe in view.get_queryset()

    def test_get_active(self, foe: Foe, rf: RequestFactory):
        view = FoesViewSet()
        request = rf.get("/api/foes/?active=true")
        request.user = AnonymousUser()

        view.request = request

        assert foe in view.get_queryset()

    def test_get_detail(self, foe: Foe, rf: RequestFactory):
        view = FoesViewSet()
        request = rf.get(f"/api/foes/{foe.uuid}/")
        request.user = AnonymousUser()

        view.request = request

        assert foe in view.get_queryset()
