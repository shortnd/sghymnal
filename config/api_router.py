from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from sghymnal.foes.api.views import FoesViewSet
from sghymnal.players.api.views import PlayersViewSet
from sghymnal.rosters.api.views import RostersViewSet
from sghymnal.users.api.views import UserViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.register("players", PlayersViewSet)
router.register("rosters", RostersViewSet)
router.register("foes", FoesViewSet)


app_name = "api"
urlpatterns = router.urls
