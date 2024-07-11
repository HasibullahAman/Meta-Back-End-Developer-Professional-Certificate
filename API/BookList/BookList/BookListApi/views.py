from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view


@api_view()
def books(request):
    return Response("List of book",status = status.HTTP_200_ok)


# Create your views here.
