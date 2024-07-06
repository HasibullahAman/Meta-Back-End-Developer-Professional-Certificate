from django.shortcuts import render
from django.http import HttpResponse
from .models import Menu
# Create your views here.


# def about(requst):
#     about_content = {"about": "this is my world, I live alone and I dont have anything in this world yet!, but I have something "} 
#     return render(requst, 'about.html',about_content)


def  mylist(request):
    mylist_content = {"person" : [
        {"name": "Ahmad",
         "age": 20,
         "job": "student"},
        {
            "name": "Ali",
            "age": 23,
            "job": "teacher"
        },
        {
            "name": "qasim",
            "age": 25,
            "job": "student"
        },
        ]}
    return render(request, 'mylist.html', mylist_content)



def menu_by_id(request):
    newMenu = Menu.objects.all()
    newMenu_dict = {'menu': newMenu}
    return render(request,'menu_cards.html', newMenu_dict)



def home(request):
    return render(request, 'home.html')
def about(request):
    return render(request, 'about.html')

def menu(request):
    return render(request, 'menu.html')





