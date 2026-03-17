from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("now", "0008_person_remove_full_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="person",
            name="surname",
            field=models.CharField(max_length=255),
        ),
    ]
