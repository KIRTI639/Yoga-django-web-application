from django.db import models
from django.core.validators import FileExtensionValidator

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
  disease = models.CharField(max_length=50)
  # city = models.CharField(max_length=50, default="UP", null=True, blank=True)

  # def __str__(self) -> str:
  #   return f"{self.id} / {self.fullname} / {self.email}"

class ContactTable(models.Model):
  id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=255)
  email = models.CharField(max_length=255)
  subject = models.CharField(max_length=255)
  message = models.CharField(max_length=255)
  status = models.CharField(max_length=20, default="In Progress")

  # def __str__(self) -> str:
  #   return f"{self.id} / {self.name} / {self.email}"
  
# id Name image description usedfor 
class YogaTable(models.Model):
  id = models.AutoField(primary_key=True)
  # y_code = models.CharField(max_length=5)
  name = models.CharField(max_length=100)
  image = models.ImageField(upload_to="static/img/")
  video_url = models.URLField(max_length=500)
  how_to_do = models.TextField(max_length=1500)
  benefits = models.TextField(max_length=1500)
  disease_code = models.CharField(max_length=5)
  contraindications = models.TextField(max_length=1000)
  # def __str__(self):
  #   return f"{self.id} / {self.disease_code} / {self.name}"

class DiseaseTable(models.Model):
  id = models.AutoField(primary_key=True)
  d_code = models.CharField(max_length=10)
  d_name = models.CharField(max_length=50)
  image = models.ImageField(upload_to="static/img/")

  # def __str__(self) -> str:
  #   return f"{self.id} / {self.d_code} / {self.d_name}"