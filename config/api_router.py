from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from sghymnal.users.api.views import UserViewSet
from sghymnal.players.api.views import PlayersViewSet
from sghymnal.rosters.api.views import RostersViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.register("players", PlayersViewSet)
router.register("rosters", RostersViewSet)


app_name = "api"
urlpatterns = router.urls
