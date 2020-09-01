# Generated by Django 2.2.5 on 2020-06-27 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SFToons', '0004_auto_20200619_1537'),
    ]

    operations = [
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('bulk', models.CharField(max_length=100)),
                ('price', models.IntegerField(max_length=100)),
                ('level', models.IntegerField(max_length=100)),
                ('damage', models.CharField(max_length=100)),
                ('range', models.IntegerField(max_length=100)),
                ('critical', models.CharField(max_length=100)),
                ('special', models.CharField(max_length=100)),
                ('capacity', models.IntegerField(max_length=100)),
                ('usage', models.IntegerField(max_length=100)),
                ('description', models.CharField(max_length=100)),
            ],
        ),
    ]
