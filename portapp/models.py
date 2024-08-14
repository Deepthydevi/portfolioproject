from django.db import models
from django.db.models import CharField,ImageField,IntegerField

# Create your models here.
class userprofile(models.Model):
    fullname=models.CharField(max_length=200)
    gender=models.CharField(max_length=200)
    DOB=models.CharField(max_length=20, null=True, blank=True)
    address=models.CharField(max_length=200)
    mobilenumber = models.CharField(max_length=300)
    email = models.EmailField(max_length=255, blank=True, null=True)
    graduation = models.CharField(max_length=200)
    percentage=models.IntegerField()
    university=models.CharField(max_length=300)
    additionalcourses = models.CharField(max_length=300)
    skills = models.CharField(max_length=200)
    projecttitle = models.CharField(max_length=200, blank=True, null=True)
    projectdescription = models.CharField(max_length=200, blank=True, null=True)
    projectimg = models.ImageField(upload_to='porject_media')
    projectlink = models.URLField(max_length=200, blank=True, null=True)
    experience = models.CharField(max_length=300)
    companyname=models.CharField(max_length=300)
    jobposition=models.CharField(max_length=200)
    aboutme=models.CharField(max_length=200)

def __str__(self):
    return '{}'.format(self.fullname)
