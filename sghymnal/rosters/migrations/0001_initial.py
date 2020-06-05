# Generated by Django 3.0.5 on 2020-06-04 04:07

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("players", "0004_auto_20200526_1315"),
    ]

    operations = [
        migrations.CreateModel(
            name="Roster",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "uuid",
                    models.UUIDField(
                        db_index=True, default=uuid.uuid4, editable=False, unique=True
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("title", models.CharField(max_length=255)),
                ("season", models.CharField(blank=True, max_length=255)),
                ("active", models.BooleanField(default=True)),
                ("default", models.BooleanField(default=False)),
                ("players", models.ManyToManyField(to="players.Player")),
            ],
            options={"abstract": False,},
        ),
    ]
