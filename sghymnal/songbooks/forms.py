from django.forms import ModelForm, inlineformset_factory

from .models import Songbook, Chapter


class SongbookForm(ModelForm):
    class Meta:
        model = Songbook
        fields = ["title", "organization", "front_cover", "back_cover"]


class ChapterForm(ModelForm):
    class Meta:
        model = Chapter
        fields = ["title"]


SongbookChapterFormSet = inlineformset_factory(
    Songbook, Chapter, form=ChapterForm, fields=["title"], extra=1, can_delete=True,
)
