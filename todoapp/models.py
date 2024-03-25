from django.db import models
from django import forms
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model


# Create your models here.




class Task(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    taskId = models.AutoField(primary_key=True)
    title = models.CharField(max_length=30)
    done = models.BooleanField()
    
    
    
    