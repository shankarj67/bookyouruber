from django.db import models


# Create your models here.
class Uber(models.Model):
    source = models.CharField(max_length=150)
    destination = models.CharField(max_length=150)
    time = models.TimeField()
    email = models.EmailField()
    
