# Generated by Django 2.2.5 on 2020-05-20 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HikingApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hikes',
            old_name='date',
            new_name='Date',
        ),
        migrations.RenameField(
            model_name='hikes',
            old_name='amountCompleted',
            new_name='Hike_Name',
        ),
        migrations.RenameField(
            model_name='hikes',
            old_name='rating',
            new_name='Rating',
        ),
        migrations.RenameField(
            model_name='hikes',
            old_name='time',
            new_name='Time',
        ),
        migrations.RemoveField(
            model_name='hikes',
            name='name',
        ),
        migrations.AddField(
            model_name='hikes',
            name='Completed',
            field=models.CharField(choices=[('True', 'True'), ('False', 'False')], default='True', max_length=5),
        ),
    ]
