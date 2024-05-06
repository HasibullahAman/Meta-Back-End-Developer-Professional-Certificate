from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
# Create your views here.

def home(request):
    content = "<html><head><h1>Wellcome to Little Lemon Resturant</h1></html>"
    return HttpResponse(content)


def myview(request):
    if request.method =='GET':
        pass
        # Perform read or delate operation in model
    if request.method == 'POST':
        pass
        # Perform create or update operation in model   
        context = {}
    return render(request,'index.html',context)

def  display_date(request):
    date_joined = datetime.today().year
    return HttpResponse(date_joined)


