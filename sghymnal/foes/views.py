from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)
from django.db import transaction

from .models import Foe
from .forms import FoeForm, FoePlayerFormset


class FoesListView(LoginRequiredMixin, ListView):
    model = Foe


foes_list_view = FoesListView.as_view()


class FoeCreateView(LoginRequiredMixin, CreateView):
    model = Foe
    form_class = FoeForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context["players"] = FoePlayerFormset(self.request.POSt)
        else:
            context["players"] = FoePlayerFormset()
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        players = context["players"]
        with transaction.atomic:
            self.object = form.save()
            if players.is_valid():
                players.instance = self.object
                players.save()
            return super(FoeCreateView, self).form_valid(form)


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
