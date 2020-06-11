from django.urls import path

from .views import (
    songbook_create_view,
    songbook_delete_view,
    songbook_detail_view,
    songbook_update_view,
    songbooks_list_view,
)

app_name = "songbooks"
urlpatterns = [
    path("", view=songbooks_list_view, name="list"),
    path("create/", view=songbook_create_view, name="create"),
    path("<uuid:uuid>/", view=songbook_detail_view, name="detail"),
    path("<uuid:uuid>/edit/", view=songbook_update_view, name="edit"),
    path("<uuid:uuid>/delete/", view=songbook_delete_view, name="delete"),
]
