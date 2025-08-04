from django.db import models


class Publication(models.Model):
    """A bibliographic reference for the publications page."""
    authors = models.CharField(max_length=512)
    title = models.CharField(max_length=512)
    journal = models.CharField(max_length=512, blank=True)
    citation = models.CharField(max_length=512, blank=True, help_text="Volume, issue and pages")
    year = models.PositiveIntegerField()
    doi = models.CharField(max_length=255, blank=True)

    class Meta:
        ordering = ["-year", "authors"]

    def __str__(self) -> str:  # pragma: no cover - trivial
        return f"{self.authors} ({self.year}) {self.title}"
