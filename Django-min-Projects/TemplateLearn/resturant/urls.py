from django.urls import path
from . import views

urlpatterns = [
    path('about',views.about),
    path('newlist',views.mylist),
    path('menu_card',views.menu_by_id),
    path('home',views.home),
    path('menu',views.menu),
    
]
