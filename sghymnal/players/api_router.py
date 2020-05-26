from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from sghymnal.players.api.views import PlayersViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("players", PlayersViewSet)

app_name = "player-api"
urlpatterns = router.urls
