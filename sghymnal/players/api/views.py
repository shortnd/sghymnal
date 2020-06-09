from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.viewsets import GenericViewSet

from sghymnal.players.api.serializers import PlayerSerializer
from sghymnal.players.models import Player


class PlayersViewSet(RetrieveModelMixin, ListModelMixin, GenericViewSet):
    serializer_class = PlayerSerializer
    queryset = Player.objects.all()
    lookup_field = "uuid"
    pagination_class = LimitOffsetPagination
    page_size = 10
