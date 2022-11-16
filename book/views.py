from django.http import HttpResponse


# Create your views here.

def welcome(request):
    return HttpResponse("<h1>Hello World!!!</h1>")
