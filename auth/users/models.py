from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class user(AbstractUser):
    name=models.CharField(max_length=250)
    email=models.CharField(max_length=250,unique=True)
    password=models.CharField(max_length=250)
    username=None

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=[]
