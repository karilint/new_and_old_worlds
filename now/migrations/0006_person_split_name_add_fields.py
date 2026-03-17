from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("now", "0005_board_tree"),
    ]

    operations = [
        migrations.AddField(
            model_name="person",
            name="first_name",
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name="person",
            name="surname",
            field=models.CharField(blank=True, default="", max_length=255),
            preserve_default=False,
        ),
    ]
