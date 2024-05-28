from django.shortcuts import render
from django import forms
# Create your views here.

shifts = (
    
    ("1" : "Morning"),
    ("2" : "Afternoon"),
    ("3" : "Evening"),
    ("4" : "Night"),
)

class InputForm(forms.Form):
    name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    shift = forms.ChoiceField(choices= Shifts)
    time_log = forms.TimeField()