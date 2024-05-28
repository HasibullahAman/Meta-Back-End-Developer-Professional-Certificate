from django.db import models


# Create your models here.


class Person(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    
    
    """
    Django automatically names the table as appname_modelname, which you can override by assigning the desired name
    to db_table parameter of the Meta class, to be declared inside the model class.
    
    class Student(CommonInfo): 
    # ... 
    class Meta(CommonInfo.Meta): 
        db_table = 'student_info' 
        
    """