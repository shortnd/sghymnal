import pytest
from django.contrib.auth.models import AnonymousUser
from django.test import RequestFactory

from sghymnal.rosters.api.views import RostersViewSet
from sghymnal.rosters.models import Roster

pytestmark = pytest.mark.django_db


class TestRosterViewSet:
    def test_get_queryset(self, roster: Roster, rf: RequestFactory):
        view = RostersViewSet()
        request = rf.get("/api/rosters/")
        request.user = AnonymousUser()

        view.request = request

        assert roster in view.get_queryset()

    def test_get_active(self, roster: Roster, rf: RequestFactory):
        view = RostersViewSet()
        request = rf.get("/api/rosters/?active=true")
        request.user = AnonymousUser()

        view.request = request

        assert roster in view.get_queryset()

    def test_get_detail(self, roster: Roster, rf: RequestFactory):
        view = RostersViewSet()
        request = rf.get(f"/api/rosters/{roster.uuid}")
        request.user = AnonymousUser()

        view.request = request

        assert roster in view.get_queryset()
