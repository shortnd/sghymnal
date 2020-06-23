from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)
from django.shortcuts import get_object_or_404

from .forms import SongbookForm, SongbookChapterFormSet
from .models import Songbook
from django.db import transaction


class SongbooksListView(LoginRequiredMixin, ListView):
    model = Songbook


songbooks_list_view = SongbooksListView.as_view()


class SongbookCreateView(LoginRequiredMixin, CreateView):
    model = Songbook
    form_class = SongbookForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context["chapters"] = SongbookChapterFormSet(self.request.POST)
        else:
            context["chapters"] = SongbookChapterFormSet()
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        chapters = context["chapters"]
        with transaction.atomic():
            self.object = form.save()
            if chapters.is_valid():
                chapters.instances = self.object
                chapters.save()
        return super(SongbookCreateView, self).form_valid(form)


songbook_create_view = SongbookCreateView.as_view()


class SongbookDetailView(LoginRequiredMixin, DetailView):
    model = Songbook

    def get_object(self, queryset=None):
        return get_object_or_404(Songbook, uuid=self.kwargs.get("uuid"))


songbook_detail_view = SongbookDetailView.as_view()


class SongbookUpdateView(LoginRequiredMixin, UpdateView):
    model = Songbook
    form_class = SongbookForm
    action = "Update"

    def get_object(self, queryset=None):
        return get_object_or_404(Songbook, uuid=self.kwargs.get("uuid"))


songbook_update_view = SongbookUpdateView.as_view()


class SongbookDeleteView(LoginRequiredMixin, DeleteView):
    model = Songbook
    success_url = reverse_lazy("songbooks:list")

    def get_object(self, queryset=None):
        return get_object_or_404(Songbook, uuid=self.kwargs.get("uuid"))


songbook_delete_view = SongbookDeleteView.as_view()
