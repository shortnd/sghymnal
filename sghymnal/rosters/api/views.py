from django_filters import rest_framework as filters
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.viewsets import GenericViewSet

from ..models import Roster
from .serializers import RosterSerializer


class RostersViewSet(RetrieveModelMixin, ListModelMixin, GenericViewSet):
    serializer_class = RosterSerializer
    queryset = Roster.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ("active", "default")
    lookup_field = "uuid"
    pagination_class = LimitOffsetPagination
    page_size = 10
