from django.urls import path

from .views import (
    roster_create_view,
    roster_delete_view,
    roster_detail_view,
    roster_list_view,
    roster_update_view,
)

app_name = "rosters"

urlpatterns = [
    path("", view=roster_list_view, name="list"),
    path("create/", view=roster_create_view, name="create"),
    path("<uuid:uuid>/", view=roster_detail_view, name="detail"),
    path("<uuid:uuid>/edit/", view=roster_update_view, name="update"),
    path("<uuid:uuid>/delete/", view=roster_delete_view, name="delete"),
]
