import pytest

from ..models import (
    Songbook,
    Chapter,
    songbook_front_cover_upload_path,
    songbook_back_cover_upload_path,
)

pytestmark = pytest.mark.django_db


def test_songbook_front_cover_upload_path(songbook: Songbook):
    assert (
        songbook_front_cover_upload_path(songbook, "image.png")
        == f"/{songbook.slug}/front_cover_image.png"
    )


def test_songbook_back_cover_upload_path(songbook: Songbook):
    assert (
        songbook_back_cover_upload_path(songbook, "image.png")
        == f"/{songbook.slug}/back_cover_image.png"
    )


class TestSongbookModel:
    def test__str__(self, songbook: Songbook):
        assert songbook.__str__() == f"{songbook.title}"

    def test_get_absolute_url(self, songbook: Songbook):
        assert songbook.get_absolute_url() == f"/songbooks/{songbook.uuid}/"


class TestChapterModel:
    def test__str__(self, chapter: Chapter):
        assert chapter.__str__() == f"{chapter.title}"
