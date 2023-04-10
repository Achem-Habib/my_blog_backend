from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import Post, Tag


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    prepopulated_fields = {"slug": ["name",]}



@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('body', 'table_of_contents',)
    list_display = ("title", "date", "published", "most_popular")
    list_editable = ("date", "published", "most_popular")
    prepopulated_fields = {"slug": ["title",]}
    list_filter = ("published", "most_popular")
    search_fields = ("title",)




