from django.shortcuts import render
from django.http import HttpResponse
from forms.forms import InputForm


def form_view(request):
    form = InputForm()
    context = {"Form": form}
    return render(request,"home.html",context)
