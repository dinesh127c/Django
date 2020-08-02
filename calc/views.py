from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'Home.html', {'name': 'bye hai 123 456'})


def add(request):
    val1 = int(request.POST["num1"])
    val2 = int(request.POST["num2"])
    res = val1 + val2

    return render(request, 'Result.html', {'result': res})

