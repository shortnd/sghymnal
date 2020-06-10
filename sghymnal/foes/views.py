from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from .forms import FoeForm, FoePlayerFormset
from .models import Foe


class FoesListView(LoginRequiredMixin, ListView):
    model = Foe


foes_list_view = FoesListView.as_view()


class FoeCreateView(LoginRequiredMixin, CreateView):
    model = Foe
    form_class = FoeForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context["players"] = FoePlayerFormset(self.request.POST)
        else:
            context["players"] = FoePlayerFormset()
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        players = context["players"]
        with transaction.atomic():
            self.object = form.save()
            if players.is_valid():
                players.instance = self.object
                players.save()
        return super(FoeCreateView, self).form_valid(form)


foe_create_view = FoeCreateView.as_view()


class FoeDetailView(LoginRequiredMixin, DetailView):
    model = Foe

    def get_object(self, queryset=None):
        return get_object_or_404(Foe, uuid=self.kwargs.get("uuid"))


foe_detail_view = FoeDetailView.as_view()


class FoeUpdateView(LoginRequiredMixin, UpdateView):
    model = Foe
    form_class = FoeForm
    action = "Update"

    def get_object(self, queryset=None):
        return get_object_or_404(Foe, uuid=self.kwargs.get("uuid"))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context["players"] = FoePlayerFormset(
                self.request.POST, instance=self.object
            )
        else:
            context["players"] = FoePlayerFormset(instance=self.object)
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        players = context["players"]
        with transaction.atomic():
            self.object = form.save()
            if players.is_valid():
                players.instance = self.object
                players.save()
            return super(FoeUpdateView, self).form_valid(form)


foe_update_view = FoeUpdateView.as_view()


class FoeDeleteView(LoginRequiredMixin, DeleteView):
    model = Foe
    success_url = reverse_lazy("foes:list")

    def get_object(self, queryset=None):
        return get_object_or_404(Foe, uuid=self.kwargs.get("uuid"))


foe_delete_view = FoeDeleteView.as_view()
