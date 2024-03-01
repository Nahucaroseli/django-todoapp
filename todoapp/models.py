from django.db import models

# Create your models here.




class Task(models.Model):
    taskId = models.AutoField(primary_key=True)
    title = models.CharField(max_length=30)
    done = models.BooleanField()
    
    
