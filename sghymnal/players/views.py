from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .models import Player
from .forms import PlayerForm

class PlayersListView(LoginRequiredMixin, ListView):

    model = Player

players_list_view = PlayersListView.as_view()


class PlayerCreateView(LoginRequiredMixin, CreateView):

    model = Player
    form_class = PlayerForm

player_create_view = PlayerCreateView.as_view()


class PlayerDetailView(LoginRequiredMixin, DetailView):

    model = Player

    def get_object(self, queryset=None):
        return Player.objects.get(uuid=self.kwargs.get("uuid"))

player_detail_view = PlayerDetailView.as_view()


class PlayerUpdateView(LoginRequiredMixin, UpdateView):

    model = Player
    form_class = PlayerForm
    action = "Update"

    def get_object(self, queryset=None):
        return Player.objects.get(uuid=self.kwargs.get("uuid"))

player_update_view = PlayerUpdateView.as_view()


class PlayerDeleteView(LoginRequiredMixin, DeleteView):

    model = Player
    success_url = reverse_lazy("players:list")

    def get_object(self, queryset=None):
        return Player.objects.get(uuid=self.kwargs.get("uuid"))

player_delete_view = PlayerDeleteView.as_view()
