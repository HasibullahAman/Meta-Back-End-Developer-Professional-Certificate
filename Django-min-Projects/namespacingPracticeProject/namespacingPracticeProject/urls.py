
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('demo/', include('manageName.urls')),
]


handler404 = 'namespacingPracticeProject.views.handler404'

