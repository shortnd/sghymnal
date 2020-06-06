from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from .api.views import RostersViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("rosters", RostersViewSet)

app_name = "roster-api"
urlpatterns = router.urls
