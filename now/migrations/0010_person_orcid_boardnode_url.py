from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("now", "0009_person_require_surname"),
    ]

    operations = [
        migrations.AddField(
            model_name="person",
            name="orcid",
            field=models.CharField(blank=True, max_length=19),
        ),
        migrations.AddField(
            model_name="boardnode",
            name="url",
            field=models.URLField(blank=True),
        ),
    ]
