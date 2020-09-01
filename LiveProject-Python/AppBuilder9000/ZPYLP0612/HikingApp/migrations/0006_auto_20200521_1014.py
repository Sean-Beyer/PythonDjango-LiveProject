# Generated by Django 2.2.5 on 2020-05-21 17:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HikingApp', '0005_auto_20200520_1733'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hikes',
            name='Difficulty',
            field=models.CharField(choices=[('easy', 'easy'), ('moderate', 'moderate'), ('hard', 'hard')], default='easy', max_length=10),
        ),
        migrations.AlterField(
            model_name='hikes',
            name='EndTime',
            field=models.TimeField(default=datetime.time(10, 0)),
        ),
        migrations.AlterField(
            model_name='hikes',
            name='Rating',
            field=models.DecimalField(choices=[(1, 1), (1.5, 1.5), (2, 2), (2.5, 2.5), (3, 3), (3.5, 3.5), (4, 4), (4.5, 4.5), (5, 5)], decimal_places=1, default=5, max_digits=2),
        ),
    ]