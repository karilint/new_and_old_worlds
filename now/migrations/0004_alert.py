from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("now", "0003_alter_publication_doi"),
    ]

    operations = [
        migrations.CreateModel(
            name="Alert",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=255)),
                ("description", models.TextField(blank=True)),
                ("start", models.DateTimeField(blank=True, null=True)),
                ("end", models.DateTimeField(blank=True, null=True)),
                ("duration_estimate", models.CharField(blank=True, max_length=255)),
            ],
            options={
                "ordering": ["-start", "title"],
            },
        ),
    ]
