# Generated by Django 3.0.5 on 2020-05-19 18:57

from django.db import migrations, models
import sghymnal.players.models
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lang', models.CharField(max_length=50, verbose_name='Bio Language')),
                ('bio', models.TextField(verbose_name='Bio')),
            ],
        ),
        migrations.AlterField(
            model_name='player',
            name='thumbnail',
            field=sorl.thumbnail.fields.ImageField(blank=True, upload_to=sghymnal.players.models.thumnail_upload_path, verbose_name='Player Thumbnail'),
        ),
    ]
