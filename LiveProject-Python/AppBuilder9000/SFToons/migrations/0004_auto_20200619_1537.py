# Generated by Django 2.2.5 on 2020-06-19 22:37

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('SFToons', '0003_character_society'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='character',
            managers=[
                ('Characters', django.db.models.manager.Manager()),
            ],
        ),
    ]