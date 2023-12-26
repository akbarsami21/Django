from django.db import models

# Create your models here.
class Anchor(models.Model):
    aid=models.IntegerField()
    name=models.CharField(max_length=200)
    email=models.EmailField(max_length=200)
    phone=models.IntegerField(max_length=11)
    
