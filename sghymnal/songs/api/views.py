from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet

from ..models import Song
from .serializers import SongSerizlizer


class SongsViewSet(RetrieveModelMixin, ListModelMixin, GenericViewSet):
    serializer_class = SongSerizlizer
    queryset = Song.objects.all()
    lookup_field = "uuid"
