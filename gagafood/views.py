# from django.http import HttpResponse
from django.shortcuts import render, redirect

from restaurant.models import *


def index(request):
    return render(request, 'gagafood/index.html')


def catalogue(request):
    restaurants = Restaurants.objects.all()
    return render(request, 'gagafood/catalogue.html', {'restaurants': restaurants})
