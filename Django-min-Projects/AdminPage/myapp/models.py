from django.db import models

# Create your models here.

class Reservation(models.Model):
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=300,blank = True)
    time = models.TimeField()
    count = models.IntegerField()
    notes = models.CharField(max_length = 300, blank = True)
    
    
    
       