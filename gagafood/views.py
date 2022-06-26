# from django.http import HttpResponse
from django.http import HttpResponse
from django.shortcuts import render, redirect
from restaurant.models import *
from dish.models import Dish


def index(request):
    return render(request, 'gagafood/index.html')


def catalogue(request):
    restaurants = Restaurants.objects.all()
    category = Category.objects.all()
    context = {
        'restaurants': restaurants,
        'category': category,
        # 'cat_selected': restaurant_id,
    }
    return render(request, 'gagafood/catalogue.html', context=context)


def show_restaurant(request, restaurant_id):
    restaurants = Restaurants.objects.all()
    context = {
        'restaurants': restaurants,
        'restaurant_selected': restaurant_id,
        'dish': Dish.objects.all(),
        # 'dish': dish,
    }
    return render(request, 'gagafood/restaurant.html', context)


def show_menu(request, restaurant_id):
    dish = Dish.objects.all()
