from django.forms import ModelForm, inlineformset_factory

from .models import Bio, Player, PlayerImage


class PlayerImageForm(ModelForm):
    class Meta:
        model = PlayerImage
        fields = ["image"]


PlayerImageFormSet = inlineformset_factory(
    parent_model=Player,
    model=PlayerImage,
    form=PlayerImageForm,
    fields=["image"],
    extra=2,
    can_delete=True,
)


class PlayerBioForm(ModelForm):
    class Meta:
        model = Bio
        fields = ["lang", "bio"]


PlayerBioFormSet = inlineformset_factory(
    Player, Bio, form=PlayerBioForm, fields=["lang", "bio"], extra=2, can_delete=True
)


class PlayerForm(ModelForm):
    class Meta:
        model = Player
        fields = [
            "name",
            "country",
            "squad_number",
            "position",
            "team",
            "twitter",
            "instagram",
            "thumbnail",
        ]
