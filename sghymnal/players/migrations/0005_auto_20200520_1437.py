# Generated by Django 3.0.5 on 2020-05-20 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("players", "0004_bio_player"),
    ]

    operations = [
        migrations.AlterField(
            model_name="bio",
            name="lang",
            field=models.CharField(max_length=50, verbose_name="Language"),
        ),
    ]