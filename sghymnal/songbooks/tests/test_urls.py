from django.test import RequestFactory
from django.urls import resolve, reverse

from ..models import Songbook
from ..views import (
    songbook_create_view,
    songbook_delete_view,
    songbook_detail_view,
    songbook_update_view,
    songbooks_list_view,
)


def test_songbook_list():
    assert reverse("songbooks:list") == "/songbooks/"
    assert resolve("/songbooks/").view_name == "songbooks:list"


def test_songbook_create():
    assert reverse("songbooks:create") == "/songbooks/create/"
    assert resolve("/songbooks/create/").view_name == "songbooks:create"
