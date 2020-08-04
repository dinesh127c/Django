from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('places', views.places, name='places'),
    path('travel', views.travel, name='travel'),
    path('contact', views.contact, name='contact')
]
