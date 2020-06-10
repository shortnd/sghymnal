from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from .forms import SongForm
from .models import Song


def get_song(uuid: str):
    return get_object_or_404(Song, uuid=uuid)


class SongsListView(LoginRequiredMixin, ListView):
    model = Song


songs_list_view = SongsListView.as_view()


class SongCreateView(LoginRequiredMixin, CreateView):
    model = Song
    form_class = SongForm


song_create_view = SongCreateView.as_view()


class SongDetailView(LoginRequiredMixin, DetailView):
    model = Song

    def get_object(self, queryset=None):
        return get_song(self.kwargs.get("uuid"))


song_detail_view = SongDetailView.as_view()


class SongUpdateView(LoginRequiredMixin, UpdateView):
    model = Song
    form_class = SongForm
    action = "Update"

    def get_object(self, queryset=None):
        return get_song(self.kwargs.get("uuid"))


song_update_view = SongUpdateView.as_view()


class SongDeleteView(LoginRequiredMixin, DeleteView):
    model = Song
    success_url = reverse_lazy("songs:list")

    def get_object(self, queryset=None):
        return get_song(self.kwargs.get("uuid"))


song_delete_view = SongDeleteView.as_view()
