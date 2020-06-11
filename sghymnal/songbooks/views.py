from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from .forms import SongbookForm
from .models import Songbook


class SongbooksListView(LoginRequiredMixin, ListView):
    model = Songbook


songbooks_list_view = SongbooksListView.as_view()


class SongbookCreateView(LoginRequiredMixin, CreateView):
    model = Songbook
    form_class = SongbookForm


songbook_create_view = SongbookCreateView.as_view()


class SongbookDetailView(DetailView):
    model = Songbook


songbook_detail_view = SongbookDetailView.as_view()


class SongbookUpdateView(UpdateView):
    model = Songbook


songbook_update_view = SongbookUpdateView.as_view()


class SongbookDeleteView(DeleteView):
    model = Songbook
    success_url = reverse_lazy("songbooks:list")


songbook_delete_view = SongbookDeleteView.as_view()
