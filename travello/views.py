from django.shortcuts import render

from . import models

# Create your views here.
from .models import Destination


def index(request):

    dest2 = Destination.objects.all()

    return render(request, 'index.html', {'dest2': dest2})
