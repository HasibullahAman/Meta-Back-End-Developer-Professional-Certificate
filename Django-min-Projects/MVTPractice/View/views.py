from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
# Create your views here.

def home(request):
    path = request.path
    # return HttpResponse(path,content_type="text/html",charset="UTF-8")
    Response = HttpResponse("this is correct!")
    return Response 
    


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


def menuItems(request, dish):
    item = {
        "pasta": "A versatile and popular dish made from various types of dough, such as wheat, rice, or even potatoes. It is often served with various toppings, sauces, and cheeses.",
        "falafel": "A popular Middle Eastern dish made from ground chickpeas, which are seasoned with spices and then deep-fried until crispy. It is often served with hummus, tahini, or pickles.",
        "cheesecake": "A dessert consisting of a sweet, crumbly base made from a mixture of cream cheese, sugar, and eggs, often topped with a variety of fruit, chocolate, or other fillings."
    }
    
    discriptions = item[dish]
    return HttpResponse(f"<h2> {dish} </h2>" + discriptions)


