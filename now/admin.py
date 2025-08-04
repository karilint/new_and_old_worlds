from django.contrib import admin
from .models import Publication


@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = ("year", "title", "authors")
    list_filter = ("year",)
    search_fields = ("title", "authors", "journal", "doi")
