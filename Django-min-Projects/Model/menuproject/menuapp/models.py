from django.db import models
from unicodedata import name
# Create your models here.

class Menuitems(models.Model):
    name = models.CharField(max_length = 100)
    courses = models.CharField(max_length = 100)
    year = models.IntegerField(default=2000)
    
    


class MenuCategory(models.Model):
    menu_category_name = models.CharField(max_length = 100)
    
    
class Menu(models.Model):
    menu_item = models.CharField(max_length =200)
    price = models.IntegerField(null = False)
    category_id = models.ForeignKey(MenuCategory, on_delete= models.PROTECT , default = None)
    
    
class customers(models.Model):
    name = models.CharField(max_length = 100)
    
    
class Vehicle(moedls.Model):
    name = models.CharField(max_length = 100)
    customers= models.ForeignKey(customers,on_delete=models.CASCADE,related_name="vehicles")
    
    

    
    
    
     