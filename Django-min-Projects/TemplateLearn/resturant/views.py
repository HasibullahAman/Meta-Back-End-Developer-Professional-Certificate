from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def about(requst):
    about_content = {"about": "this is my world, I live alone and I dont have anything in this world yet!, but I have something "} 
    return render(requst, 'about.html',about_content)
