import re

from django.core.validators import RegexValidator
from django.db import models
from django.templatetags.static import static


class Alert(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    start = models.DateTimeField(blank=True, null=True)
    end = models.DateTimeField(blank=True, null=True)
    duration_estimate = models.CharField(max_length=255, blank=True)

    class Meta:
        ordering = ["-start", "title"]

    def __str__(self) -> str:  # pragma: no cover - trivial
        return self.title


class Person(models.Model):
    surname = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255, blank=True)
    email = models.EmailField(blank=True)
    affiliation = models.CharField(max_length=255, blank=True)
    orcid = models.CharField(max_length=19, blank=True)

    class Meta:
        ordering = ["surname", "first_name", "id"]

    @property
    def display_name(self) -> str:
        if self.first_name:
            return f"{self.first_name} {self.surname}"
        return self.surname

    @property
    def orcid_url(self) -> str:
        if not self.orcid:
            return ""
        return f"https://orcid.org/{self.orcid}"

    def __str__(self) -> str:  # pragma: no cover - trivial
        return self.display_name


class RoleType(models.Model):
    name = models.CharField(max_length=100, unique=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "name"]

    def __str__(self) -> str:  # pragma: no cover - trivial
        return self.name


class BoardNode(models.Model):
    name = models.CharField(max_length=255)
    parent = models.ForeignKey(
        "self",
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name="children",
    )
    node_type = models.CharField(
        max_length=50,
        help_text="Examples: section, region, discipline, project, taxon, time.",
    )
    url = models.URLField(blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "name", "id"]

    @property
    def project_url(self) -> str:
        if self.url and self.node_type.lower() == "project":
            return self.url
        return ""

    def __str__(self) -> str:  # pragma: no cover - trivial
        return self.name


class BoardAssignment(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name="board_assignments")
    node = models.ForeignKey(BoardNode, on_delete=models.CASCADE, related_name="assignments")
    role = models.ForeignKey(
        RoleType,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name="board_assignments",
    )
    note = models.CharField(max_length=255, blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "id"]

    def __str__(self) -> str:  # pragma: no cover - trivial
        return f"{self.person} -> {self.node}"


class Publication(models.Model):
    """A bibliographic reference for the publications page."""
    authors = models.CharField(max_length=512)
    title = models.CharField(max_length=512)
    journal = models.CharField(max_length=512, blank=True)
    citation = models.CharField(
        max_length=512, blank=True, help_text="Volume, issue and pages"
    )
    year = models.PositiveIntegerField()
    pages = models.CharField(max_length=64, blank=True)
    pdf = models.CharField(max_length=512, blank=True)
    dataset = models.CharField(max_length=512, blank=True)
    doi = models.CharField(
        max_length=255,
        blank=True,
        validators=[
            RegexValidator(
                regex=r"^10\.\d{4,9}/[-._;()/:A-Z0-9]+$",
                flags=re.IGNORECASE,
                message="Enter a valid DOI.",
            )
        ],
    )

    class Meta:
        ordering = ["-year", "authors"]

    def __str__(self) -> str:  # pragma: no cover - trivial
        return f"{self.authors} ({self.year}) {self.title}"

    @property
    def pdf_link(self) -> str:
        if not self.pdf:
            return ""
        if self.pdf.startswith(("http://", "https://")):
            return self.pdf
        return static(f"now/pdf/{self.pdf}")

    @property
    def dataset_link(self) -> str:
        if not self.dataset:
            return ""
        if self.dataset.startswith(("http://", "https://")):
            return self.dataset
        return static(f"now/datasets/{self.dataset}")
