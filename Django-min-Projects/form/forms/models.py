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

class Logger(forms.Form):
    name = forms.CharField(max_length=100, required= False)
    last_name = forms.CharField(max_length=100,)
    time_log = forms.TimeField(help_text= "Please Enter a date like a human!")