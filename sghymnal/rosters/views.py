from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from .forms import RosterForm
from .models import Roster


class RosterListView(LoginRequiredMixin, ListView):
    model = Roster


roster_list_view = RosterListView.as_view()


class RosterCreateView(LoginRequiredMixin, CreateView):
    model = Roster
    form_class = RosterForm


roster_create_view = RosterCreateView.as_view()


class RosterDetailView(LoginRequiredMixin, DetailView):
    model = Roster

    def get_object(self, queryset=None):
        return Roster.objects.get(uuid=self.kwargs.get("uuid"))


roster_detail_view = RosterDetailView.as_view()


class RosterUpdateView(LoginRequiredMixin, UpdateView):
    model = Roster
    form_class = RosterForm

    def get_object(self, queryset=None):
        return Roster.objects.get(uuid=self.kwargs.get("uuid"))


roster_update_view = RosterUpdateView.as_view()


class RosterDeleteView(LoginRequiredMixin, DeleteView):
    model = Roster
    success_url = reverse_lazy("rosters:list")

    def get_object(self, queryset=None):
        return Roster.objects.get(uuid=self.kwargs.get("uuid"))


roster_delete_view = RosterDeleteView.as_view()
