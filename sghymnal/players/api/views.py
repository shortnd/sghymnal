from rest_framework import status
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from ..models import Player
from .serializers import PlayerSerializer


class PlayersViewSet(RetrieveModelMixin, ListModelMixin, GenericViewSet):
    serializer_class = PlayerSerializer
    queryset = Player.objects.all()
    lookup_field = "uuid"
