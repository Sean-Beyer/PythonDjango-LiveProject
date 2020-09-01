# Generated by Django 2.2.5 on 2020-05-21 19:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HikingApp', '0008_auto_20200521_1149'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hikes',
            name='DateStart',
        ),
        migrations.AddField(
            model_name='hikes',
            name='Date',
            field=models.DateField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='hikes',
            name='StartTime',
            field=models.TimeField(blank=True, default=None, null=True),
        ),
    ]