# Generated by Django 4.0.5 on 2023-10-13 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Yoga_App', '0023_remove_diseasetable_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membertable',
            name='disease',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
