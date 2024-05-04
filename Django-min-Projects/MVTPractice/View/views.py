from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    content = "<html><head><h1>Wellcome to Little Lemon Resturant</h1></html>"
    return HttpResponse(content)
