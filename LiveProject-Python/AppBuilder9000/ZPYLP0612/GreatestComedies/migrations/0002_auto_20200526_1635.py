# Generated by Django 2.2.5 on 2020-05-26 23:35

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('GreatestComedies', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='comedies',
            managers=[
                ('Comedy', django.db.models.manager.Manager()),
            ],
        ),
    ]
