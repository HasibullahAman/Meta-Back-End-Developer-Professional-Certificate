from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharFeild(max_length = 255)
    author = models.CharFeild(max_length = 255)
    price  = models.models.DecimalField(max_digits=5, decimal_places=2)
    
    class Meta:
        indexes = [
            models.Index(fields=['price']),
        ]
    
