import pytest
from django.contrib.auth.models import AnonymousUser
from django.test import RequestFactory
from django.urls import reverse
from pytest_django.asserts import assertContains

from sghymnal.users.tests.factories import UserFactory

from ..views import songbook_create_view, songbooks_list_view
from .factories import SongbookFactory

pytestmark = pytest.mark.django_db


class TestSongbooksListView:
    def test_list_view_redirects(self, rf: RequestFactory):
        request = rf.get("/songbooks/")
        request.user = AnonymousUser()

        response = songbooks_list_view(request)

        assert response.status_code == 302
        assert response.url == "/accounts/login/?next=/songbooks/"

    def test_list_view_expanded(self, rf: RequestFactory):
        request = rf.get("/songbooks/")
        request.user = UserFactory()

        response = songbooks_list_view(request)

        assertContains(response, "All Songbooks")

    def test_list_contains_no_songbooks(self, rf: RequestFactory):
        request = rf.get("/songbooks/")
        request.user = UserFactory()

        response = songbooks_list_view(request)

        assertContains(response, "No Songbooks")

    def test_list_contains_songbooks(self, rf: RequestFactory):
        songbook = SongbookFactory()

        request = rf.get("/songbooks/")
        request.user = UserFactory()

        response = songbooks_list_view(request)

        assertContains(response, songbook)

    def test_list_view_has_add_songbook_button(self, rf: RequestFactory):
        request = rf.get("/songbooks/")
        request.user = UserFactory()

        response = songbooks_list_view(request)

        assertContains(response, "Add Songbook")
        assertContains(response, reverse("songbooks:create"))


class TestSongbookCreateView:
    def test_create_view_redirects(self, rf: RequestFactory):
        request = rf.get("/songbooks/create/")
        request.user = AnonymousUser()

        response = songbook_create_view(request)

        assert response.status_code == 302
        assert response.url == "/accounts/login/?next=/songbooks/create/"

    def test_create_view_expanded(self, rf: RequestFactory):
        request = rf.get("/songbooks/create/")
        request.user = UserFactory()

        response = songbook_create_view(request)

        assertContains(response, "Create Songbook")
        assertContains(response, "Title")
        assertContains(response, "Organization")
        assertContains(response, "Front Cover")
        assertContains(response, "Back Cover")
        assertContains(response, "Chapters")
