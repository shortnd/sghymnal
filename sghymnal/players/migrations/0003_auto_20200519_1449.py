# Generated by Django 3.0.5 on 2020-05-19 19:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0002_auto_20200519_1357'),
    ]

    operations = [
        migrations.RenameField(
            model_name='player',
            old_name='postition',
            new_name='position',
        ),
    ]
