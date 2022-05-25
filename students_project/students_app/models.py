from django import forms
from django.db import models
from django.forms import ModelForm
from django import forms

# Create your models here.
class Students(models.Model):
    # ID = models.IntegerField(default=0)
    name = models.CharField(max_length=30)
    age = models.IntegerField(default=0)
    address = models.CharField(max_length=50)
    mobile_number = models.CharField(max_length=15)
    def __str__(self):
        return self.name

class Teacher(models.Model):
    # ID = models.IntegerField(default=0)
    name = models.CharField(max_length=30)
    age = models.IntegerField(default=0)
    address = models.CharField(max_length=50)
    def __str__(self):
        return self.name

#Create form from Model
class Teacher(ModelForm):
    model = Teacher
    fields= ['name', 'age', 'address']