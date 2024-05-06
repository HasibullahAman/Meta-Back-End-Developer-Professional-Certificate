from django.urls import path
from . import views
urlpatterns = [
    path('home/main', views.home, name='home'),
    path("display_date",views.display_date),
    path("<str:dish>",views.menuItems),
    
]


