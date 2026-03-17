from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("now", "0004_alert"),
    ]

    operations = [
        migrations.CreateModel(
            name="BoardNode",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=255)),
                ("node_type", models.CharField(help_text="Examples: section, region, discipline, project, taxon, time.", max_length=50)),
                ("order", models.PositiveIntegerField(default=0)),
                ("parent", models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name="children", to="now.boardnode")),
            ],
            options={
                "ordering": ["order", "name", "id"],
            },
        ),
        migrations.CreateModel(
            name="Person",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("full_name", models.CharField(max_length=255)),
                ("email", models.EmailField(blank=True, max_length=254)),
                ("affiliation", models.CharField(blank=True, max_length=255)),
            ],
            options={
                "ordering": ["full_name"],
            },
        ),
        migrations.CreateModel(
            name="RoleType",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=100, unique=True)),
                ("order", models.PositiveIntegerField(default=0)),
            ],
            options={
                "ordering": ["order", "name"],
            },
        ),
        migrations.CreateModel(
            name="BoardAssignment",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("note", models.CharField(blank=True, max_length=255)),
                ("order", models.PositiveIntegerField(default=0)),
                ("node", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="assignments", to="now.boardnode")),
                ("person", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="board_assignments", to="now.person")),
                ("role", models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name="board_assignments", to="now.roletype")),
            ],
            options={
                "ordering": ["order", "id"],
            },
        ),
    ]
