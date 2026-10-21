from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [("now", "0012_seed_notices")]

    operations = [
        migrations.AlterModelOptions(
            name="person",
            options={"ordering": ["surname", "first_name", "id"]},
        ),
    ]
