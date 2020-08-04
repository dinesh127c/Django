from django.shortcuts import render, redirect

from . import models

# Create your views here.
from .models import Destination


def index(request):
    dest2 = Destination.objects.all()

    return render(request, 'index.html', {'dest2': dest2})


def places(request):
    if request.user.is_authenticated:
        return render(request, 'places.html')
    else:
        return redirect('login')


def travel(request):
    return redirect('/')


def contact(request):
    return render(request, 'contact.html')
