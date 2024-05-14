from django.db import models
from unicodedata import name
# Create your models here.

class Menuitems(models.Model):
    name = models.CharField(max_length = 100)
    course = models.CharField(max_length = 100)
    year = models.IntegerField(default=2000)
    
    
    
    
    