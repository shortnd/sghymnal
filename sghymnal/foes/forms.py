from django.forms import ModelForm, inlineformset_factory

from .models import Foe, FoePlayer


class FoeForm(ModelForm):
    class Meta:
        model = Foe
        fields = (
            "opponent",
            "logo",
            "competition",
            "background_color",
            "accent_color",
            "text_color",
            "season",
            "active",
        )


class FoePlayerForm(ModelForm):
    class Meta:
        model = FoePlayer
        fields = ("name", "position", "squad_number")


FoePlayerFormset = inlineformset_factory(
    parent_model=Foe,
    model=FoePlayer,
    form=FoePlayerForm,
    fields=["name", "position", "squad_number"],
    extra=2,
    can_delete=True,
)
