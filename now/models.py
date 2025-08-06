import re

from django.db import models
from django.core.validators import RegexValidator
from django.templatetags.static import static


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
