# Generated by Django 3.0.5 on 2020-05-26 15:37

import autoslug.fields
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields
import sghymnal.players.models
import sorl.thumbnail.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Player",
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
                ("name", models.CharField(max_length=255, verbose_name="Player Name")),
                (
                    "slug",
                    autoslug.fields.AutoSlugField(
                        editable=False,
                        populate_from="name",
                        unique=True,
                        verbose_name="Player Slug",
                    ),
                ),
                (
                    "country",
                    django_countries.fields.CountryField(
                        blank=True, max_length=2, verbose_name="Player Country"
                    ),
                ),
                (
                    "position",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("Forward", "Forward"),
                            ("Defender", "Defender"),
                            ("Midfielder", "Midfielder"),
                            ("Goalkeeper", "Goalkeeper"),
                            ("Head Coach", "Head Coach"),
                            ("Assistant Coach", "Assistant Coach"),
                            ("Goalkeeper Coach", "Goalkeeper Coach"),
                            ("Technical Director", "Technical Director"),
                            ("Associate Head Coach", "Associate Head Coach"),
                        ],
                        max_length=50,
                        verbose_name="Position",
                    ),
                ),
                (
                    "squad_number",
                    models.IntegerField(blank=True, verbose_name="Players Number"),
                ),
                (
                    "team",
                    models.CharField(
                        blank=True,
                        max_length=255,
                        null=True,
                        verbose_name="Player's Team",
                    ),
                ),
                (
                    "twitter",
                    models.CharField(
                        blank=True, max_length=255, verbose_name="Twitter"
                    ),
                ),
                (
                    "instagram",
                    models.CharField(
                        blank=True, max_length=255, verbose_name="Instagram"
                    ),
                ),
                (
                    "thumbnail",
                    sorl.thumbnail.fields.ImageField(
                        blank=True,
                        upload_to=sghymnal.players.models.thumnail_upload_path,
                        verbose_name="Player Thumbnail",
                    ),
                ),
            ],
            options={"abstract": False,},
        ),
        migrations.CreateModel(
            name="PlayerImage",
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
                    "image",
                    sorl.thumbnail.fields.ImageField(
                        upload_to=sghymnal.players.models.image_upload_path,
                        verbose_name="Player Image",
                    ),
                ),
                (
                    "player",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="images",
                        to="players.Player",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Bio",
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
                ("lang", models.CharField(max_length=50, verbose_name="Language")),
                ("bio", models.TextField(verbose_name="Bio")),
                (
                    "player",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="bios",
                        to="players.Player",
                    ),
                ),
            ],
        ),
    ]
