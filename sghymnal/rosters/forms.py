from django.forms import ModelForm

from .models import Roster


class RosterForm(ModelForm):
    class Meta:
        model = Roster
        exclude = ()
