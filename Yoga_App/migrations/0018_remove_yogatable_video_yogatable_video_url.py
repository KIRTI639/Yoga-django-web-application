# Generated by Django 4.0.5 on 2023-05-12 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Yoga_App', '0017_yogatable_video'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='yogatable',
            name='video',
        ),
        migrations.AddField(
            model_name='yogatable',
            name='video_url',
            field=models.URLField(default=1, max_length=500),
            preserve_default=False,
        ),
    ]