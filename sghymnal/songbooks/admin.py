from django.contrib import admin

from .models import Chapter, Songbook


class ChapterInline(admin.TabularInline):
    model = Chapter
    fields = ("title", "songs")


class SongbookAdmin(admin.ModelAdmin):
    inlines = [ChapterInline]


admin.site.register(Songbook, SongbookAdmin)
# admin.site.register(Chapter)
