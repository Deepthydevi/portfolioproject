# Generated by Django 4.2.14 on 2024-08-14 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portapp', '0002_remove_userprofile_city_remove_userprofile_country_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='additionalinformation',
            new_name='aboutme',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='firstname',
            new_name='fullname',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='location',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='surname',
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='skills',
            field=models.CharField(default=1234, max_length=200),
            preserve_default=False,
        ),
    ]
