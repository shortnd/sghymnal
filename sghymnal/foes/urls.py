from django.urls import path

from .views import (
    foe_create_view,
    foe_delete_view,
    foe_detail_view,
    foe_update_view,
    foes_list_view,
)

app_name = "foes"
urlpatterns = [
    path("", view=foes_list_view, name="list"),
    path("create/", view=foe_create_view, name="create"),
    path("<uuid:uuid>/", view=foe_detail_view, name="detail"),
    path("<uuid:uuid>/edit/", view=foe_update_view, name="edit"),
    path("<uuid:uuid>/delete/", view=foe_delete_view, name="delete"),
]
