from . import views
from django.contrib import admin
from django.urls import path
# Create your views here.


urlpatterns = [
    path('home/', views.form_view)
]
