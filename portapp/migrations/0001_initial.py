# Generated by Django 4.2.14 on 2024-08-13 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='userprofile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=200)),
                ('surname', models.CharField(max_length=200)),
                ('gender', models.CharField(max_length=200)),
                ('DOB', models.CharField(max_length=20)),
                ('martialstatus', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=200)),
                ('country', models.CharField(max_length=200)),
                ('mobilenumber', models.CharField(max_length=20)),
                ('email', models.EmailField(blank=True, max_length=255, null=True)),
                ('graduation', models.CharField(max_length=200)),
                ('percentage', models.IntegerField()),
                ('university', models.CharField(max_length=300)),
                ('projecttitle', models.CharField(blank=True, max_length=200, null=True)),
                ('projectdescription', models.CharField(blank=True, max_length=200, null=True)),
                ('projectimg', models.ImageField(upload_to='porject_media')),
                ('projectlink', models.URLField(blank=True, null=True)),
                ('additionalcourses', models.CharField(max_length=300)),
                ('experience', models.CharField(max_length=300)),
                ('companyname', models.CharField(max_length=300)),
                ('jobposition', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=200)),
                ('datefrom', models.DateField()),
                ('dateto', models.DateField()),
                ('additionalinformation', models.CharField(max_length=200)),
                ('skills', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]
