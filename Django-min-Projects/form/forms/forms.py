from django.shortcuts import render
from django import forms
# Create your views here.

from .models import Logger

class LogForm(forms.ModelForm):
    class Meta:
        model = Logger
        fields = '__all__'
        