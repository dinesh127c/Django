from django.shortcuts import render

from . import models

# Create your views here.
from .models import Destination


def index(request):
    dest1 = Destination()
    dest1.name = "Mumbai"
    dest1.image = "destination_1.jpg"
    dest1.desc = "A city that never sleeps"
    dest1.offer = False
    dest1.price = 700

    dest2 = Destination()
    dest2.name = "Simula"
    dest2.image = "destination_2.jpg"
    dest2.desc = "A beautiful place"
    dest2.offer = True
    dest2.price = 100

    dest3 = Destination()
    dest3.name = "Amiga"
    dest3.image = "destination_3.jpg"
    dest3.desc = "A southern hill"
    dest3.offer = False
    dest3.price = 10000

    dest = [dest1, dest2, dest3]

    return render(request, 'index.html', {'dest2': dest})
