# Generated by Django 4.2.14 on 2024-08-14 08:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='city',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='country',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='datefrom',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='dateto',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='martialstatus',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='state',
        ),
    ]
