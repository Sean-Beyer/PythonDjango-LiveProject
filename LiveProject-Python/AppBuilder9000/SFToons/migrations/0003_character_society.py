# Generated by Django 2.2.5 on 2020-06-18 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SFToons', '0002_auto_20200617_1419'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='Society',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
