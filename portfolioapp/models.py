from django.db import models

# Create your models here.
class message(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    response = models.CharField(max_length=500)