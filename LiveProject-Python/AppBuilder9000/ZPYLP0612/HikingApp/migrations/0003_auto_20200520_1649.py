# Generated by Django 2.2.5 on 2020-05-20 23:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HikingApp', '0002_auto_20200520_1259'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hikes',
            name='Time',
        ),
        migrations.AddField(
            model_name='hikes',
            name='StartTime',
            field=models.TimeField(default=datetime.datetime.now),
        ),
    ]
