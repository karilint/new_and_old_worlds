from django.db import migrations


def copy_full_name_to_surname(apps, schema_editor):
    Person = apps.get_model("now", "Person")
    for person in Person.objects.all().only("id", "full_name", "surname"):
        if person.full_name and not person.surname:
            person.surname = person.full_name
            person.save(update_fields=["surname"])


def reverse_copy_full_name_to_surname(apps, schema_editor):
    Person = apps.get_model("now", "Person")
    for person in Person.objects.all().only("id", "full_name", "surname"):
        if person.surname and not person.full_name:
            person.full_name = person.surname
            person.save(update_fields=["full_name"])


class Migration(migrations.Migration):

    dependencies = [
        ("now", "0006_person_split_name_add_fields"),
    ]

    operations = [
        migrations.RunPython(copy_full_name_to_surname, reverse_copy_full_name_to_surname),
    ]
