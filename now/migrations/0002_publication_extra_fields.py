from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("now", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="publication",
            name="dataset",
            field=models.CharField(blank=True, max_length=512),
        ),
        migrations.AddField(
            model_name="publication",
            name="pages",
            field=models.CharField(blank=True, max_length=64),
        ),
        migrations.AddField(
            model_name="publication",
            name="pdf",
            field=models.CharField(blank=True, max_length=512),
        ),
    ]
