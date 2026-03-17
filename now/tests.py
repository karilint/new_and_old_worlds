from django.core.exceptions import ValidationError
from django.test import TestCase, override_settings
from django.urls import reverse
from import_export.admin import ImportExportModelAdmin

from .admin import (
    BoardAssignmentAdmin,
    BoardAssignmentResource,
    BoardNodeAdmin,
    BoardNodeResource,
    PersonAdmin,
    PersonResource,
    PublicationAdmin,
    PublicationResource,
    RoleTypeAdmin,
    RoleTypeResource,
)
from .models import BoardAssignment, BoardNode, Person, Publication, RoleType


TEST_STORAGES = {
    "default": {"BACKEND": "django.core.files.storage.FileSystemStorage"},
    "staticfiles": {"BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage"},
}


@override_settings(STORAGES=TEST_STORAGES)
class PublicationViewTests(TestCase):
    def setUp(self):
        Publication.objects.create(
            authors="Doe, J.",
            title="Example Publication",
            journal="Journal of Tests",
            citation="1(1), 1-2",
            year=2024,
            pdf="example.pdf",
            dataset="data.csv",
            doi="10.1234/example",
        )

    def test_publications_page_lists_entries(self):
        response = self.client.get(reverse("publications"))
        self.assertContains(response, "Example Publication")
        self.assertContains(response, "2024")
        self.assertContains(response, '[PDF]')
        self.assertContains(response, '/static/now/pdf/example.pdf')
        self.assertContains(response, '[dataset]')
        self.assertContains(response, '/static/now/datasets/data.csv')
        self.assertContains(response, '[doi:10.1234/example]')
        self.assertContains(response, 'https://doi.org/10.1234/example')

    def test_invalid_doi_rejected(self):
        pub = Publication(
            authors="Doe, J.",
            title="Bad DOI",
            year=2024,
            doi="invalid",
        )
        with self.assertRaises(ValidationError):
            pub.full_clean()


@override_settings(STORAGES=TEST_STORAGES)
class BoardViewTests(TestCase):
    def test_board_page_links_orcid_and_project_url(self):
        role = RoleType.objects.create(name="Coordinator", order=1)
        person = Person.objects.create(
            surname="Doe",
            first_name="Jane",
            orcid="0000-0002-1825-0097",
        )
        project = BoardNode.objects.create(
            name="Example Project",
            node_type="project",
            url="https://example.org/project",
        )
        BoardAssignment.objects.create(person=person, node=project, role=role)

        response = self.client.get(reverse("board"))

        self.assertContains(
            response,
            'href="https://orcid.org/0000-0002-1825-0097" target="_blank" rel="noopener noreferrer">Jane Doe</a>',
        )
        self.assertContains(
            response,
            'href="https://example.org/project" target="_blank" rel="noopener noreferrer"',
        )

    def test_board_page_ignores_url_for_non_project_nodes(self):
        person = Person.objects.create(surname="Doe")
        node = BoardNode.objects.create(
            name="Region Alpha",
            node_type="region",
            url="https://example.org/region",
        )
        BoardAssignment.objects.create(person=person, node=node)

        response = self.client.get(reverse("board"))

        self.assertNotContains(response, 'href="https://example.org/region"')
        self.assertContains(response, 'Region Alpha')


@override_settings(STORAGES=TEST_STORAGES)
class BoardAdminImportExportTests(TestCase):
    def setUp(self):
        self.role = RoleType.objects.create(id=7, name="Coordinator", order=1)
        self.person = Person.objects.create(
            id=11,
            surname="Doe",
            first_name="Jane",
            email="jane@example.org",
            affiliation="Example University",
            orcid="0000-0002-1825-0097",
        )
        self.node = BoardNode.objects.create(
            id=13,
            name="Example Project",
            node_type="project",
            url="https://example.org/project",
            order=2,
        )
        self.assignment = BoardAssignment.objects.create(
            id=17,
            person=self.person,
            node=self.node,
            role=self.role,
            note="Lead",
            order=3,
        )

    def test_admins_include_import_export(self):
        self.assertTrue(issubclass(PersonAdmin, ImportExportModelAdmin))
        self.assertTrue(issubclass(RoleTypeAdmin, ImportExportModelAdmin))
        self.assertTrue(issubclass(BoardNodeAdmin, ImportExportModelAdmin))
        self.assertTrue(issubclass(BoardAssignmentAdmin, ImportExportModelAdmin))
        self.assertTrue(issubclass(PublicationAdmin, ImportExportModelAdmin))

    def test_resources_export_board_data(self):
        person_row = PersonResource().export().dict[0]
        role_row = RoleTypeResource().export().dict[0]
        node_row = BoardNodeResource().export().dict[0]
        assignment_row = BoardAssignmentResource().export().dict[0]

        self.assertEqual(person_row["orcid"], "0000-0002-1825-0097")
        self.assertEqual(role_row["name"], "Coordinator")
        self.assertEqual(node_row["url"], "https://example.org/project")
        self.assertEqual(node_row["parent"], "")
        self.assertEqual(assignment_row["person"], 11)
        self.assertEqual(assignment_row["node"], 13)
        self.assertEqual(assignment_row["role"], 7)
        self.assertEqual(assignment_row["note"], "Lead")


@override_settings(STORAGES=TEST_STORAGES)
class PublicationAdminTests(TestCase):
    def setUp(self):
        Publication.objects.create(
            authors="Doe, J.",
            title="Example Publication",
            journal="Journal of Tests",
            citation="1(1), 1-2",
            year=2024,
            pages="1-2",
            pdf="example.pdf",
            dataset="data.csv",
            doi="10.1234/example",
        )

    def test_admin_includes_import_export(self):
        self.assertTrue(issubclass(PublicationAdmin, ImportExportModelAdmin))

    def test_resource_exports_publication(self):
        dataset = PublicationResource().export()
        self.assertEqual(dataset.dict[0]["title"], "Example Publication")
        self.assertEqual(dataset.dict[0]["pages"], "1-2")
        self.assertEqual(dataset.dict[0]["pdf"], "example.pdf")
        self.assertEqual(dataset.dict[0]["dataset"], "data.csv")
