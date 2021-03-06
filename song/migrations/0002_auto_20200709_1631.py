# Generated by Django 2.2.12 on 2020-07-09 08:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('song', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='song',
            old_name='label_set',
            new_name='lable_set',
        ),
        migrations.RemoveField(
            model_name='song',
            name='album_id',
        ),
        migrations.RemoveField(
            model_name='song',
            name='lyric_id',
        ),
        migrations.AddField(
            model_name='song',
            name='album',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='song.Album'),
        ),
        migrations.AddField(
            model_name='song',
            name='duration',
            field=models.IntegerField(default=1, verbose_name='时长'),
        ),
        migrations.AlterField(
            model_name='lyric',
            name='song',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='song.Song'),
        ),
    ]
