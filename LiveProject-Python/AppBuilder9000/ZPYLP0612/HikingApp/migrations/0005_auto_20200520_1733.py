# Generated by Django 2.2.5 on 2020-05-21 00:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HikingApp', '0004_auto_20200520_1658'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hikes',
            name='EndTime',
            field=models.TimeField(default=datetime.time(16, 0)),
        ),
    ]