from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("now", "0010_person_orcid_boardnode_url")]

    operations = [
        migrations.CreateModel(
            name="Notice",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("heading", models.CharField(max_length=255)),
                ("text", models.TextField()),
                ("priority", models.PositiveIntegerField(default=0, help_text="Higher values are shown first.")),
                ("active", models.BooleanField(default=True)),
                ("starts_at", models.DateTimeField(blank=True, null=True)),
                ("ends_at", models.DateTimeField(blank=True, null=True)),
                ("link_url", models.URLField(blank=True)),
                ("link_text", models.CharField(blank=True, max_length=100)),
            ],
            options={"ordering": ["-priority", "starts_at", "heading", "id"]},
        ),
    ]
