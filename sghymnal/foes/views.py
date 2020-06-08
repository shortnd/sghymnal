from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from .models import Foe


class FoesListView(LoginRequiredMixin, ListView):
    model = Foe


foes_list_view = FoesListView.as_view()


class FoeCreateView(CreateView):
    model = Foe


foe_create_view = FoeCreateView.as_view()


class FoeDetailView(DetailView):
    model = Foe


foe_detail_view = FoeDetailView.as_view()


class FoeUpdateView(UpdateView):
    model = Foe


foe_update_view = FoeUpdateView.as_view()


class FoeDeleteView(DeleteView):
    model = Foe


foe_delete_view = FoeDeleteView.as_view()
