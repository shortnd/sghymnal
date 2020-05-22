from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from .forms import PlayerBioFormSet, PlayerForm, PlayerImageFormSet
from .models import Player


class PlayersListView(LoginRequiredMixin, ListView):

    model = Player


players_list_view = PlayersListView.as_view()


class PlayerCreateView(LoginRequiredMixin, CreateView):

    model = Player
    form_class = PlayerForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context["images"] = PlayerImageFormSet(
                self.request.POST, self.request.FILES
            )
            context["bios"] = PlayerBioFormSet(self.request.POST)
        else:
            context["images"] = PlayerImageFormSet()
            context["bios"] = PlayerBioFormSet()
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        images = context["images"]
        bios = context["bios"]
        with transaction.atomic():
            self.object = form.save()
            if images.is_valid():
                images.instance = self.object
                images.save()
            if bios.is_valid():
                bios.instance = self.object
                bios.save()
        return super(PlayerCreateView, self).form_valid(form)


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

    def get_context_data(self, **kwargs):
        context = super(PlayerUpdateView, self).get_context_data(**kwargs)
        if self.request.POST:
            context["images"] = PlayerImageFormSet(
                self.request.POST, self.request.FILES, instance=self.object
            )
            context["bios"] = PlayerBioFormSet(self.request.POST, instance=self.object)
        else:
            context["images"] = PlayerImageFormSet(instance=self.object)
            context["bios"] = PlayerBioFormSet(instance=self.object)
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        images = context["images"]
        bios = context["bios"]
        with transaction.atomic():
            self.object = form.save()
            if images.is_valid():
                images.instance = self.object
                images.save()
            if bios.is_valid():
                bios.instance = self.object
                bios.save()
        return super(PlayerUpdateView, self).form_valid(form)

    def get_object(self, queryset=None):
        return Player.objects.get(uuid=self.kwargs.get("uuid"))


player_update_view = PlayerUpdateView.as_view()


class PlayerDeleteView(LoginRequiredMixin, DeleteView):

    model = Player
    success_url = reverse_lazy("players:list")

    def get_object(self, queryset=None):
        return Player.objects.get(uuid=self.kwargs.get("uuid"))


player_delete_view = PlayerDeleteView.as_view()
