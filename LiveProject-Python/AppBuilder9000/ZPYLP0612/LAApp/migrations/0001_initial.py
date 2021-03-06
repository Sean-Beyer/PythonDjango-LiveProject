# Generated by Django 2.2.5 on 2020-05-01 23:45

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('genre', models.CharField(choices=[('SciFi & Fantasy', 'SciFi & Fantasy'), ('Literature', 'Literature'), ('Poetry', 'Poetry'), ('Non-Fiction', 'Non-Fiction'), ('Travel', 'Travel'), ('Crime/Detective', 'Crime/Detective'), ('Romance', 'Romance,'), ('Western', 'Western'), ('Horror', 'Horror'), ('Biography', 'Biography'), ("Children's Lit", "Children's Lit"), ('Young Adult Fiction', 'Young Adult Fiction'), ('Other', 'Other')], max_length=30)),
                ('city', models.CharField(max_length=30)),
                ('state', models.CharField(choices=[('Oregon', 'OR'), ('Washington', 'WA'), ('California', 'CA'), ('Alaska', 'AK'), ('Hawaii', 'HI')], max_length=15)),
                ('title', models.CharField(max_length=40)),
                ('publisher', models.CharField(blank=True, max_length=30, null=True)),
                ('published_year', models.PositiveIntegerField(blank=True, null=True)),
            ],
            managers=[
                ('Authors', django.db.models.manager.Manager()),
            ],
        ),
    ]
