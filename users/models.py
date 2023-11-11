from django.db import models
from django.contrib.auth.models import AbstractUser
from tasks.models import *

# Create your models here.
class User(AbstractUser):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

class Manager(models.Model):
    id_manger = models.ForeignKey('User', on_delete=models.CASCADE, unique=True)
    name = models.TextField()
    Addres_location = models.TextField()

class Curier(models.Model):
    id_curier = models.ForeignKey('User', on_delete=models.CASCADE, unique=True)
    id_manager = models.ForeignKey('Manager', on_delete=models.CASCADE)
    Addres_start_location = models.TextField()
    grade = models.TextField() #junior, middle, senior
    Time_in_work = models.PositiveSmallIntegerField() #Продолжительность рабочего дня
