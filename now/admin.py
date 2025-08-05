from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import Publication


class PublicationResource(resources.ModelResource):
    class Meta:
        model = Publication
        fields = (
            "id",
            "authors",
            "title",
            "journal",
            "citation",
            "pages",
            "pdf",
            "dataset",
            "year",
            "doi",
        )


@admin.register(Publication)
class PublicationAdmin(ImportExportModelAdmin):
    resource_class = PublicationResource
    list_display = ("year", "title", "authors")
    list_filter = ("year",)
    search_fields = ("title", "authors", "journal", "doi")
