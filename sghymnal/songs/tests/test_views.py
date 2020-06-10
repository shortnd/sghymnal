import pytest
from django.contrib.auth.models import AnonymousUser
from django.test import RequestFactory
from django.urls import reverse
from pytest_django.asserts import assertContains

from sghymnal.users.tests.factories import UserFactory

from ..models import Song
from ..views import (
    song_create_view,
    song_delete_view,
    song_detail_view,
    song_update_view,
    songs_list_view,
)
from .factories import SongFactory

pytestmark = pytest.mark.django_db


class TestSongsListView:
    def test_songs_list_view_redirects(self, rf: RequestFactory):
        request = rf.get(reverse("songs:list"))
        request.user = AnonymousUser()

        response = songs_list_view(request)

        assert response.status_code == 302
        assert response.url == "/accounts/login/?next=/songs/"

    def test_songs_list_expanded(self, rf: RequestFactory):
        request = rf.get(reverse("songs:list"))
        request.user = UserFactory()

        response = songs_list_view(request)

        assertContains(response, "All Songs")

    def test_songs_list_contains_no_songs(self, rf: RequestFactory):
        request = rf.get(reverse("songs:list"))
        request.user = UserFactory()

        response = songs_list_view(request)
        assertContains(response, "No Songs")

    def test_list_contains_songs(self, rf: RequestFactory):
        song = SongFactory()

        request = rf.get(reverse("songs:list"))
        request.user = UserFactory()

        response = songs_list_view(request)
        assertContains(response, song)

    def test_list_contains_create_song_button(self, rf: RequestFactory):
        request = rf.get(reverse("songs:list"))
        request.user = UserFactory()

        response = songs_list_view(request)

        assertContains(response, "Create Song")


class TestSongCreateView:
    def test_song_create_view_redirects(self, rf: RequestFactory):
        request = rf.get(reverse("songs:create"))
        request.user = AnonymousUser()

        response = song_create_view(request)

        assert response.status_code == 302
        assert response.url == "/accounts/login/?next=/songs/create/"

    def test_song_create_expanded(self, rf: RequestFactory):
        request = rf.get(reverse("songs:create"))
        request.user = UserFactory()

        response = song_create_view(request)

        assertContains(response, "Create Song")


class TestSongDetailView:
    def test_song_detail_view_redirects(self, song: Song, rf: RequestFactory):
        request = rf.get(reverse("songs:detail", kwargs={"uuid": song.uuid}))
        request.user = AnonymousUser()

        response = song_detail_view(request, uuid=song.uuid)

        assert response.status_code == 302
        assert response.url == f"/accounts/login/?next=/songs/{song.uuid}/"

    def test_song_detail_view_expanded(self, song: Song, rf: RequestFactory):
        request = rf.get(reverse("songs:detail", kwargs={"uuid": song.uuid}))
        request.user = UserFactory()

        response = song_detail_view(request, uuid=song.uuid)

        assertContains(response, song)

    def test_song_detail_shows_correct_information(
        self, song: Song, rf: RequestFactory
    ):
        request = rf.get(reverse("songs:detail", kwargs={"uuid": song.uuid}))
        request.user = UserFactory()

        response = song_detail_view(request, uuid=song.uuid)

        assertContains(response, song.title)
        assertContains(response, song.instructions)
        assertContains(response, song.lyrics)
        assertContains(response, song.reference_title)
        assertContains(response, song.reference_link)
        assertContains(response, song.sheet_music_link)
        assertContains(response, song.capo_signal)
        # assertContains(response, f"Player: {song.player}")

    def test_song_detail_contains_edit_button(self, song: Song, rf: RequestFactory):
        request = rf.get(reverse("songs:detail", kwargs={"uuid": song.uuid}))
        request.user = UserFactory()

        response = song_detail_view(request, uuid=song.uuid)

        assertContains(response, "Edit Song")
        assertContains(response, f"{reverse('songs:edit', kwargs={'uuid': song.uuid})}")

    def test_song_detail_contains_delete_button(self, song: Song, rf: RequestFactory):
        request = rf.get(reverse("songs:detail", kwargs={"uuid": song.uuid}))
        request.user = UserFactory()

        response = song_detail_view(request, uuid=song.uuid)

        assertContains(response, "Delete Song")
        assertContains(
            response, f"{reverse('songs:delete', kwargs={'uuid': song.uuid})}"
        )


class TestSongUpdateView:
    def test_song_update_view_redirects(self, song: Song, rf: RequestFactory):
        request = rf.get(reverse("songs:edit", kwargs={"uuid": song.uuid}))
        request.user = AnonymousUser()

        response = song_update_view(request, uuid=song.uuid)

        assert response.status_code == 302
        assert response.url == f"/accounts/login/?next=/songs/{song.uuid}/edit/"

    def test_song_update_view_expanded(self, song: Song, rf: RequestFactory):
        request = rf.get(reverse("songs:edit", kwargs={"uuid": song.uuid}))
        request.user = UserFactory()

        response = song_update_view(request, uuid=song.uuid)

        assertContains(response, "Update Song")


class TestSongDeleteView:
    def test_song_delete_view_redirects(self, song: Song, rf: RequestFactory):
        request = rf.get(reverse("songs:delete", kwargs={"uuid": song.uuid}))
        request.user = AnonymousUser()

        response = song_delete_view(request, uuid=song.uuid)

        assert response.status_code == 302
        assert response.url == f"/accounts/login/?next=/songs/{song.uuid}/delete/"

    def test_song_delete_view_expanded(self, song: Song, rf: RequestFactory):
        request = rf.get(reverse("songs:delete", kwargs={"uuid": song.uuid}))
        request.user = UserFactory()

        response = song_delete_view(request, uuid=song.uuid)

        assertContains(response, f"Delete {song.title}")
