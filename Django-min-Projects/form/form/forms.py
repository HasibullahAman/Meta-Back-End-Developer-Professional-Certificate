from django.shortcuts import render
from django import forms
# Create your views here.


class DemoForms(forms.Form):
    name = forms.CharField()