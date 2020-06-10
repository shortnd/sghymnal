from django.urls import path

from .views import (
    song_create_view,
    song_delete_view,
    song_detail_view,
    song_update_view,
    songs_list_view,
)

app_name = "songs"

urlpatterns = [
    path("", view=songs_list_view, name="list"),
    path("create/", view=song_create_view, name="create"),
    path("<uuid:uuid>/", view=song_detail_view, name="detail"),
    path("<uuid:uuid>/edit/", view=song_update_view, name="edit"),
    path("<uuid:uuid>/delete/", view=song_delete_view, name="delete"),
]
