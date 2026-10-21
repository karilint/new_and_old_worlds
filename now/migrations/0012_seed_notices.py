from django.db import migrations


def create_notices(apps, schema_editor):
    Notice = apps.get_model("now", "Notice")
    Notice.objects.create(
        heading="The next NOW symposium",
        text="will take place in Leiden, tentatively in the Fall of 2027. More information will follow soon.",
        priority=10,
    )
    Notice.objects.create(
        heading="Latest NOW circular",
        text="The latest circular can be found here:",
        link_url="/static/now/circulars/NOW_circular_20260302.pdf",
        link_text="Read the circular (PDF)",
    )


class Migration(migrations.Migration):
    dependencies = [("now", "0011_notice")]
    operations = [migrations.RunPython(create_notices, migrations.RunPython.noop)]
