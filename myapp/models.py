from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Register(AbstractUser):
    name=models.CharField(max_length=100, default="")
    age=models.IntegerField(default=0)
    username=models.CharField(max_length=150, default="", unique=True)
    password=models.CharField(max_length=120)
