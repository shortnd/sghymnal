from django_filters import rest_framework as filters
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet

from ..models import Foe
from .serializers import FoeSerializer


class FoesViewSet(RetrieveModelMixin, ListModelMixin, GenericViewSet):
    serializer_class = FoeSerializer
    queryset = Foe.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ("active",)
    lookup_field = "uuid"
