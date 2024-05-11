from django.http import HttpResponse, HttpResponseNotFound
# Create your views here.


def handler404(request, exception):
    return HttpResponse("404: Page not Found!")

def my_view(request):
    if condition == True:
        return HttpResponseNotFound("<h1> Page not found</h1>")
    else:
        return HttpResponse("<h1>Page found</h1")


def home(request):
    return HttpResponse("Little Limmon !")