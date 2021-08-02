from django.db import models
from django.db.models.base import Model, ModelState
from django.db.models.fields import DateField, TextField
from django.db.models.fields.files import ImageField

# Create your models here.
class registers(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password_1 = models.CharField(max_length=50)
    password_2 = models.CharField(max_length=50)

    def __str__(self):
         return self.first_name
