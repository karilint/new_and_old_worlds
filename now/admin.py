from django.contrib import admin
from import_export import fields, resources
from import_export.admin import ImportExportModelAdmin
from import_export.widgets import ForeignKeyWidget

from .models import Alert, BoardAssignment, BoardNode, Person, Publication, RoleType


class AlertResource(resources.ModelResource):
    class Meta:
        model = Alert
        fields = (
            "id",
            "title",
            "description",
            "start",
            "end",
            "duration_estimate",
        )


@admin.register(Alert)
class AlertAdmin(ImportExportModelAdmin):
    resource_class = AlertResource
    list_display = ("title", "start", "end", "duration_estimate")
    list_filter = ("start", "end")
    search_fields = ("title", "description", "duration_estimate")


class BoardAssignmentInline(admin.TabularInline):
    model = BoardAssignment
    extra = 0
    autocomplete_fields = ("person", "role")
    ordering = ("order", "id")


class PersonAssignmentInline(admin.TabularInline):
    model = BoardAssignment
    fk_name = "person"
    extra = 0
    autocomplete_fields = ("node", "role")
    ordering = ("order", "id")


class PersonResource(resources.ModelResource):
    class Meta:
        model = Person
        fields = ("id", "surname", "first_name", "email", "affiliation", "orcid")
        export_order = fields
        import_id_fields = ("id",)


@admin.register(Person)
class PersonAdmin(ImportExportModelAdmin):
    resource_class = PersonResource
    list_display = ("surname", "first_name", "email", "affiliation", "orcid")
    search_fields = ("surname", "first_name", "email", "affiliation", "orcid")
    ordering = ("surname", "first_name", "id")
    inlines = [PersonAssignmentInline]


class RoleTypeResource(resources.ModelResource):
    class Meta:
        model = RoleType
        fields = ("id", "name", "order")
        export_order = fields
        import_id_fields = ("id",)


@admin.register(RoleType)
class RoleTypeAdmin(ImportExportModelAdmin):
    resource_class = RoleTypeResource
    list_display = ("name", "order")
    list_editable = ("order",)
    search_fields = ("name",)


class BoardNodeResource(resources.ModelResource):
    parent = fields.Field(
        attribute="parent",
        column_name="parent",
        widget=ForeignKeyWidget(BoardNode, "id"),
    )

    class Meta:
        model = BoardNode
        fields = ("id", "name", "node_type", "url", "parent", "order")
        export_order = fields
        import_id_fields = ("id",)


@admin.register(BoardNode)
class BoardNodeAdmin(ImportExportModelAdmin):
    resource_class = BoardNodeResource
    list_display = ("name", "node_type", "url", "parent", "order")
    list_filter = ("node_type",)
    search_fields = ("name", "node_type", "url")
    autocomplete_fields = ("parent",)
    ordering = ("order", "name", "id")
    inlines = [BoardAssignmentInline]


class BoardAssignmentResource(resources.ModelResource):
    person = fields.Field(
        attribute="person",
        column_name="person",
        widget=ForeignKeyWidget(Person, "id"),
    )
    node = fields.Field(
        attribute="node",
        column_name="node",
        widget=ForeignKeyWidget(BoardNode, "id"),
    )
    role = fields.Field(
        attribute="role",
        column_name="role",
        widget=ForeignKeyWidget(RoleType, "id"),
    )

    class Meta:
        model = BoardAssignment
        fields = ("id", "person", "node", "role", "note", "order")
        export_order = fields
        import_id_fields = ("id",)


@admin.register(BoardAssignment)
class BoardAssignmentAdmin(ImportExportModelAdmin):
    resource_class = BoardAssignmentResource
    list_display = ("person", "node", "role", "note", "order")
    list_filter = ("role", "node__node_type")
    search_fields = ("person__surname", "person__first_name", "node__name", "role__name", "note")
    autocomplete_fields = ("person", "node", "role")
    ordering = ("node", "order", "id")


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
