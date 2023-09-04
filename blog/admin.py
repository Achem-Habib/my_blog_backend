from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import Post, Subscriber, Tag


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    prepopulated_fields = {"slug": ["name",]}


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('body', 'table_of_contents',)
    list_display = ("title", "date", "published",)
    list_editable = ("date", "published",)
    prepopulated_fields = {"slug": ["title",]}
    list_filter = ("published",)
    search_fields = ("title",)


@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ("email", "date_time")
