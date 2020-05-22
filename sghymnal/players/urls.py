from django.urls import path

from .views import (
    player_create_view,
    player_delete_view,
    player_detail_view,
    player_update_view,
    players_list_view,
)

app_name = "players"

urlpatterns = [
    path("", view=players_list_view, name="list"),
    path("create/", view=player_create_view, name="create"),
    path("<uuid:uuid>/", view=player_detail_view, name="detail"),
    path("<uuid:uuid>/edit/", view=player_update_view, name="update"),
    path("<uuid:uuid>/delete/", view=player_delete_view, name="delete"),
]
