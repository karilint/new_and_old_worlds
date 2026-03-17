from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("now", "0007_copy_person_full_name_to_surname"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="person",
            name="full_name",
        ),
    ]
