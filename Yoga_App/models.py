from django.db import models


# Create your models here.
class MemberTable(models.Model):
  id = models.AutoField(primary_key=True)
  fullname = models.CharField(max_length=255)
  pass1 = models.CharField(max_length=255)
  pass2 = models.CharField(max_length=255)
  email = models.CharField(max_length=255)
  mobile = models.CharField(max_length=20)
  age = models.CharField(max_length=5)
  gender = models.CharField(max_length=20)
  disease = models.CharField(max_length=50, null=True, blank=True)


class ContactTable(models.Model):
  id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=255)
  email = models.CharField(max_length=255)
  subject = models.CharField(max_length=255)
  message = models.CharField(max_length=255)
  status = models.CharField(max_length=20, default="In Progress")


class YogaTable(models.Model):
  id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=100)
  image = models.ImageField(upload_to="static/img/")
  video_url = models.URLField(max_length=500)
  how_to_do = models.TextField(max_length=1500)
  benefits = models.TextField(max_length=1500)
  disease_code = models.CharField(max_length=5)
  contraindications = models.TextField(max_length=1000)


class DiseaseTable(models.Model):
  id = models.AutoField(primary_key=True)
  d_code = models.CharField(max_length=10)
  d_name = models.CharField(max_length=50)
  image = models.ImageField(upload_to="static/img/")
