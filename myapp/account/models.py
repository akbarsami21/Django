from django.db import models

# Create your models here.
class Teacher(models.Model):
    tid=models.IntegerField()
    tname=models.CharField(max_length=200)
    temail=models.CharField(max_length=100)