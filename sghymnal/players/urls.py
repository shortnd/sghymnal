from django.urls import path

from .views import (
    PlayersListView,
    PlayerCreateView,
    PlayerDetailView,
    PlayerUpdateView,
    PlayerDeleteView,
)

app_name = "players"

urlpatterns = [
    path("", PlayersListView.as_view(), name="list"),
    path("create/", PlayerCreateView.as_view(), name="create"),
    path("<uuid:uuid>/", PlayerDetailView.as_view(), name="detail"),
    path("<uuid:uuid>/edit/", PlayerUpdateView.as_view(), name="update"),
    path("<uuid:uuid>/delete/", PlayerDeleteView.as_view(), name="delete"),
]
