# Generated by Django 2.2.5 on 2020-05-21 16:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ShoeCloset', '0003_auto_20200520_1428'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shoeclosetmodel',
            name='notes',
        ),
    ]
