from django.shortcuts import render
from django.db import IntegrityError
from django.http import HttpResponse, JsonResponse
from .models import Book
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict


# Create your views here.

@csrf_exempt
def books(request):
    if request.method == 'GET':
        books = Book.objects.all().values()
        return JsonResponse({"books":list(books)})
    elif request.method == 'POST':
        title = request.get('title')
        author = request.get('author')
        price = request.get('price')
        
        books = Book(
            title = title,
            author = author,
            price = price
        )
        try:
            books.save()
        except IntegrityError:
            return JsonResponse({'error':'true','message':'required field missing'},status=400)
        