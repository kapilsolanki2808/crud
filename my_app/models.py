from django.db import models
from django.forms import ModelForm
# Create your models here.

class About(models.Model):
  ids = models.AutoField(primary_key=True)
  first_name = models.CharField(max_length=200)
  last_name = models.CharField(max_length=200)
  roll_number = models.IntegerField(default=100)
  mobile_number = models.IntegerField()
  image = models.ImageField(upload_to='img/',null=True,blank=True)

  def __str__(self):
    return self.first_name

# class PickForm(ModelForm):
#     class Meta:
#         Model = About

# from django.contrib.auth.models import AbstractUser,AbstractBaseUser
# print(AbstractUser)