# Generated by Django 3.0.5 on 2020-06-09 17:21

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('players', '0004_auto_20200526_1315'),
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('instructions', models.CharField(max_length=255, verbose_name='Instructions')),
                ('lyrics', models.TextField(verbose_name='Lyrics')),
                ('reference_title', models.CharField(blank=True, max_length=255, verbose_name='Reference Link')),
                ('reference_link', models.URLField(blank=True, max_length=255, verbose_name='Reference URL')),
                ('sheet_music_link', models.URLField(blank=True, max_length=255, verbose_name='Sheet Music Link')),
                ('legend', models.CharField(blank=True, max_length=255, verbose_name='Legend')),
                ('capo_signal', models.CharField(blank=True, max_length=255, verbose_name='Capo Signal')),
                ('player', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='players.Player')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
