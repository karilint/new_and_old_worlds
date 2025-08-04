from django.test import TestCase
from django.urls import reverse
from .models import Publication


class PublicationViewTests(TestCase):
    def setUp(self):
        Publication.objects.create(
            authors="Doe, J.",
            title="Example Publication",
            journal="Journal of Tests",
            citation="1(1), 1-2",
            year=2024,
            doi="10.1234/example",
        )

    def test_publications_page_lists_entries(self):
        response = self.client.get(reverse("publications"))
        self.assertContains(response, "Example Publication")
        self.assertContains(response, "2024")
